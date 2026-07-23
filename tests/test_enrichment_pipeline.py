from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import export_enrichment_input
import import_enrichment
import run_enrichment
from enrichment_schema import EnrichmentValidationError, validate_enrichment_item


FIELDNAMES = [
    "paper_id",
    "title",
    "url",
    "year",
    "authors",
    "candidate_topic",
    "source",
    "paper_type",
    "status",
    "enrichment_status",
]


def enrichment_item(paper_id: int = 1) -> dict:
    return {
        "paper_id": paper_id,
        "summary": "summary",
        "why_it_matters": "why",
        "method_setup": "method",
        "key_claims": ["claim"],
        "limitations": ["limitation"],
        "evaluates": [],
        "builds_on_unresolved": [],
        "compares_to_unresolved": [],
    }


def paper_row(paper_id: int, enrichment_status: str = "pending") -> dict[str, str]:
    return {
        "paper_id": str(paper_id),
        "title": f"Paper {paper_id}",
        "url": f"https://arxiv.org/abs/2401.{paper_id:05d}",
        "year": "2024",
        "authors": "Author",
        "candidate_topic": "memory-context",
        "source": "arxiv",
        "paper_type": "system",
        "status": "ingested",
        "enrichment_status": enrichment_status,
    }


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


class EnrichmentSchemaTests(unittest.TestCase):
    def test_rejects_wrong_paper_id_and_non_string_list_entries(self) -> None:
        with self.assertRaisesRegex(EnrichmentValidationError, "does not match"):
            validate_enrichment_item(
                enrichment_item(2),
                expected_paper_id="1",
            )

        item = enrichment_item()
        item["limitations"] = [3]
        with self.assertRaisesRegex(EnrichmentValidationError, "every entry"):
            validate_enrichment_item(item)


class OpenAIEnrichmentTests(unittest.TestCase):
    def test_uses_strict_schema_and_retries_transient_failure(self) -> None:
        response_payload = {
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"content": json.dumps(enrichment_item())},
                }
            ]
        }
        requests = []
        attempts = iter(
            [urllib.error.URLError("temporary failure"), FakeResponse(response_payload)]
        )

        def fake_urlopen(request, timeout):
            requests.append(json.loads(request.data.decode("utf-8")))
            result = next(attempts)
            if isinstance(result, Exception):
                raise result
            return result

        sleeps = []
        with mock.patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "test-key", "OPENAI_MAX_ATTEMPTS": "2"},
        ):
            result = run_enrichment.call_openai(
                "prompt",
                urlopen=fake_urlopen,
                sleep=sleeps.append,
            )

        self.assertEqual(result["paper_id"], 1)
        self.assertEqual(len(requests), 2)
        self.assertEqual(sleeps, [1])
        response_format = requests[0]["response_format"]
        self.assertEqual(response_format["type"], "json_schema")
        self.assertTrue(response_format["json_schema"]["strict"])
        self.assertFalse(
            response_format["json_schema"]["schema"]["additionalProperties"]
        )

    def test_rejects_refusal_and_incomplete_response(self) -> None:
        with self.assertRaisesRegex(run_enrichment.EnrichmentError, "refused"):
            run_enrichment.parse_openai_response(
                {
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {"refusal": "cannot process"},
                        }
                    ]
                }
            )
        with self.assertRaisesRegex(run_enrichment.EnrichmentError, "finish_reason"):
            run_enrichment.parse_openai_response(
                {
                    "choices": [
                        {
                            "finish_reason": "length",
                            "message": {"content": "{}"},
                        }
                    ]
                }
            )

    def test_does_not_enrich_without_source_text(self) -> None:
        def unavailable(_url: str) -> str:
            raise urllib.error.URLError("unavailable")

        with self.assertRaisesRegex(run_enrichment.EnrichmentError, "not attempted"):
            run_enrichment.paper_source_text(
                "Unavailable paper",
                "https://arxiv.org/abs/2401.12345",
                fetcher=unavailable,
            )


class ImportEnrichmentTests(unittest.TestCase):
    def test_invalid_batch_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            inbox = root / "papers.csv"
            enrichment_dir = root / "enrichment"
            input_path = root / "input.json"
            write_rows(inbox, [paper_row(1), paper_row(2)])
            original_csv = inbox.read_text(encoding="utf-8")
            invalid = enrichment_item(2)
            invalid.pop("summary")
            input_path.write_text(
                json.dumps([enrichment_item(1), invalid]),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(EnrichmentValidationError, "item 2"):
                import_enrichment.import_enrichment(
                    input_path,
                    inbox=inbox,
                    enrichment_dir=enrichment_dir,
                )

            self.assertEqual(inbox.read_text(encoding="utf-8"), original_csv)
            self.assertFalse(enrichment_dir.exists())

    def test_valid_batch_atomically_updates_files_and_registry(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            inbox = root / "papers.csv"
            enrichment_dir = root / "enrichment"
            input_path = root / "input.json"
            write_rows(inbox, [paper_row(1)])
            input_path.write_text(
                json.dumps([enrichment_item(1)]),
                encoding="utf-8",
            )

            count = import_enrichment.import_enrichment(
                input_path,
                inbox=inbox,
                enrichment_dir=enrichment_dir,
            )

            self.assertEqual(count, 1)
            payload = json.loads((enrichment_dir / "1.json").read_text())
            self.assertEqual(payload["paper_id"], "1")
            with inbox.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[0]["enrichment_status"], "enriched")
            self.assertEqual(list(root.rglob("*.tmp")), [])

    def test_publish_failure_rolls_back_prior_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            inbox = root / "papers.csv"
            enrichment_dir = root / "enrichment"
            enrichment_dir.mkdir()
            input_path = root / "input.json"
            write_rows(inbox, [paper_row(1), paper_row(2)])
            original_csv = inbox.read_text(encoding="utf-8")
            first_path = enrichment_dir / "1.json"
            first_path.write_text('{"old": true}\n', encoding="utf-8")
            input_path.write_text(
                json.dumps([enrichment_item(1), enrichment_item(2)]),
                encoding="utf-8",
            )
            real_atomic_write = import_enrichment.atomic_write_text
            call_count = 0

            def fail_second_write(path: Path, content: str) -> None:
                nonlocal call_count
                call_count += 1
                if call_count == 2:
                    raise OSError("simulated publication failure")
                real_atomic_write(path, content)

            with mock.patch.object(
                import_enrichment,
                "atomic_write_text",
                side_effect=fail_second_write,
            ):
                with self.assertRaisesRegex(OSError, "simulated"):
                    import_enrichment.import_enrichment(
                        input_path,
                        inbox=inbox,
                        enrichment_dir=enrichment_dir,
                    )

            self.assertEqual(first_path.read_text(encoding="utf-8"), '{"old": true}\n')
            self.assertFalse((enrichment_dir / "2.json").exists())
            self.assertEqual(inbox.read_text(encoding="utf-8"), original_csv)


class QueueTests(unittest.TestCase):
    def test_existing_enrichment_file_is_not_queued_again(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            inbox = root / "papers.csv"
            output = root / "queue.json"
            enrichment_dir = root / "enrichment"
            enrichment_dir.mkdir()
            write_rows(inbox, [paper_row(1), paper_row(2)])
            (enrichment_dir / "1.json").write_text("{}", encoding="utf-8")

            with (
                mock.patch.object(export_enrichment_input, "INBOX", inbox),
                mock.patch.object(export_enrichment_input, "OUTPUT", output),
                mock.patch.object(
                    export_enrichment_input,
                    "ENRICHMENT_DIR",
                    enrichment_dir,
                ),
            ):
                export_enrichment_input.main()

            queue = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual([paper["paper_id"] for paper in queue["papers"]], ["2"])


if __name__ == "__main__":
    unittest.main()

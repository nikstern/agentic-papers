#!/usr/bin/env python3

import csv
import io
import json
import os
import stat
import sys
import tempfile
from pathlib import Path

from enrichment_schema import (
    REQUIRED_FIELDS,
    EnrichmentValidationError,
    validate_enrichment_item,
)


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
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


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_rows(path: Path = INBOX) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDNAMES:
            fail("papers.csv header does not match expected schema")
        return list(reader)


def load_items(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        fail("enrichment file must be a JSON array")
    return data


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    target_mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            os.fchmod(handle.fileno(), target_mode)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_path = Path(handle.name)
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def publish_transaction(writes: list[tuple[Path, str]]) -> None:
    originals = {
        path: path.read_text(encoding="utf-8") if path.exists() else None
        for path, _ in writes
    }
    published: list[Path] = []
    try:
        for path, content in writes:
            atomic_write_text(path, content)
            published.append(path)
    except Exception as publish_error:
        rollback_errors = []
        for path in reversed(published):
            try:
                original = originals[path]
                if original is None:
                    path.unlink(missing_ok=True)
                else:
                    atomic_write_text(path, original)
            except Exception as rollback_error:
                rollback_errors.append(f"{path}: {rollback_error}")
        if rollback_errors:
            raise RuntimeError(
                "enrichment import failed and rollback was incomplete: "
                + "; ".join(rollback_errors)
            ) from publish_error
        raise


def import_enrichment(
    input_path: Path,
    *,
    inbox: Path = INBOX,
    enrichment_dir: Path = ENRICHMENT_DIR,
) -> int:
    rows = load_rows(inbox)
    known_ids = {row["paper_id"] for row in rows}
    items = load_items(input_path)
    rows_by_id = {row["paper_id"]: row for row in rows}

    validated_items: list[dict] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        try:
            validated = validate_enrichment_item(item, known_ids=known_ids)
        except EnrichmentValidationError as exc:
            raise EnrichmentValidationError(f"item {index}: {exc}") from exc
        paper_id = validated["paper_id"]
        if paper_id in seen_ids:
            raise EnrichmentValidationError(
                f"item {index}: duplicate paper_id '{paper_id}'"
            )
        seen_ids.add(paper_id)
        validated_items.append(validated)

    writes: list[tuple[Path, str]] = []
    for item in validated_items:
        paper_id = item["paper_id"]
        payload = {field: item[field] for field in REQUIRED_FIELDS}
        writes.append(
            (
                enrichment_dir / f"{paper_id}.json",
                json.dumps(payload, indent=2) + "\n",
            )
        )
        rows_by_id[paper_id]["enrichment_status"] = "enriched"

    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)
    writes.append((inbox, csv_buffer.getvalue()))
    publish_transaction(writes)
    return len(validated_items)


def main() -> None:
    if len(sys.argv) != 2:
        fail(
            "usage: python3 scripts/import_enrichment.py "
            "<path-to-enrichment.json>"
        )

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.exists():
        fail(f"input file not found: {input_path}")

    try:
        imported_count = import_enrichment(input_path)
    except EnrichmentValidationError as exc:
        fail(str(exc))
    print(f"Imported enrichment for {imported_count} papers.")


if __name__ == "__main__":
    main()

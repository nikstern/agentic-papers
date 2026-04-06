#!/usr/bin/env python3

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
LAST_IMPORT = ROOT / "paper_inbox" / "last_import.json"
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
REQUIRED_INPUT_FIELDS = [
    "title",
    "url",
    "year",
    "authors",
    "candidate_topic",
    "paper_type",
]
ALLOWED_TOPICS = {
    "llm-multi-agent-systems",
    "agent-evaluation",
    "agent-harnesses",
    "task-allocation",
    "search-retrieval",
    "central-place-foraging",
    "hallucination-factuality",
    "software-agents",
    "memory-context",
}
ALLOWED_TYPES = {"survey", "benchmark", "system", "position", "application"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def normalize_url(value: str) -> str:
    return value.strip().lower().rstrip("/")


def next_paper_id(rows: list[dict]) -> int:
    if not rows:
        return 1
    return max(int(row["paper_id"]) for row in rows) + 1


def load_candidates(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        fail("candidate file must be a JSON array")
    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            fail(f"candidate {idx}: each item must be an object")
        for field in REQUIRED_INPUT_FIELDS:
            if field not in item or str(item[field]).strip() == "":
                fail(f"candidate {idx}: missing '{field}'")
        if str(item["candidate_topic"]) not in ALLOWED_TOPICS:
            fail(
                f"candidate {idx}: invalid candidate_topic "
                f"'{item['candidate_topic']}'"
            )
        if str(item["paper_type"]) not in ALLOWED_TYPES:
            fail(f"candidate {idx}: invalid paper_type '{item['paper_type']}'")
        year = str(item["year"])
        if not year.isdigit() or len(year) != 4:
            fail(f"candidate {idx}: year must be a 4-digit number")
        url = str(item["url"])
        if not (url.startswith("http://") or url.startswith("https://")):
            fail(f"candidate {idx}: url must start with http:// or https://")
    return data


def main() -> None:
    if len(sys.argv) != 2:
        fail(
            "usage: python3 scripts/import_mcp_candidates.py "
            "<path-to-mcp-candidates.json>"
        )

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.exists():
        fail(f"input file not found: {input_path}")

    with INBOX.open(newline="", encoding="utf-8") as handle:
        existing_rows = list(csv.DictReader(handle))

    existing_titles = {normalize_title(row["title"]) for row in existing_rows}
    existing_urls = {normalize_url(row["url"]) for row in existing_rows}

    imported = 0
    imported_rows: list[dict] = []
    skipped_rows: list[dict] = []
    next_id = next_paper_id(existing_rows)
    for item in load_candidates(input_path):
        title_key = normalize_title(str(item["title"]))
        url_key = normalize_url(str(item["url"]))
        if title_key in existing_titles or url_key in existing_urls:
            skipped_rows.append(
                {
                    "title": str(item["title"]).strip(),
                    "url": str(item["url"]).strip(),
                    "reason": "duplicate",
                }
            )
            continue
        row = {
            "paper_id": str(next_id),
            "title": str(item["title"]).strip(),
            "url": str(item["url"]).strip(),
            "year": str(item["year"]).strip(),
            "authors": str(item["authors"]).strip(),
            "candidate_topic": str(item["candidate_topic"]).strip(),
            "source": "alphaxiv-mcp",
            "paper_type": str(item["paper_type"]).strip(),
            "status": "candidate",
            "enrichment_status": "pending",
        }
        existing_rows.append(
            row
        )
        imported_rows.append(
            {
                "paper_id": row["paper_id"],
                "title": row["title"],
                "url": row["url"],
                "paper_type": row["paper_type"],
                "candidate_topic": row["candidate_topic"],
            }
        )
        existing_titles.add(title_key)
        existing_urls.add(url_key)
        next_id += 1
        imported += 1

    with INBOX.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(existing_rows)

    LAST_IMPORT.write_text(
        json.dumps(
            {
                "source_file": str(input_path),
                "imported_count": imported,
                "imported": imported_rows,
                "skipped": skipped_rows,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Imported {imported} new MCP candidates.")
    for row in imported_rows:
        print(f"{row['paper_id']}: {row['title']}")


if __name__ == "__main__":
    main()

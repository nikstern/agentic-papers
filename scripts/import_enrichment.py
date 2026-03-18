#!/usr/bin/env python3

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
REQUIRED_FIELDS = [
    "paper_id",
    "summary",
    "why_it_matters",
    "method_setup",
    "key_claims",
    "limitations",
    "evaluates",
    "builds_on_unresolved",
    "compares_to_unresolved",
]
LIST_FIELDS = {
    "key_claims",
    "limitations",
    "evaluates",
    "builds_on_unresolved",
    "compares_to_unresolved",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_rows() -> list[dict]:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_items(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        fail("enrichment file must be a JSON array")
    return data


def validate_item(index: int, item: dict, known_ids: set[str]) -> None:
    if not isinstance(item, dict):
        fail(f"item {index}: each enrichment item must be an object")
    for field in REQUIRED_FIELDS:
        if field not in item:
            fail(f"item {index}: missing '{field}'")
    paper_id = str(item["paper_id"])
    if not paper_id.isdigit():
        fail(f"item {index}: paper_id must be numeric")
    if paper_id not in known_ids:
        fail(f"item {index}: unknown paper_id '{paper_id}'")
    for field in LIST_FIELDS:
        if not isinstance(item[field], list):
            fail(f"item {index}: '{field}' must be a list")
    for field in ("summary", "why_it_matters", "method_setup"):
        if not isinstance(item[field], str):
            fail(f"item {index}: '{field}' must be a string")


def main() -> None:
    if len(sys.argv) != 2:
        fail(
            "usage: python3 scripts/import_enrichment.py "
            "<path-to-enrichment.json>"
        )

    input_path = Path(sys.argv[1]).resolve()
    if not input_path.exists():
        fail(f"input file not found: {input_path}")

    rows = load_rows()
    known_ids = {row["paper_id"] for row in rows}
    items = load_items(input_path)

    ENRICHMENT_DIR.mkdir(parents=True, exist_ok=True)
    for index, item in enumerate(items, start=1):
        validate_item(index, item, known_ids)
        paper_id = str(item["paper_id"])
        payload = {"paper_id": paper_id}
        for field in REQUIRED_FIELDS[1:]:
            payload[field] = item[field]
        (ENRICHMENT_DIR / f"{paper_id}.json").write_text(
            json.dumps(payload, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"Imported enrichment for {len(items)} papers.")


if __name__ == "__main__":
    main()

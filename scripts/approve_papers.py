#!/usr/bin/env python3

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
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
]
APPROVABLE = {"candidate"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    ids = sys.argv[1:]
    if not ids:
        fail("usage: python3 scripts/approve_papers.py <paper_id> [<paper_id> ...]")
    invalid = [paper_id for paper_id in ids if not paper_id.isdigit()]
    if invalid:
        fail(f"paper_id values must be numeric: {', '.join(invalid)}")

    with INBOX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    requested = set(ids)
    found: set[str] = set()
    approved_count = 0
    for row in rows:
        if row["paper_id"] not in requested:
            continue
        found.add(row["paper_id"])
        if row["status"] in APPROVABLE:
            row["status"] = "approved"
            approved_count += 1

    missing = requested - found
    if missing:
        fail(f"paper_id not found: {', '.join(sorted(missing))}")

    with INBOX.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Approved {approved_count} papers.")


if __name__ == "__main__":
    main()

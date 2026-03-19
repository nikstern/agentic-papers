#!/usr/bin/env python3

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
OLD_FIELDNAMES = [
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
NEW_FIELDNAMES = OLD_FIELDNAMES + ["enrichment_status"]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames == NEW_FIELDNAMES:
            print("papers.csv already includes enrichment_status.")
            return
        if reader.fieldnames != OLD_FIELDNAMES:
            fail("papers.csv header does not match expected pre-migration schema")
        rows = list(reader)

    enriched_ids = {
        path.stem for path in ENRICHMENT_DIR.glob("*.json") if path.stem.isdigit()
    }
    for row in rows:
        row["enrichment_status"] = (
            "enriched" if row["paper_id"] in enriched_ids else "pending"
        )

    with INBOX.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=NEW_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Migrated {len(rows)} papers to include enrichment_status.")


if __name__ == "__main__":
    main()

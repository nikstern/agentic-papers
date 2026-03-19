#!/usr/bin/env python3

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
OUTPUT = ROOT / "paper_inbox" / "approved_for_enrichment.json"
ACTIVE_FOR_ENRICHMENT = {"ingested", "skimmed", "deep_read", "cited"}
PENDING_ENRICHMENT = "pending"
QUERY_SET = [
    "What is the main contribution of this paper in 1-2 sentences?",
    "Which paper type best fits this paper: survey, benchmark, system, position, or application?",
    "What evaluation setting, benchmark, or task suite does this paper introduce or use?",
    "What prior systems, methods, or baselines does it explicitly compare against?",
    "What prior work does it explicitly build on?",
    "What limitations do the authors describe or acknowledge?",
]


def main() -> None:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    payload = {
        "queries": QUERY_SET,
        "papers": [
            {
                "paper_id": row["paper_id"],
                "title": row["title"],
                "url": row["url"],
                "status": row["status"],
            }
            for row in rows
            if row["status"] in ACTIVE_FOR_ENRICHMENT
            and row["enrichment_status"] == PENDING_ENRICHMENT
        ],
    }

    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote enrichment input for {len(payload['papers'])} papers to {OUTPUT}.")


if __name__ == "__main__":
    main()

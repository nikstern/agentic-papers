#!/usr/bin/env python3

import argparse
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "paper_inbox" / "papers.csv"
ENRICHMENT_DIR = ROOT / "paper_inbox" / "enrichment"
NOTES_DIR = ROOT / "paper_notes"
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
ACTIVE_READING_STATUSES = {"ingested", "skimmed", "deep_read", "approved"}
TOPIC_WEIGHTS = {
    "memory-context": 4.0,
    "llm-multi-agent-systems": 3.5,
    "agent-evaluation": 3.0,
    "task-allocation": 2.5,
    "search-retrieval": 2.5,
    "central-place-foraging": 2.5,
    "hallucination-factuality": 2.5,
    "software-agents": 2.0,
    "agent-harnesses": 2.0,
}
TYPE_WEIGHTS = {
    "survey": 3.0,
    "position": 2.5,
    "benchmark": 2.5,
    "system": 2.0,
    "application": 1.5,
}
RELATION_KEYS = ("builds_on_unresolved", "compares_to_unresolved")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def normalize_title(value: str) -> str:
    chars = []
    for char in value.lower():
        if char.isalnum() or char.isspace():
            chars.append(char)
        else:
            chars.append(" ")
    return " ".join("".join(chars).split())


def slug_title(title: str) -> str:
    cleaned = []
    for char in title:
        if char.isalnum() or char.isspace() or char in {"_", "-"}:
            cleaned.append(char)
    normalized = " ".join("".join(cleaned).split())
    words = normalized.split()
    short = "-".join(words[:8]).strip("-")
    return short or "Untitled"


def note_name(year: str, title: str) -> str:
    return f"{year}-{slug_title(title)}.md"


def load_rows() -> list[dict[str, str]]:
    with INBOX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDNAMES:
            fail("papers.csv header does not match expected schema")
        return list(reader)


def load_enrichment(paper_id: str) -> dict:
    path = ENRICHMENT_DIR / f"{paper_id}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}

    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def note_overrides(row: dict[str, str]) -> dict[str, str]:
    path = NOTES_DIR / note_name(row["year"], row["title"])
    return parse_frontmatter(path)


def effective_status(row: dict[str, str], overrides: dict[str, str]) -> str:
    return overrides.get("status", row["status"])


def priority_bonus(value: str) -> float:
    normalized = value.strip().lower()
    if normalized == "":
        return 0.0
    named = {
        "low": 0.5,
        "medium": 1.0,
        "med": 1.0,
        "high": 2.0,
        "urgent": 3.0,
    }
    if normalized in named:
        return named[normalized]
    try:
        return max(0.0, min(float(normalized), 3.0))
    except ValueError:
        return 0.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rank papers by reading importance."
    )
    parser.add_argument("--top", type=int, default=10, help="number of papers to print")
    parser.add_argument(
        "--status",
        action="append",
        dest="statuses",
        help="include only these statuses; defaults to active reading statuses",
    )
    parser.add_argument(
        "--topic-weight-file",
        help="optional JSON file overriding topic weights",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print machine-readable JSON",
    )
    return parser.parse_args()


def load_topic_weights(path: str | None) -> dict[str, float]:
    weights = dict(TOPIC_WEIGHTS)
    if not path:
        return weights
    file_path = Path(path).expanduser().resolve()
    data = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("topic weight file must be a JSON object")
    for key, value in data.items():
        weights[str(key)] = float(value)
    return weights


def relation_centrality(rows: list[dict[str, str]]) -> dict[str, int]:
    title_index = {normalize_title(row["title"]): row["paper_id"] for row in rows}
    inbound_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        enrichment = load_enrichment(row["paper_id"])
        linked_ids: set[str] = set()
        for key in RELATION_KEYS:
            for value in enrichment.get(key, []):
                target_id = title_index.get(normalize_title(str(value)))
                if target_id and target_id != row["paper_id"]:
                    linked_ids.add(target_id)
        for target_id in linked_ids:
            inbound_counts[target_id] += 1
    return dict(inbound_counts)


def foundation_candidates(rows: list[dict[str, str]]) -> set[str]:
    by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_topic[row["candidate_topic"]].append(row)

    foundations: set[str] = set()
    for topic_rows in by_topic.values():
        earliest_year = min(int(row["year"]) for row in topic_rows)
        for row in topic_rows:
            year = int(row["year"])
            if year > earliest_year + 1:
                continue
            if row["paper_type"] in {"survey", "position", "benchmark", "system"}:
                foundations.add(row["paper_id"])
    return foundations


def compute_scores(
    rows: list[dict[str, str]],
    statuses: set[str],
    topic_weights: dict[str, float],
) -> list[dict]:
    effective_rows: list[dict[str, str]] = []
    for row in rows:
        effective_row = dict(row)
        overrides = note_overrides(row)
        effective_row["status"] = effective_status(row, overrides)
        effective_row["priority"] = overrides.get("priority", "0")
        effective_row["last_read"] = overrides.get("last_read", "")
        effective_rows.append(effective_row)

    candidates = [row for row in effective_rows if row["status"] in statuses]
    if not candidates:
        return []

    topic_counts = Counter(row["candidate_topic"] for row in candidates)
    centrality_counts = relation_centrality(effective_rows)
    foundation_ids = foundation_candidates(effective_rows)

    years = [int(row["year"]) for row in candidates]
    min_year = min(years)
    max_year = max(years)
    year_span = max(max_year - min_year, 1)
    max_centrality = max(centrality_counts.values(), default=0)

    ranked: list[dict] = []
    for row in candidates:
        paper_id = row["paper_id"]
        topic = row["candidate_topic"]
        year = int(row["year"])
        topic_score = topic_weights.get(topic, 1.0)
        type_score = TYPE_WEIGHTS.get(row["paper_type"], 1.0)
        raw_centrality = centrality_counts.get(paper_id, 0)
        centrality_score = (
            3.0 * raw_centrality / max_centrality if max_centrality else 0.0
        )
        gap_score = 2.0 / math.sqrt(topic_counts[topic])
        recency_score = 1.5 * (year - min_year) / year_span
        foundation_score = 1.5 if paper_id in foundation_ids else 0.0
        priority_score = priority_bonus(row.get("priority", "0"))
        score = (
            topic_score
            + type_score
            + centrality_score
            + gap_score
            + recency_score
            + foundation_score
            + priority_score
        )
        ranked.append(
            {
                "paper_id": paper_id,
                "title": row["title"],
                "year": row["year"],
                "candidate_topic": topic,
                "paper_type": row["paper_type"],
                "status": row["status"],
                "score": round(score, 3),
                "components": {
                    "topic_fit": round(topic_score, 3),
                    "type_value": round(type_score, 3),
                    "centrality": round(centrality_score, 3),
                    "gap_bonus": round(gap_score, 3),
                    "recency": round(recency_score, 3),
                    "foundation_bonus": round(foundation_score, 3),
                    "priority": round(priority_score, 3),
                },
                "raw_centrality": raw_centrality,
                "url": row["url"],
                "authors": row["authors"],
                "priority": row.get("priority", "0"),
                "last_read": row.get("last_read", ""),
            }
        )

    ranked.sort(
        key=lambda item: (
            -item["score"],
            -item["components"]["centrality"],
            -int(item["year"]),
            item["title"].lower(),
        )
    )
    return ranked


def print_human(ranked: list[dict], limit: int) -> None:
    for index, item in enumerate(ranked[:limit], start=1):
        components = item["components"]
        print(f"{index}. [{item['paper_id']}] {item['title']} ({item['year']})")
        print(
            "   "
            f"score={item['score']} "
            f"topic={item['candidate_topic']} "
            f"type={item['paper_type']} "
            f"status={item['status']}"
        )
        print(
            "   "
            f"topic_fit={components['topic_fit']} "
            f"type_value={components['type_value']} "
            f"centrality={components['centrality']} "
            f"gap_bonus={components['gap_bonus']} "
            f"recency={components['recency']} "
            f"foundation_bonus={components['foundation_bonus']} "
            f"priority={components['priority']}"
        )
        print(f"   {item['url']}")


def main() -> None:
    args = parse_args()
    rows = load_rows()
    statuses = set(args.statuses or ACTIVE_READING_STATUSES)
    topic_weights = load_topic_weights(args.topic_weight_file)
    ranked = compute_scores(rows, statuses, topic_weights)
    if args.json:
        print(json.dumps(ranked[: args.top], indent=2))
        return
    print_human(ranked, args.top)


if __name__ == "__main__":
    main()

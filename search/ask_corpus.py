#!/usr/bin/env python3

from __future__ import annotations

import argparse
from collections import defaultdict
import re

from qdrant_client.models import FieldCondition, Filter, MatchValue

from common import (
    get_client,
    get_collection_name,
    get_embedder,
    load_paper_records,
    normalize_text,
    record_aliases,
)


RELATION_FIELDS = (
    "evaluates",
    "builds_on",
    "compares_to",
    "builds_on_unresolved",
    "compares_to_unresolved",
)
RELATION_WEIGHTS = {
    "compares_to": 3.0,
    "builds_on": 2.0,
    "compares_to_unresolved": 1.75,
    "builds_on_unresolved": 1.5,
    "evaluates": 1.25,
}
MODE_FIELDS = {
    "comparison": {"compares_to", "compares_to_unresolved"},
    "builds_on": {"builds_on", "builds_on_unresolved"},
    "evaluation": {"compares_to", "compares_to_unresolved", "evaluates"},
    "lookup": set(RELATION_FIELDS),
}


def detect_intent(question: str) -> str:
    lowered = question.strip().lower()

    critique_markers = (
        "critique",
        "criticize",
        "criticism",
        "criticisms",
        "limitation",
        "limitations",
        "weakness",
        "weaknesses",
        "failure",
        "failures",
        "risk",
        "risks",
        "problem",
        "problems",
    )
    comparison_markers = (
        "compare",
        "comparison",
        "versus",
        "vs",
        "better than",
        "worse than",
        "difference",
        "different",
    )
    evaluation_markers = (
        "evaluate",
        "evaluates",
        "evaluated",
        "evaluation",
        "benchmark",
        "benchmarks",
        "tested",
        "test",
        "outperform",
        "baseline",
        "baselines",
    )
    lookup_markers = (
        "what paper",
        "which paper",
        "who",
        "when",
        "where",
        "what is",
        "which papers mention",
        "which papers discuss",
    )

    if any(marker in lowered for marker in critique_markers):
        return "critique"
    if any(marker in lowered for marker in comparison_markers):
        return "comparison"
    if any(marker in lowered for marker in evaluation_markers):
        return "evaluation"
    if any(marker in lowered for marker in lookup_markers):
        return "lookup"
    return "survey"


def discussion_angles(intent: str) -> list[str]:
    if intent == "critique":
        return [
            "Are the main weaknesses empirical, architectural, or scope-related?",
            "Which limitations recur across multiple papers instead of appearing in only one note?",
            "Do any retrieved papers directly challenge the assumptions behind the top result?",
        ]
    if intent == "comparison":
        return [
            "What is the actual disagreement between the top papers rather than their surface-level topic overlap?",
            "Which differences are about memory architecture, which are about evaluation setting, and which are about task scope?",
            "If you had to choose one approach, what evidence in these notes would make that choice defensible?",
        ]
    if intent == "evaluation":
        return [
            "Which retrieved papers present direct benchmark evidence versus conceptual or survey-level claims?",
            "What baselines, tasks, or metrics are actually used to support the strongest result here?",
            "Where do the evaluations look narrow enough that you should be cautious about generalizing them?",
        ]
    if intent == "lookup":
        return [
            "Which top result answers the question directly versus only citing or building on the named concept?",
            "Do the retrieved notes contain an explicit relation such as `evaluates`, `compares_to`, or `builds_on`?",
            "Which nearby papers would you open next if you wanted evidence rather than just mention-level linkage?",
        ]
    return [
        "Which retrieved papers are describing mechanisms versus presenting evidence?",
        "Where do the strongest limitations or failure modes show up across the top hits?",
        "Which papers seem closest to your question semantically but still miss part of it?",
    ]


def relation_mode(question: str) -> str | None:
    lowered = question.lower()
    if any(token in lowered for token in ("compares to", "compare to", "compared to", "versus", " vs ")):
        return "comparison"
    if any(token in lowered for token in ("build on", "builds on", "built on", "build upon", "extends", "based on")):
        return "builds_on"
    if any(token in lowered for token in ("evaluates", "evaluate", "evaluated", "benchmark", "benchmarks", "tested")):
        return "evaluation"
    if any(token in lowered for token in ("mentions", "mention", "discusses", "discuss", "what paper", "which paper")):
        return "lookup"
    return None


def alias_index(records: list) -> dict[str, list]:
    index: dict[str, list] = defaultdict(list)
    for record in records:
        for alias in record_aliases(record):
            index[normalize_text(alias)].append(record)
    return index


def resolve_target_records(question: str, records: list) -> list:
    normalized_question = normalize_text(question)
    matches: list = []
    for alias, matched_records in alias_index(records).items():
        if not alias:
            continue
        pattern = rf"(^| )({re.escape(alias)})( |$)"
        if re.search(pattern, normalized_question):
            for record in matched_records:
                if record.paper_id not in {item.paper_id for item in matches}:
                    matches.append(record)
    matches.sort(key=lambda item: len(item.title), reverse=True)
    return matches


def normalize_relation_value(value: str) -> str:
    cleaned = str(value).strip()
    link_match = re.fullmatch(r"\[\[(.+)\]\]", cleaned)
    if link_match:
        cleaned = link_match.group(1)
    return normalize_text(cleaned)


def relation_candidates(question: str, records: list) -> list[dict]:
    mode = relation_mode(question)
    if mode is None:
        return []

    targets = resolve_target_records(question, records)
    if not targets:
        return []

    target_aliases: set[str] = set()
    for target in targets:
        target_aliases.update(normalize_text(alias) for alias in record_aliases(target))

    scored: dict[int, dict] = {}
    for record in records:
        for field in RELATION_FIELDS:
            allowed_fields = MODE_FIELDS.get(mode, set(RELATION_FIELDS))
            if field not in allowed_fields:
                continue
            values = record.frontmatter.get(field, []) or []
            if not isinstance(values, list):
                continue
            for value in values:
                normalized_value = normalize_relation_value(str(value))
                if normalized_value not in target_aliases:
                    continue

                score = RELATION_WEIGHTS.get(field, 1.0)
                if mode == "comparison" and field == "compares_to":
                    score += 1.0
                elif mode == "builds_on" and field == "builds_on":
                    score += 1.0
                elif mode == "evaluation" and field == "compares_to":
                    score += 0.75
                elif mode == "lookup":
                    score += 0.25

                existing = scored.get(record.paper_id)
                hit = {
                    "paper_id": record.paper_id,
                    "title": record.title,
                    "year": record.year,
                    "topic": record.candidate_topic,
                    "paper_type": record.paper_type,
                    "path": record.path,
                    "url": record.url,
                    "best_score": score,
                    "relation_hits": [
                        {
                            "field": field,
                            "value": str(value),
                        }
                    ],
                }
                if existing is None:
                    scored[record.paper_id] = hit
                else:
                    existing["best_score"] = max(existing["best_score"], score)
                    existing["relation_hits"].append(hit["relation_hits"][0])

    ordered = sorted(
        scored.values(),
        key=lambda item: (item["best_score"], item["year"]),
        reverse=True,
    )
    return ordered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask a natural-language question against the indexed paper vault."
    )
    parser.add_argument("question", help="research question to probe")
    parser.add_argument("--topic", help="optional candidate_topic filter")
    parser.add_argument("--type", dest="paper_type", help="optional paper_type filter")
    parser.add_argument("--year", type=int, help="optional exact year filter")
    parser.add_argument("--limit", type=int, default=10, help="number of section hits")
    parser.add_argument(
        "--papers",
        type=int,
        default=4,
        help="maximum number of papers to summarize",
    )
    return parser.parse_args()


def build_filter(args: argparse.Namespace) -> Filter | None:
    clauses = []
    if args.topic:
        clauses.append(
            FieldCondition(key="candidate_topic", match=MatchValue(value=args.topic))
        )
    if args.paper_type:
        clauses.append(
            FieldCondition(key="paper_type", match=MatchValue(value=args.paper_type))
        )
    if args.year is not None:
        clauses.append(FieldCondition(key="year", match=MatchValue(value=args.year)))
    if not clauses:
        return None
    return Filter(must=clauses)


def shorten(text: str, limit: int = 220) -> str:
    compact = " ".join(text.split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


def label_for_section(section: str) -> str:
    labels = {
        "summary": "summary",
        "why_it_matters": "importance",
        "method_setup": "setup",
        "key_claims": "claims",
        "limitations": "limitations",
        "full_context": "context",
    }
    return labels.get(section, section)


def main() -> None:
    args = parse_args()
    intent = detect_intent(args.question)
    records = load_paper_records()
    relation_results = relation_candidates(args.question, records)
    client = get_client()
    embedder = get_embedder()
    collection = get_collection_name()
    query_vector = embedder.embed_query(args.question)

    results = client.query_points(
        collection_name=collection,
        query=query_vector,
        query_filter=build_filter(args),
        limit=args.limit,
        with_payload=True,
    ).points

    if not results:
        print("No results.")
        return

    grouped: dict[int, dict] = {}
    paper_order: list[int] = []
    section_hits: dict[int, list[dict]] = defaultdict(list)

    for item in relation_results:
        grouped[item["paper_id"]] = dict(item)
        paper_order.append(item["paper_id"])
        relation_lines = [
            {
                "score": item["best_score"],
                "section": "relation_match",
                "text": f"{hit['field']}: {hit['value']}",
            }
            for hit in item["relation_hits"]
        ]
        section_hits[item["paper_id"]].extend(relation_lines)

    for point in results:
        payload = point.payload
        paper_id = int(payload["paper_id"])
        if paper_id not in grouped:
            grouped[paper_id] = {
                "paper_id": paper_id,
                "title": payload["title"],
                "year": payload["year"],
                "topic": payload["candidate_topic"],
                "paper_type": payload["paper_type"],
                "path": payload["path"],
                "url": payload["url"],
                "best_score": point.score,
            }
            paper_order.append(paper_id)
        else:
            grouped[paper_id]["best_score"] = max(grouped[paper_id]["best_score"], point.score)

        section_hits[paper_id].append(
            {
                "score": point.score,
                "section": payload["section"],
                "text": payload["text"],
            }
        )

    deduped_order: list[int] = []
    seen_ids: set[int] = set()
    for paper_id in paper_order:
        if paper_id in seen_ids:
            continue
        seen_ids.add(paper_id)
        deduped_order.append(paper_id)

    deduped_order.sort(key=lambda paper_id: grouped[paper_id]["best_score"], reverse=True)
    selected = deduped_order[: args.papers]

    print(f"Question: {args.question}\n")
    print("Relevant papers:\n")
    for index, paper_id in enumerate(selected, start=1):
        paper = grouped[paper_id]
        print(
            f"{index}. [{paper['paper_id']}] {paper['title']} "
            f"({paper['year']}) score={paper['best_score']:.4f}"
        )
        print(f"   topic={paper['topic']} type={paper['paper_type']}")
        print(f"   path={paper['path']}")
        print(f"   url={paper['url']}")

        hits = sorted(section_hits[paper_id], key=lambda hit: hit["score"], reverse=True)
        seen_sections: set[str] = set()
        printed = 0
        for hit in hits:
            section = hit["section"]
            if section == "full_context" or section in seen_sections:
                continue
            seen_sections.add(section)
            if section == "relation_match":
                print(f"   - relation: {hit['text']}")
                printed += 1
                if printed >= 3:
                    break
                continue
            print(
                f"   - {label_for_section(section)}: {shorten(hit['text'])}"
            )
            printed += 1
            if printed >= 3:
                break
        print()

    print(f"Question type: {intent}\n")
    print("Discussion angles:\n")
    for angle in discussion_angles(intent):
        print(f"- {angle}")


if __name__ == "__main__":
    main()

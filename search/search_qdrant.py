#!/usr/bin/env python3

from __future__ import annotations

import argparse

from qdrant_client.models import FieldCondition, Filter, MatchValue

from common import get_client, get_collection_name, get_embedder


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search indexed paper sections in Qdrant.")
    parser.add_argument("query", help="natural-language query")
    parser.add_argument("--topic", help="filter by candidate_topic")
    parser.add_argument("--type", dest="paper_type", help="filter by paper_type")
    parser.add_argument("--year", type=int, help="filter by exact publication year")
    parser.add_argument("--section", help="filter by section name")
    parser.add_argument("--limit", type=int, default=8, help="number of results")
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
    if args.section:
        clauses.append(FieldCondition(key="section", match=MatchValue(value=args.section)))
    if not clauses:
        return None
    return Filter(must=clauses)


def main() -> None:
    args = parse_args()
    client = get_client()
    embedder = get_embedder()
    collection = get_collection_name()
    query_vector = embedder.embed_query(args.query)

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

    for index, point in enumerate(results, start=1):
        payload = point.payload
        print(
            f"{index}. [{payload['paper_id']}] {payload['title']} "
            f"({payload['year']}) score={point.score:.4f}"
        )
        print(
            f"   topic={payload['candidate_topic']} type={payload['paper_type']} "
            f"section={payload['section']}"
        )
        print(f"   path={payload['path']}")
        text = " ".join(str(payload["text"]).split())
        snippet = text[:260] + ("..." if len(text) > 260 else "")
        print(f"   {snippet}")
        print()


if __name__ == "__main__":
    main()

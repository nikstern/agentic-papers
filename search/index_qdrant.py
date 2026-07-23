#!/usr/bin/env python3

from __future__ import annotations

import time
import sys

from qdrant_client.models import (
    CreateAlias,
    CreateAliasOperation,
    DeleteAlias,
    DeleteAliasOperation,
    Distance,
    PointStruct,
    VectorParams,
)

from common import (
    get_backend_mode,
    get_collection_name,
    get_embedder,
    get_model_name,
    iter_sections,
    load_rows,
    require_client,
)


def alias_target(client, alias_name: str) -> str | None:
    for alias in client.get_aliases().aliases:
        if alias.alias_name == alias_name:
            return alias.collection_name
    return None


def create_collection(client, collection_name: str, vector_size: int) -> None:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )


def validate_collection(client, collection_name: str, expected_count: int) -> None:
    actual_count = client.count(collection_name=collection_name, exact=True).count
    if actual_count != expected_count:
        raise RuntimeError(
            f"Qdrant index validation failed for '{collection_name}': "
            f"expected {expected_count} points, found {actual_count}"
        )


def publish_server_collection(
    client,
    alias_name: str,
    vector_size: int,
    points: list[PointStruct],
    *,
    build_id: str | None = None,
) -> str:
    suffix = build_id or str(time.time_ns())
    staging = f"{alias_name}__build_{suffix}"
    previous_target = alias_target(client, alias_name)

    if previous_target is None and client.collection_exists(alias_name):
        raise RuntimeError(
            f"Cannot atomically publish alias '{alias_name}' because a physical "
            "collection already uses that name. The existing collection was "
            "left untouched. Delete it explicitly before reindexing, or set "
            "QDRANT_COLLECTION to a new alias name."
        )

    if client.collection_exists(staging):
        client.delete_collection(staging)

    create_collection(client, staging, vector_size)
    try:
        client.upsert(collection_name=staging, points=points)
        validate_collection(client, staging, len(points))

        operations = []
        if previous_target is not None:
            operations.append(
                DeleteAliasOperation(
                    delete_alias=DeleteAlias(alias_name=alias_name)
                )
            )
        operations.append(
            CreateAliasOperation(
                create_alias=CreateAlias(
                    collection_name=staging,
                    alias_name=alias_name,
                )
            )
        )
        client.update_collection_aliases(operations)
    except Exception:
        # If the server committed the alias update but the response was lost,
        # retaining the staging collection preserves the now-live alias.
        try:
            published_despite_error = alias_target(client, alias_name) == staging
            if not published_despite_error and client.collection_exists(staging):
                client.delete_collection(staging)
        except Exception:
            pass
        raise

    if previous_target and previous_target != staging:
        client.delete_collection(previous_target)
    return staging


def publish_embedded_collection(
    client,
    collection_name: str,
    vector_size: int,
    points: list[PointStruct],
) -> str:
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
    create_collection(client, collection_name, vector_size)
    client.upsert(collection_name=collection_name, points=points)
    validate_collection(client, collection_name, len(points))
    return collection_name


def build_points(sections, vectors) -> list[PointStruct]:
    points = []
    for section, vector in zip(sections, vectors, strict=True):
        payload = {
            "paper_id": section.paper_id,
            "title": section.title,
            "candidate_topic": section.candidate_topic,
            "paper_type": section.paper_type,
            "year": section.year,
            "status": section.status,
            "enrichment_status": section.enrichment_status,
            "authors": section.authors,
            "source": section.source,
            "url": section.url,
            "section": section.section,
            "path": section.path,
            "text": section.text,
            "model": get_model_name(),
        }
        points.append(
            PointStruct(id=section.point_id, vector=vector.tolist(), payload=payload)
        )
    return points


def main() -> None:
    client = require_client()
    embedder = get_embedder()
    collection = get_collection_name()
    vector_size = next(embedder.embed(["dimension probe"])).shape[0]

    rows = load_rows()
    sections = list(iter_sections(rows))
    texts = [section.text for section in sections]
    vectors = list(embedder.embed(texts))
    points = build_points(sections, vectors)

    if get_backend_mode() == "server":
        physical_collection = publish_server_collection(
            client,
            collection,
            vector_size,
            points,
        )
    else:
        physical_collection = publish_embedded_collection(
            client,
            collection,
            vector_size,
            points,
        )
    print(
        f"Indexed {len(points)} sections from {len(rows)} papers into "
        f"'{collection}' ({physical_collection})."
    )


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

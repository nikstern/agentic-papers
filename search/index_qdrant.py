#!/usr/bin/env python3

from __future__ import annotations

from qdrant_client.models import Distance, PointStruct, VectorParams

from common import get_client, get_collection_name, get_embedder, get_model_name, iter_sections, load_rows


def main() -> None:
    client = get_client()
    embedder = get_embedder()
    collection = get_collection_name()

    rows = load_rows()
    sections = list(iter_sections(rows))
    texts = [section.text for section in sections]
    vector_size = len(embedder.embed_query("dimension probe"))
    vectors = embedder.embed_documents(texts)
    if any(len(vector) != vector_size for vector in vectors):
        raise RuntimeError(
            "Ollama returned document embeddings that do not match the query "
            f"embedding dimension ({vector_size})"
        )

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
        points.append(PointStruct(id=section.point_id, vector=vector, payload=payload))

    if client.collection_exists(collection):
        client.delete_collection(collection)
    client.create_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )
    client.upsert(collection_name=collection, points=points)
    print(
        f"Indexed {len(points)} sections from {len(rows)} papers into '{collection}'."
    )


if __name__ == "__main__":
    main()

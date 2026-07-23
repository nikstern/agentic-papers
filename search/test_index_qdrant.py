from __future__ import annotations

from types import SimpleNamespace
import unittest
from unittest import mock

import index_qdrant


class RecordingClient:
    def __init__(self) -> None:
        self.actions: list[str] = []

    def collection_exists(self, collection: str) -> bool:
        self.actions.append("collection_exists")
        return True

    def delete_collection(self, collection: str) -> None:
        self.actions.append("delete_collection")

    def create_collection(self, *, collection_name: str, vectors_config) -> None:
        self.actions.append("create_collection")

    def upsert(self, *, collection_name: str, points) -> None:
        self.actions.append("upsert")


class FailingEmbedder:
    def embed_query(self, text: str) -> list[float]:
        return [1.0, 0.0]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        raise RuntimeError("simulated Ollama failure")


class IndexReplacementTests(unittest.TestCase):
    def test_embedding_failure_preserves_existing_collection(self) -> None:
        client = RecordingClient()
        section = SimpleNamespace(text="paper text")

        with (
            mock.patch.object(index_qdrant, "get_client", return_value=client),
            mock.patch.object(
                index_qdrant,
                "get_embedder",
                return_value=FailingEmbedder(),
            ),
            mock.patch.object(
                index_qdrant,
                "get_collection_name",
                return_value="papers",
            ),
            mock.patch.object(index_qdrant, "load_rows", return_value=[{}]),
            mock.patch.object(
                index_qdrant,
                "iter_sections",
                return_value=iter([section]),
            ),
        ):
            with self.assertRaisesRegex(RuntimeError, "simulated Ollama failure"):
                index_qdrant.main()

        self.assertEqual(client.actions, [])


if __name__ == "__main__":
    unittest.main()

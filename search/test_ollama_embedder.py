from __future__ import annotations

import json
import unittest
import urllib.error

from ollama_embedder import OllamaEmbedder, OllamaEmbeddingError


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


class FakeOpener:
    def __init__(self) -> None:
        self.batches: list[dict] = []

    def open(self, request, timeout):
        payload = json.loads(request.data.decode("utf-8"))
        self.batches.append(payload)
        embeddings = [
            [float(len(text)), float(index)]
            for index, text in enumerate(payload["input"])
        ]
        return FakeResponse({"model": payload["model"], "embeddings": embeddings})


class FailingOpener:
    def open(self, request, timeout):
        raise urllib.error.URLError("connection refused")


class OllamaEmbedderTests(unittest.TestCase):
    def test_batches_documents_and_preserves_order(self) -> None:
        embedder = OllamaEmbedder(
            base_url="http://127.0.0.1:11434",
            model="test-model",
            batch_size=2,
        )
        opener = FakeOpener()
        embedder._opener = opener

        vectors = embedder.embed_documents(["a", "bb", "ccc", "dddd", "eeeee"])

        self.assertEqual([len(batch["input"]) for batch in opener.batches], [2, 2, 1])
        self.assertEqual([vector[0] for vector in vectors], [1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertTrue(all(batch["truncate"] is False for batch in opener.batches))

    def test_embeds_one_query(self) -> None:
        embedder = OllamaEmbedder(
            base_url="http://localhost:11434",
            model="test-model",
        )
        opener = FakeOpener()
        embedder._opener = opener

        self.assertEqual(embedder.embed_query("question"), [8.0, 0.0])

    def test_rejects_remote_endpoint(self) -> None:
        with self.assertRaisesRegex(ValueError, "loopback"):
            OllamaEmbedder(base_url="http://example.com", model="test-model")

    def test_reports_unavailable_service(self) -> None:
        embedder = OllamaEmbedder(
            base_url="http://127.0.0.1:11434",
            model="test-model",
        )
        embedder._opener = FailingOpener()

        with self.assertRaisesRegex(OllamaEmbeddingError, "start the local service"):
            embedder.embed_query("question")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import socket
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_OLLAMA_BASE_URL = "http://127.0.0.1:11434"
DEFAULT_OLLAMA_BATCH_SIZE = 32
DEFAULT_OLLAMA_TIMEOUT = 30.0


class OllamaEmbeddingError(RuntimeError):
    """Raised when the local Ollama embedding provider cannot serve a request."""


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class OllamaEmbedder:
    """Minimal loopback-only client for Ollama's native embedding API."""

    def __init__(
        self,
        *,
        base_url: str,
        model: str,
        batch_size: int = DEFAULT_OLLAMA_BATCH_SIZE,
        timeout: float = DEFAULT_OLLAMA_TIMEOUT,
    ) -> None:
        parsed = urllib.parse.urlparse(base_url)
        if parsed.scheme != "http" or parsed.username or parsed.password:
            raise ValueError("OLLAMA_BASE_URL must be a credential-free loopback HTTP URL")
        if parsed.query or parsed.fragment or parsed.hostname not in {
            "localhost",
            "127.0.0.1",
            "::1",
        }:
            raise ValueError("OLLAMA_BASE_URL must point to localhost or a loopback IP")
        if not model.strip():
            raise ValueError("EMBEDDING_MODEL must not be blank")
        if batch_size <= 0:
            raise ValueError("OLLAMA_BATCH_SIZE must be positive")
        if timeout <= 0:
            raise ValueError("OLLAMA_TIMEOUT must be positive")

        self.base_url = base_url.rstrip("/")
        self.model = model
        self.batch_size = batch_size
        self.timeout = timeout
        self._opener = urllib.request.build_opener(_NoRedirectHandler())

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        dimension: int | None = None
        for start in range(0, len(texts), self.batch_size):
            batch = texts[start : start + self.batch_size]
            batch_vectors = self._embed_batch(batch)
            for vector in batch_vectors:
                if dimension is None:
                    dimension = len(vector)
                elif len(vector) != dimension:
                    raise OllamaEmbeddingError(
                        "Ollama changed embedding dimensions within one request"
                    )
            vectors.extend(batch_vectors)
        return vectors

    def embed_query(self, text: str) -> list[float]:
        return self._embed_batch([text])[0]

    def _embed_batch(self, texts: list[str]) -> list[list[float]]:
        payload = json.dumps(
            {"model": self.model, "input": texts, "truncate": False}
        ).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/api/embed",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._opener.open(request, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            model_missing = "model" in detail.lower() and "not found" in detail.lower()
            if exc.code == 404 or model_missing:
                raise OllamaEmbeddingError(
                    f"Ollama model {self.model!r} is unavailable; "
                    f"run `ollama pull {self.model}`"
                ) from exc
            raise OllamaEmbeddingError(
                f"Ollama embedding request failed with HTTP {exc.code}: {detail}"
            ) from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            raise OllamaEmbeddingError(
                f"Ollama is unavailable at {self.base_url}; start the local service"
            ) from exc
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise OllamaEmbeddingError("Ollama returned invalid JSON") from exc

        vectors = data.get("embeddings")
        if not isinstance(vectors, list) or len(vectors) != len(texts):
            raise OllamaEmbeddingError(
                f"Ollama returned {len(vectors) if isinstance(vectors, list) else 0} "
                f"vectors for {len(texts)} inputs"
            )
        if any(
            not isinstance(vector, list)
            or not vector
            or any(not isinstance(value, (int, float)) for value in vector)
            for vector in vectors
        ):
            raise OllamaEmbeddingError("Ollama returned an invalid embedding vector")
        return vectors

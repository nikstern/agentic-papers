# Qdrant Search

This folder adds a minimal semantic search layer for the vault.

Default mode uses Ollama for local embeddings and connects to a Qdrant server at
`http://127.0.0.1:6333`. Paper text stays on the machine during embedding. The
repository includes a Docker Compose service for Qdrant, backed by a persistent
named volume and configured to restart when the local Docker runtime starts.

Embedded mode remains available through `QDRANT_MODE=embedded`, but it is
single-process and should only be used as an explicit fallback.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r search/requirements.txt
ollama pull embeddinggemma:300m
make search-server-up
python search/index_qdrant.py
python search/search_qdrant.py "shared memory coordination failures"
python search/ask_corpus.py "What are the strongest critiques of shared memory in multi-agent systems?"
```

On this macOS workstation, Homebrew runs Colima at login. Qdrant's
`restart: unless-stopped` policy then starts the existing container
automatically. Useful service commands:

```bash
make search-server-status
make search-server-logs
make search-server-stop
make search-server-up
```

If Qdrant is unavailable after login, run `brew services restart colima`, wait
for `colima status` to succeed, and then run `make search-server-up`.

## Environment

- `QDRANT_MODE`: `server` by default; set to `embedded` for the single-process fallback.
- `QDRANT_URL`: Qdrant server base URL. Defaults to `http://127.0.0.1:6333`.
- `QDRANT_API_KEY`: optional API key for a server deployment.
- `QDRANT_TIMEOUT`: server request timeout in seconds. Defaults to `5`.
- `QDRANT_COLLECTION`: collection name. Defaults to `agentic-papers`.
- `QDRANT_LOCAL_PATH`: embedded storage path. Defaults to `search/.qdrant`.
- `EMBEDDING_MODEL`: installed Ollama model. Defaults to `embeddinggemma:300m`.
- `OLLAMA_BASE_URL`: local Ollama URL. Defaults to `http://127.0.0.1:11434`; remote endpoints are rejected.
- `OLLAMA_BATCH_SIZE`: embedding request batch size. Defaults to `32`.
- `OLLAMA_TIMEOUT`: request timeout in seconds. Defaults to `30`.

Changing `EMBEDDING_MODEL` requires rebuilding the collection with `python search/index_qdrant.py` (or `make ingest`). For longer sections, `qwen3-embedding:0.6b` is an optional long-context alternative.

Server reindexing builds a new physical collection, validates its point count,
and atomically switches the stable `QDRANT_COLLECTION` alias. Searches therefore
see either the previous complete index or the new complete index.

If upgrading from embedded or older server indexing leaves a physical collection
with the same name as `QDRANT_COLLECTION`, reindexing stops without modifying it:
Qdrant cannot atomically replace a physical collection with a same-named alias.
Delete the legacy collection explicitly after confirming it can be rebuilt, or
set `QDRANT_COLLECTION` to a new alias name before reindexing.

## Indexed Content

Each indexed point represents one paper section with payload fields such as:

- `paper_id`
- `title`
- `candidate_topic`
- `paper_type`
- `year`
- `section`
- `path`
- `text`

Sections currently indexed:

- `summary`
- `why_it_matters`
- `method_setup`
- `key_claims`
- `limitations`
- `full_context`

## Discussion Mode

Use `ask_corpus.py` when you want a compact bundle of evidence for a discussion rather than raw nearest-neighbor hits.

```bash
python search/ask_corpus.py "What are the strongest critiques of shared memory in multi-agent systems?"
python search/ask_corpus.py "Which papers argue for role-specific memory instead of shared memory?" --topic memory-context
```

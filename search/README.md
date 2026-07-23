# Qdrant Search

This folder adds a minimal semantic search layer for the vault.

Default mode uses Ollama for local embeddings and Qdrant local storage under `search/.qdrant/`. Paper text stays on the machine during embedding. The same scripts can later switch Qdrant storage to a remote instance by setting `QDRANT_URL` and `QDRANT_API_KEY`; embeddings remain loopback-only.

Local mode is single-process. If you need concurrent queries or multiple clients at once, switch to a Qdrant server deployment.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r search/requirements.txt
ollama pull embeddinggemma:300m
python search/index_qdrant.py
python search/search_qdrant.py "shared memory coordination failures"
python search/ask_corpus.py "What are the strongest critiques of shared memory in multi-agent systems?"
```

## Environment

- `QDRANT_URL`: remote Qdrant base URL. If unset, scripts use local mode.
- `QDRANT_API_KEY`: API key for remote Qdrant.
- `QDRANT_COLLECTION`: collection name. Defaults to `agentic-papers`.
- `QDRANT_LOCAL_PATH`: local Qdrant storage path. Defaults to `search/.qdrant`.
- `EMBEDDING_MODEL`: installed Ollama model. Defaults to `embeddinggemma:300m`.
- `OLLAMA_BASE_URL`: local Ollama URL. Defaults to `http://127.0.0.1:11434`; remote endpoints are rejected.
- `OLLAMA_BATCH_SIZE`: embedding request batch size. Defaults to `32`.
- `OLLAMA_TIMEOUT`: request timeout in seconds. Defaults to `30`.

Changing `EMBEDDING_MODEL` requires rebuilding the collection with `python search/index_qdrant.py` (or `make ingest`). For longer sections, `qwen3-embedding:0.6b` is an optional long-context alternative.

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

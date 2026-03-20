# Qdrant Search

This folder adds a minimal semantic search layer for the vault.

Default mode uses Qdrant local storage under `search/.qdrant/`, so you can experiment without running a separate server. The same scripts can later switch to a remote Qdrant instance by setting `QDRANT_URL` and `QDRANT_API_KEY`.

Local mode is single-process. If you need concurrent queries or multiple clients at once, switch to a Qdrant server deployment.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r search/requirements.txt
python search/index_qdrant.py
python search/search_qdrant.py "shared memory coordination failures"
python search/ask_corpus.py "What are the strongest critiques of shared memory in multi-agent systems?"
```

## Environment

- `QDRANT_URL`: remote Qdrant base URL. If unset, scripts use local mode.
- `QDRANT_API_KEY`: API key for remote Qdrant.
- `QDRANT_COLLECTION`: collection name. Defaults to `agentic-papers`.
- `QDRANT_LOCAL_PATH`: local Qdrant storage path. Defaults to `search/.qdrant`.
- `EMBEDDING_MODEL`: FastEmbed model name. Defaults to `BAAI/bge-small-en-v1.5`.

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

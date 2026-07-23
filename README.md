# Agentic Research Vault

This repository is an Obsidian vault for summaries and metadata for agentic AI research papers, with a focus on single-agent systems, multi-agent systems, memory, evaluation, and related synthesis work. All papers are linked to their original sources. Copyright remains with the original authors and publishers.

It stores:

- structured source metadata in `paper_inbox/`
- generated paper notes in `paper_notes/`
- topic-level synthesis in `topic_maps/`
- authored writing and planning docs in `drafts/`

The repository is designed around a deterministic paper-ingestion workflow:

- authoritative paper state lives in `paper_inbox/papers.csv`
- richer extracted metadata lives in `paper_inbox/enrichment/*.json`
- notes are generated, not manually maintained as primary source state
- local paper-to-paper links are resolved during ingest when titles match existing vault papers
- each ingest refreshes `paper_inbox/approved_for_enrichment.json` so pending enrichment work is queued automatically
- semantic search in `search/` uses local Ollama embeddings and is refreshed after ingest when `.venv`, Ollama, and Qdrant are available
- optional automatic enrichment can be run through `scripts/run_enrichment.py` when `OPENAI_API_KEY` is configured
- trusted Codex sessions can use the project-configured arXiv MCP server for paper discovery and reading

## Requirements

Base vault usage only requires:

- Obsidian or another Markdown editor
- `python3` for the local workflow scripts

Codex-based paper discovery additionally requires `uvx`; the project-local `.codex/config.toml` launches `arxiv-mcp-server` on demand after the repository is trusted.

Semantic search requires:

- a local virtual environment at `.venv`
- Python packages from `search/requirements.txt`
- Ollama with the local `embeddinggemma:300m` model installed
- the repository's localhost Qdrant server, started with `make search-server-up`
- Docker with Colima or another compatible local runtime

Automatic enrichment additionally requires:

- `OPENAI_API_KEY`
- outbound network access to OpenAI and paper sources such as arXiv

Emailing the reading queue additionally requires:

- the local Gmail helper expected by `scripts/email_reading_queue.py`
- a working local Gmail/OAuth setup for that helper

## Setup

Create the virtual environment and install the search stack:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r search/requirements.txt
ollama pull embeddinggemma:300m
make search-server-up
make reindex-search
```

Optional environment variables:

- `OPENAI_API_KEY`: required for `make enrich-pending`
- `OPENAI_MODEL`: overrides the default enrichment model
- `OPENAI_MAX_ATTEMPTS`: transient OpenAI request attempts before failure (defaults to `3`)
- `QDRANT_MODE`: defaults to `server`; set to `embedded` for the explicit single-process fallback
- `QDRANT_URL`: server base URL, defaulting to `http://127.0.0.1:6333`
- `QDRANT_API_KEY`: optional API key for a server deployment
- `QDRANT_TIMEOUT`: server request timeout in seconds, defaulting to `5`
- `QDRANT_COLLECTION`: overrides the default collection name
- `QDRANT_LOCAL_PATH`: overrides the embedded fallback path
- `EMBEDDING_MODEL`: overrides the default Ollama embedding model (`embeddinggemma:300m`)
- `OLLAMA_BASE_URL`: overrides the loopback Ollama URL (remote hosts are rejected)
- `OLLAMA_BATCH_SIZE`: overrides the default embedding batch size (`32`)
- `OLLAMA_TIMEOUT`: overrides the default Ollama request timeout in seconds (`30`)

Common local commands:

```bash
make ingest
make enrich-pending
make test
make test-search
make search-server-status
python search/search_qdrant.py "shared memory coordination failures"
python search/ask_corpus.py "Which papers build on MemGPT?"
```

The Qdrant container binds only to localhost, stores data in the
`agentic-papers-qdrant-data` Docker volume, and restarts when Colima starts at
macOS login. See `search/README.md` for service operations and troubleshooting.

`make enrich-pending` regenerates the pending queue, refuses to call the model when paper text cannot be fetched, requests strict schema-conforming output, and retries transient API failures. Enrichment remains remote: source text is sent to OpenAI when this command is run.

## Key Docs

- [Workflow](/Users/nikstern/Documents/Agentic/docs/workflow.md)
- [Paper Inbox Schema](/Users/nikstern/Documents/Agentic/paper_inbox/README.md)

## Repository Layout

- `paper_inbox/`: source data, import artifacts, and enrichment payloads
- `paper_notes/`: generated atomic paper notes
- `topic_maps/`: topic hubs and synthesis maps
- `drafts/`: draft writing and planning notes
- `scripts/`: ingestion and workflow scripts

## Current Conventions

- generated paper note filenames use hyphenated names such as `2025-G-Memory-...md`
- topic map filenames also use hyphenated names such as `Memory-Context.md`
- frontmatter stays flat and Obsidian-safe

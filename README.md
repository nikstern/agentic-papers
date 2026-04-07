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
- semantic search in `search/` is refreshed after ingest when `.venv` and the Qdrant search stack are available
- optional automatic enrichment can be run through `scripts/run_enrichment.py` when `OPENAI_API_KEY` is configured

## Requirements

Base vault usage only requires:

- Obsidian or another Markdown editor
- `python3` for the local workflow scripts

Semantic search requires:

- a local virtual environment at `.venv`
- Python packages from `search/requirements.txt`
- local embedded Qdrant storage under `search/.qdrant/` or a remote Qdrant instance via `QDRANT_URL`

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
```

Optional environment variables:

- `OPENAI_API_KEY`: required for `make enrich-pending`
- `OPENAI_MODEL`: overrides the default enrichment model
- `QDRANT_URL`: use a remote Qdrant instance instead of local embedded storage
- `QDRANT_API_KEY`: API key for remote Qdrant
- `QDRANT_COLLECTION`: overrides the default collection name
- `QDRANT_LOCAL_PATH`: overrides the local embedded Qdrant path
- `EMBEDDING_MODEL`: overrides the default FastEmbed model

Common local commands:

```bash
make ingest
make enrich-pending
python search/search_qdrant.py "shared memory coordination failures"
python search/ask_corpus.py "Which papers build on MemGPT?"
```

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

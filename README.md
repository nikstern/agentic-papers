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

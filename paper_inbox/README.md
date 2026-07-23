# Paper Inbox Schema

This folder is the deterministic source layer for paper ingestion and enrichment state.

Workflow details live in [docs/workflow.md](/Users/nikstern/Documents/Agentic/docs/workflow.md). This file only documents the source schema, contracts, and rules for `paper_inbox/`.

## Primary Source Files

- `papers.csv`: authoritative paper metadata and lifecycle state
- `enrichment/*.json`: structured extracted metadata keyed by `paper_id`
- `mcp_candidates.example.json`: candidate import contract
- `enrichment.example.json`: enrichment import contract

## Generated Workflow Artifacts

- `last_import.json`: records assigned IDs for the most recent candidate import
- `approved_for_enrichment.json`: deterministic export payload for pending enrichment work

## Note Data Model

Generated notes keep only flat, Obsidian-safe properties in frontmatter.

- stable metadata lives in `papers.csv`
- richer extracted metadata lives in `paper_inbox/enrichment/*.json`
- unresolved references stay as plain title lists until they can be resolved deterministically
- `make ingest` resolves matching titles into local links when possible

## Required Columns

- `paper_id`
- `title`
- `url`
- `year`
- `authors`
- `candidate_topic`
- `source`
- `paper_type`
- `status`
- `enrichment_status`

## Allowed `candidate_topic`

- `llm-multi-agent-systems`
- `agent-evaluation`
- `agent-harnesses`
- `task-allocation`
- `search-retrieval`
- `central-place-foraging`
- `hallucination-factuality`
- `software-agents`
- `memory-context`

## Allowed `paper_type`

- `survey`
- `benchmark`
- `system`
- `position`
- `application`

## Allowed `status`

- `candidate`
- `approved`
- `ingested`
- `skimmed`
- `deep_read`
- `cited`
- `discarded`

## Allowed `enrichment_status`

- `pending`
- `enriched`
- `failed`

## Rules

1. One paper per CSV row.
2. Do not add extra columns unless the scripts are updated first.
3. Generated paper note filenames use the form `YEAR-Short-Title.md`.
4. Topic map filenames use hyphenated names such as `Memory-Context.md`.
5. `paper_id` must be unique and numeric.
6. Title and URL duplicates are rejected by the scripts.
7. Search results should enter as `candidate`.
8. Only `approved` papers are ingested into notes.
9. Approved papers are ingested immediately; enrichment is a follow-up step.
10. Every row must carry an authoritative `enrichment_status`.
11. Enrichment should be minimal and fixed-schema by default.
12. The preferred enrichment path is `answer_pdf_queries`, with `get_paper_content` as fallback.
13. Successful enrichment import sets `enrichment_status = enriched`.
14. Failed extraction attempts should be recorded as `enrichment_status = failed`.
15. The ingestion script only accepts the controlled vocabularies above.
16. Topic links are derived from `candidate_topic`, not handwritten per note.
17. A per-paper enrichment file takes precedence over stale pending state; ingest reconciles that row to `enriched`.
18. Import validates the complete batch before publishing atomically replaced files and registry state.

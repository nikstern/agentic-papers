# Paper Inbox Schema

This folder is the deterministic source for paper ingestion.

## File

`papers.csv`

## MCP Import

When papers are gathered through alphaXiv MCP, first write them to a JSON array
matching `mcp_candidates.example.json`, then import them with:

```bash
make import-candidates FILE=paper_inbox/mcp_candidates.example.json
```

Imported MCP results are stored as `candidate` rows with source
`alphaxiv-mcp`.

Each import also writes `last_import.json`, which records the exact assigned
`paper_id` values for newly imported rows and any skipped duplicates.

## Enrichment Import

Approved papers should enter the vault immediately. Enrichment then runs as a
second phase and rerenders notes after the fact.

After approved papers are analyzed with `answer_pdf_queries` or, when needed,
`get_paper_content`, save the results as a JSON array matching
`enrichment.example.json`, then import them with:

```bash
make import-enrichment FILE=paper_inbox/enrichment.example.json
```

Imported enrichment is stored per paper under `paper_inbox/enrichment/` and is
used by `make ingest` when rendering notes.

Generate the deterministic input payload for this step with:

```bash
make export-enrichment-input
```

This writes `approved_for_enrichment.json` with the paper IDs, URLs, and fixed
query set to use for background enrichment. Only papers with active reading
state and `enrichment_status = pending` are exported.

## Note Schema

Notes keep only flat, Obsidian-safe properties in frontmatter.

- stable metadata lives in `papers.csv`
- richer extracted metadata lives in `paper_inbox/enrichment/*.json`
- unresolved references stay as plain title lists
- `make ingest` resolves those titles into local links when possible

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
2. Do not add extra columns unless the script is updated first.
3. Use `YEAR - Short Title.md` for generated note filenames.
4. `paper_id` must be unique and numeric.
5. Title and URL duplicates are rejected by the scripts.
6. Search results should enter as `candidate`.
7. Only `approved` papers are ingested into notes.
8. Approved papers are ingested immediately; enrichment is a follow-up step.
9. Every row must carry an authoritative `enrichment_status`.
10. Enrichment should be minimal and fixed-schema by default.
11. The preferred enrichment path is `answer_pdf_queries`, with `get_paper_content` as fallback.
12. Successful enrichment import sets `enrichment_status = enriched`.
13. Failed extraction attempts should be recorded as `enrichment_status = failed`.
14. The ingestion script only accepts the controlled vocabularies above.
15. Topic links are derived from `candidate_topic`, not handwritten per note.

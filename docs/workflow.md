# Workflow

This repository uses a deterministic paper workflow so papers can be discovered, approved, enriched, and rerendered without turning rendered notes into a second source of truth.

## Workflow Spec

1. Discover with alphaXiv MCP.
2. Present a numbered shortlist. Do not write anything yet.
3. Wait for explicit approval.
4. Import approved papers as flat metadata.
5. Ingest approved papers immediately so notes appear in the vault without blocking on enrichment latency.
6. Mark enrichment as pending and queue enrichment input automatically during ingest.
7. Store enrichment outside notes under `paper_inbox/enrichment/`.
8. Record enrichment as `enriched` or `failed` in `papers.csv`.
9. Rerender notes from metadata plus enrichment when enrichment completes.
10. Refresh the semantic search index after ingest when the local search environment is available.
11. Resolve unresolved relation titles into local links on every ingest or rerender.
12. Keep unmatched references as unresolved text for future reconciliation.

## Command Flow

1. Gather candidates with alphaXiv MCP.
2. Save the shortlist in the JSON shape shown by `paper_inbox/mcp_candidates.example.json`.
3. Import candidates with `make import-candidates FILE=...`.
4. Read assigned IDs from `paper_inbox/last_import.json` or the import output.
5. Approve papers by `paper_id` with `make approve IDS='1 2 3'`.
6. Run `make ingest` so approved papers appear immediately in `paper_notes/` and `topic_maps/`; this also refreshes `approved_for_enrichment.json` and the semantic search index.
7. Use `paper_inbox/approved_for_enrichment.json` as the deterministic pending-enrichment queue for background enrichment.
8. Run `make enrich-pending` for an automatic enrichment pass when `OPENAI_API_KEY` is configured, or use the MCP/manual enrichment path when higher-fidelity extraction is needed. The command regenerates the queue before calling OpenAI.
9. Save enrichment results in the JSON shape shown by `paper_inbox/enrichment.example.json`.
10. Import enrichment with `make import-enrichment FILE=...` when importing a manual or external enrichment payload.
11. `make import-enrichment` rerenders notes and refreshes the search index automatically.
12. `make ingest-and-enrich` runs the full local loop: ingest, queue export, automatic enrichment, rerender, and reindex.
13. If enrichment fails after fallback, mark the paper with `make mark-enrichment-failed IDS='...'`.
14. Review generated notes in `paper_notes/`.
15. Write synthesis in `topic_maps/` and `drafts/`.

## Deterministic Guarantees

- controlled vocabularies for topic, type, and status
- human approval gate before ingestion
- fixed note filename format
- flat, Obsidian-safe frontmatter schema
- duplicate detection on `paper_id`, title, and URL
- MCP search results imported through a strict JSON contract
- PDF enrichment imported through a strict JSON contract
- approved papers can enter the vault before enrichment completes
- enrichment lifecycle state is authoritative in `papers.csv`
- existing per-paper enrichment files are never queued again and are reconciled to `enriched` during ingest
- complete enrichment batches are validated before files or registry state are published
- automatic enrichment uses strict schema output and bounded retries for transient failures
- enrichment updates notes through deterministic rerendering, not manual note edits
- unresolved paper references are reconciled on every ingest
- topic maps are updated from CSV source state, not ad hoc linking

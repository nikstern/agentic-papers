# Agentic Research Vault

This vault uses a deterministic paper workflow with LLM-native discovery and flat, Obsidian-safe note properties.

## Workflow Spec

1. Discover with alphaXiv MCP.
2. Present a numbered shortlist. Do not write anything yet.
3. Wait for explicit approval.
4. Import approved papers as flat metadata.
5. Ingest approved papers immediately so notes appear in the vault without blocking on MCP latency.
6. Mark enrichment as pending and run minimal enrichment in the background.
7. Store enrichment outside notes under `paper_inbox/enrichment/`.
8. Record enrichment as `enriched` or `failed` in `papers.csv`.
9. Rerender notes from metadata + enrichment when enrichment completes.
10. Resolve unresolved relation titles into local links on every ingest or rerender.
11. Keep unmatched references as unresolved text for future reconciliation.

## Workflow

1. Gather candidates with alphaXiv MCP.
2. Save the shortlist in the JSON shape shown by `paper_inbox/mcp_candidates.example.json`.
3. Import them with `make import-candidates FILE=...`.
4. Read assigned IDs from `paper_inbox/last_import.json` or the import output.
5. Approve papers by `paper_id` with `make approve IDS='1 2 3'`.
6. Run `make ingest` so approved papers appear immediately in `paper_notes/` and `topic_maps/`.
7. Run `make export-enrichment-input` to emit the papers and fixed query set for background enrichment.
8. Use `answer_pdf_queries` when it is clean enough; fall back to `get_paper_content` when needed.
9. Save the enrichment results in the JSON shape shown by `paper_inbox/enrichment.example.json`.
10. Import enrichment with `make import-enrichment FILE=...`.
11. If enrichment fails after fallback, mark the paper with `make mark-enrichment-failed IDS='...'`.
12. Run `make ingest` again to rerender enriched notes and resolve links.
13. Review generated notes in `paper_notes/`.
14. Write synthesis in `topic_maps/` and `drafts/`.

## Deterministic Guarantees

- Controlled vocabularies for topic, type, and status.
- Human approval gate before ingestion.
- Fixed note filename format.
- Flat, Obsidian-safe frontmatter schema.
- Duplicate detection on `paper_id`, title, and URL.
- MCP search results are imported through a strict JSON contract.
- PDF enrichment is imported through a strict JSON contract.
- Approved papers can enter the vault before enrichment completes.
- Enrichment lifecycle state is authoritative in `papers.csv`.
- Enrichment updates notes through deterministic rerendering, not manual edits.
- Unresolved paper references are reconciled on every ingest.
- Topic maps updated from the CSV source, not by ad hoc linking.

## Folders

- `paper_inbox/`: structured source data
- `paper_notes/`: generated atomic paper notes
- `topic_maps/`: synthesis hubs
- `drafts/`: authored writing

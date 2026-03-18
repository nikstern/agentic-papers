# Agentic Research Vault

This vault uses a deterministic paper workflow with LLM-native discovery and flat, Obsidian-safe note properties.

## Workflow Spec

1. Discover with alphaXiv MCP.
2. Present a numbered shortlist. Do not write anything yet.
3. Wait for explicit approval.
4. Import approved papers as flat metadata.
5. Run minimal enrichment with `answer_pdf_queries`.
6. Store enrichment outside notes under `paper_inbox/enrichment/`.
7. Render notes from metadata + enrichment.
8. Resolve unresolved relation titles into local links on every ingest.
9. Keep unmatched references as unresolved text for future reconciliation.

## Workflow

1. Gather candidates with alphaXiv MCP.
2. Save the shortlist in the JSON shape shown by `paper_inbox/mcp_candidates.example.json`.
3. Import them with `make import-candidates FILE=...`.
4. Read assigned IDs from `paper_inbox/last_import.json` or the import output.
5. Approve papers by `paper_id` with `make approve IDS='1 2 3'`.
6. Run `make export-enrichment-input` to emit the approved-paper list and fixed query set.
7. Use `answer_pdf_queries` on those papers and save the results in the JSON shape shown by `paper_inbox/enrichment.example.json`.
8. Import enrichment with `make import-enrichment FILE=...`.
9. Run `make ingest`.
10. Review generated notes in `paper_notes/`.
11. Write synthesis in `topic_maps/` and `drafts/`.

## Deterministic Guarantees

- Controlled vocabularies for topic, type, and status.
- Human approval gate before ingestion.
- Fixed note filename format.
- Flat, Obsidian-safe frontmatter schema.
- Duplicate detection on `paper_id`, title, and URL.
- MCP search results are imported through a strict JSON contract.
- PDF enrichment is imported through a strict JSON contract.
- Unresolved paper references are reconciled on every ingest.
- Topic maps updated from the CSV source, not by ad hoc linking.

## Folders

- `paper_inbox/`: structured source data
- `paper_notes/`: generated atomic paper notes
- `topic_maps/`: synthesis hubs
- `drafts/`: authored writing

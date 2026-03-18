# Workflow Improvements Plan

## 1. Enrichment Fallback Policy

### Goal
Make enrichment reliable when `answer_pdf_queries` returns incomplete or malformed output.

### Plan
- Define the default order explicitly:
  1. try `answer_pdf_queries`
  2. validate whether the response is usable
  3. if unusable, fall back to `get_paper_content`
- Add a short rule for what counts as unusable:
  - empty response
  - truncated response
  - missing answers to the fixed query set
- Update the workflow docs so this is the standard path, not an ad hoc fallback.

### Result
The enrichment path becomes predictable and robust without changing the vault schema.

## 2. Feedback and Value Tracking

### Goal
Let the system learn over time which papers are actually valuable.

### Plan
- Add a small structured feedback store, likely `paper_inbox/paper_feedback.csv`.
- Track a minimal set of signals:
  - `paper_id`
  - `deep_read`
  - `cited`
  - `used_in_draft`
  - optional `notes`
- Keep the first version simple and deterministic.
- Later use this file to influence shortlist ranking and recommendations.

### Result
The vault can distinguish between papers that were merely ingested and papers that became central to the research workflow.

## 3. Resolver Report

### Goal
Make unresolved-reference reconciliation visible and auditable.

### Plan
- Extend `make ingest` / `scripts/ingest_papers.py` to report:
  - how many unresolved references were resolved in this run
  - how many unresolved references remain
  - optionally which notes were updated
- Keep the report lightweight and deterministic.
- If useful, also write a small machine-readable artifact such as `paper_inbox/last_resolution.json`.

### Result
The paper-to-paper linking process becomes easier to trust and easier to debug.

## 4. Topic Cross-Links

### Goal
Make topic maps connect more clearly when concepts overlap.

### Plan
- Add a minimal `## Related Topics` section to topic map notes.
- Only add sparse, high-signal links.
- Start with:
  - `Memory Context` <-> `LLM Multi-Agent Systems`
  - `Memory Context` <-> `Agent Harnesses`
  - `LLM Multi-Agent Systems` <-> `Task Allocation`
- Keep these links curated, not automatically generated.

### Result
The Obsidian graph will show stronger topic-level structure instead of only paper-level overlap.

## Priority Order

1. Enrichment fallback policy
2. Feedback and value tracking
3. Resolver report
4. Topic cross-links

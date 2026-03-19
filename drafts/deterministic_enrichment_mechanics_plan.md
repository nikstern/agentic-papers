# Deterministic Enrichment Mechanics Spec

## Goal

Make paper enrichment mechanically deterministic without requiring semantic determinism from the LLM.

The system should guarantee:

1. fixed input contracts
2. fixed state transitions
3. fixed write targets
4. fixed rerender behavior
5. fixed reference resolution rules

The extraction content may vary. The workflow mechanics must not vary.

## Scope

This spec covers:

- authoritative paper state in `paper_inbox/papers.csv`
- enrichment payloads in `paper_inbox/enrichment/*.json`
- note rendering in `paper_notes/`
- topic map updates in `topic_maps/`
- export/import mechanics for background enrichment

This spec does not require semantic consistency from MCP tools or the LLM.

## Design Principles

### Separate Semantic Variability From Mechanical Determinism

The LLM may produce different wording or different levels of detail across runs.
That is acceptable.

The pipeline must still enforce:

- the same schema
- the same valid states
- the same transition rules
- the same write destinations
- the same rerender inputs

### One Authoritative State Layer

The source of truth is `paper_inbox/papers.csv`.

Rendered notes are projections of source state. They are not an independent workflow state store.

Enrichment JSON files hold structured extracted content, but they do not replace authoritative lifecycle state in `papers.csv`.

### Ingest Must Not Block On Enrichment

Approved papers must appear in the vault immediately after ingest, even when enrichment has not run yet or has failed.

## State Model

Keep reading lifecycle and enrichment lifecycle separate.

### Paper Lifecycle

Allowed `status` values remain:

- `candidate`
- `approved`
- `ingested`
- `skimmed`
- `deep_read`
- `cited`
- `discarded`

### Enrichment Lifecycle

Add an authoritative `enrichment_status` column to `papers.csv`.

Allowed values:

- `pending`
- `enriched`
- `failed`

### State Semantics

- `pending`: the paper is eligible for enrichment work or awaiting enrichment output
- `enriched`: a valid enrichment JSON file has been imported for the paper
- `failed`: enrichment was attempted but no valid usable extraction was produced

`failed` is a terminal workflow state for a given attempt, but not necessarily permanent. A later explicit retry may move it back to `pending`, then to `enriched` or `failed` again.

## Normative Invariants

The system must enforce these invariants:

1. Every row in `papers.csv` has one valid `status`.
2. Every row in `papers.csv` has one valid `enrichment_status`.
3. Only `papers.csv` defines lifecycle state.
4. Enrichment JSON never changes paper lifecycle `status`.
5. Ingest may change `status` from `approved` to `ingested`.
6. Ingest may set `enrichment_status` to `pending` when required by rule.
7. Enrichment import may change `enrichment_status` to `enriched`.
8. Failure handling may change `enrichment_status` to `failed`.
9. Notes and topic maps are rerendered from source data, not manually patched.
10. Reference resolution is title-rule-based only and never delegated to the LLM.

## Deterministic Workflow

### Phase 1: Discovery

1. Gather candidates with alphaXiv MCP.
2. Present a shortlist.
3. Wait for explicit user approval.

Deterministic mechanics:

- fixed import shape from `mcp_candidates.example.json`
- duplicate detection at import
- deterministic `paper_id` assignment
- no vault mutation before approval

### Phase 2: Candidate Import

1. Import selected candidate JSON into `paper_inbox/papers.csv`.
2. Assign:
   - `status = candidate`
3. Assign default enrichment state:
   - `enrichment_status = pending`
4. Write `paper_inbox/last_import.json`.

Rationale:

- Every paper should have a valid enrichment lifecycle value immediately.
- `pending` here means "not yet enriched or failed"; export rules will decide when work is actually queued.

### Phase 3: Approval

1. Approve papers by `paper_id`.
2. Transition:
   - `candidate -> approved`
3. Do not change `enrichment_status`.

### Phase 4: Immediate Ingest

1. Run `make ingest`.
2. Transition:
   - `approved -> ingested`
3. If the paper has no enrichment file and `enrichment_status` is not `failed`, enforce:
   - `enrichment_status = pending`
4. Render note immediately from CSV metadata plus any existing enrichment JSON.

This guarantees fast vault entry without waiting for enrichment.

### Phase 5: Background Enrichment Export

1. Run `make export-enrichment-input`.
2. Export only papers where:
   - `status in {ingested, skimmed, deep_read, cited}`
   - `enrichment_status = pending`
3. Export:
   - `paper_id`
   - `title`
   - `url`
   - `status`
   - fixed query set

Deterministic mechanics:

- no `approved` rows in enrichment export
- no `failed` rows in export unless a separate retry command explicitly resets them
- same query set order every time
- same paper order every time

### Phase 6: Background Enrichment Execution

1. Run enrichment outside the critical path.
2. Attempt extraction with `answer_pdf_queries`.
3. If output is empty, malformed, or unusable, fall back to `get_paper_content`.
4. Map the result to the same fixed enrichment JSON schema.

The content may vary. The contract must not vary.

### Phase 7: Enrichment Import

1. Import enrichment JSON from a fixed array shape.
2. Validate every item.
3. Write each validated payload to `paper_inbox/enrichment/{paper_id}.json`.
4. Transition:
   - `pending -> enriched`
5. Leave paper lifecycle `status` unchanged.

Import must be deterministic:

- same validation rules
- same write path
- same overwrite behavior
- same status update behavior

### Phase 8: Failure Recording

If enrichment for a paper cannot produce a valid usable payload after fallback:

1. record explicit failure for the `paper_id`
2. transition:
   - `pending -> failed`
3. keep the paper note renderable from metadata only

Failure must be represented as authoritative state, not hidden in prose or operator memory.

### Phase 9: Rerender

1. Run `make ingest` again.
2. Rerender notes from:
   - `papers.csv`
   - `paper_inbox/enrichment/*.json`
3. Resolve references deterministically.
4. Update topic maps deterministically.

## State Transition Rules

### Allowed `status` Transitions

- `candidate -> approved`
- `approved -> ingested`
- `ingested -> skimmed`
- `skimmed -> deep_read`
- `deep_read -> cited`
- `candidate -> discarded`
- `approved -> discarded`
- `ingested -> discarded`
- `skimmed -> discarded`
- `deep_read -> discarded`

This spec does not introduce new paper lifecycle states.

### Allowed `enrichment_status` Transitions

- initial import: `pending`
- `pending -> enriched`
- `pending -> failed`
- explicit retry only: `failed -> pending`
- explicit retry overwrite only: `enriched -> pending`

No other transitions are valid.

### Non-Transitions

These operations must not change state:

- note rerender alone must not change `enrichment_status`
- enrichment import must not change `status`
- approval must not change `enrichment_status`
- exporting enrichment input must not change any state

## Required Schema Changes

### `papers.csv`

Add one column:

- `enrichment_status`

Required header order:

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

### Note Frontmatter

Add:

- `enrichment_status`

This is rendered presentation of authoritative state, not an independent note-only field.

### Enrichment JSON

Keep the fixed shape:

- `paper_id`
- `summary`
- `why_it_matters`
- `method_setup`
- `key_claims`
- `limitations`
- `evaluates`
- `builds_on_unresolved`
- `compares_to_unresolved`

No schema drift.
No optional alternate field names.

## Deterministic Fallback Mechanics

Fallback policy must be implemented as workflow logic, not as prompt preference:

1. attempt extraction with `answer_pdf_queries`
2. validate whether output is usable for the enrichment schema
3. if unusable, use `get_paper_content`
4. map to the same enrichment schema
5. import through the same deterministic JSON contract

Usability should be defined mechanically.
At minimum, unusable includes:

- non-JSON output when JSON is required by the operator step
- missing required fields
- wrong field types
- structurally empty payloads for required string or list fields

## Deterministic Resolution Rules

Reference resolution remains fully rule-based:

1. normalize unresolved title
2. compare against normalized note title index
3. if matched:
   - write resolved wiki-link field
4. if unmatched:
   - keep in unresolved field

No LLM participates in reference resolution.

## Ordering Rules

To preserve deterministic output, scripts should use fixed ordering:

1. `papers.csv` row order is preserved on rewrite.
2. export payload order follows `papers.csv` row order.
3. note rendering iterates in `papers.csv` row order.
4. topic map inclusion order follows `papers.csv` row order.
5. relation lists preserve imported list order except for deterministic title resolution.

## Idempotency Rules

Repeated runs with unchanged inputs should produce the same outputs.

### `make ingest`

If run twice without data changes:

- `papers.csv` should not drift
- rendered notes should not drift
- topic maps should not drift

### `make import-enrichment`

If the same valid enrichment payload is imported twice:

- the same JSON file should be written
- `enrichment_status` should remain `enriched`
- no unrelated rows should change

### `make export-enrichment-input`

If no paper states change:

- exported paper set should remain the same
- query order should remain the same

## Implementation Checklist

### Step 1: CSV Schema Migration

Update:

- `paper_inbox/papers.csv`
- schema docs
- all CSV readers and writers
- header validation

Migration rule:

- existing rows with enrichment JSON file -> `enriched`
- existing rows without enrichment JSON file -> `pending`

### Step 2: Ingest Logic

Update `make ingest` behavior:

- `approved -> ingested`
- inject `enrichment_status` into note frontmatter
- if row is active and has no enrichment file and status is not `failed`, enforce `pending`

### Step 3: Enrichment Import Logic

Update enrichment import:

- validate payload schema
- write `paper_inbox/enrichment/{paper_id}.json`
- set `enrichment_status = enriched` in `papers.csv`

### Step 4: Failure Path

Add an explicit failure-recording mechanism:

- import a failure file, or
- add a script that marks paper IDs as failed

Required effect:

- set `enrichment_status = failed`
- do not block notes from rendering

### Step 5: Enrichment Export Logic

Update `make export-enrichment-input` to select only:

- `status in {ingested, skimmed, deep_read, cited}`
- `enrichment_status = pending`

### Step 6: Docs And Skill Text

Update docs to reflect:

- ingest-first
- enrichment as second lifecycle
- explicit success and failure states
- rerender driven from authoritative source data

## Review: Gaps In The Current Repo

The current repo already follows ingest-first at the documentation level, but it does not yet fully implement this deterministic enrichment model.

### Confirmed Gaps

1. `paper_inbox/papers.csv` has no `enrichment_status` column, so there is no authoritative enrichment lifecycle state.
2. [`scripts/ingest_papers.py`](/Users/nikstern/Documents/Agentic/scripts/ingest_papers.py) validates an exact CSV header without `enrichment_status`, so schema migration is mandatory before behavior can change.
3. [`scripts/ingest_papers.py`](/Users/nikstern/Documents/Agentic/scripts/ingest_papers.py) renders notes without writing `enrichment_status` into frontmatter.
4. [`scripts/ingest_papers.py`](/Users/nikstern/Documents/Agentic/scripts/ingest_papers.py) changes `approved -> ingested` but does not enforce any enrichment lifecycle rule.
5. [`scripts/import_enrichment.py`](/Users/nikstern/Documents/Agentic/scripts/import_enrichment.py) writes enrichment JSON files but does not update `papers.csv`, so successful enrichment is not represented in authoritative state.
6. [`scripts/export_enrichment_input.py`](/Users/nikstern/Documents/Agentic/scripts/export_enrichment_input.py) currently exports `approved` papers as well as active ingested papers, which conflicts with the intended ingest-first, enrich-after-ingest model.
7. The current workflow has no explicit failure-recording path for enrichment, so `failed` cannot be represented mechanically.
8. The docs describe fallback behavior, but there is no script-level contract for marking extraction attempts as unusable and recording failure.

### Ambiguities To Resolve Before Coding

1. Should newly imported `candidate` rows default to `pending`, or should `pending` only begin once a paper becomes `ingested`? This spec chooses immediate `pending` so every row has a value, while export rules control queue eligibility.
2. Should `failed` papers be excluded from all future exports by default? This spec says yes, unless an explicit retry action resets them to `pending`.
3. Should importing enrichment for an already `enriched` paper overwrite the existing JSON file? This spec assumes yes, because overwrite behavior is simpler and deterministic, but it should be stated explicitly in the implementation.
4. Should there be a machine-readable failure artifact, or is updating `papers.csv` enough? This spec requires authoritative state in `papers.csv`; a separate failure artifact is optional.

## Success Criteria

The workflow is mechanically deterministic when:

1. every paper has a valid paper lifecycle state
2. every paper has a valid enrichment lifecycle state
3. ingestion never blocks on enrichment
4. enrichment success and failure are script-enforced state transitions
5. rerendering is always driven from source data
6. enrichment import always uses one schema
7. reference resolution never depends on model output
8. repeated runs with unchanged inputs are idempotent

## Recommended Next Implementation Order

1. migrate CSV schema and script validation
2. update ingest to render and maintain `enrichment_status`
3. update enrichment import to set `enriched`
4. add failure-recording mechanics
5. tighten export selection to active `pending` rows only
6. update docs and skill text

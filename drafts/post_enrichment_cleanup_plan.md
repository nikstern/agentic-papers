# Post-Enrichment Cleanup Plan

## Goal

Clean up a completed enrichment batch so the vault is more trustworthy, more linkable, and easier to use for synthesis work.

This phase happens after enrichment JSON has already been imported. It is not part of the extraction step itself.

## Desired Outcomes

The cleanup pass should produce four results:

1. enrichment fields read as paper-specific rather than generic
2. unresolved references are reduced wherever the referenced paper already exists in the vault
3. rendered paper notes become cleaner and more navigable
4. no schema drift or ad hoc note patching is introduced

## Scope

This plan covers two follow-up tracks:

1. enrichment quality review
2. unresolved reference resolution

Artifacts in scope:

- `paper_inbox/enrichment/*.json`
- `paper_inbox/papers.csv` only if cleanup requires authoritative metadata fixes
- `paper_notes/`

Artifacts out of scope:

- changing the enrichment schema
- changing extraction prompts
- manually editing rendered paper notes as a primary workflow

## Operating Principles

### Source-of-Truth Discipline

Cleanup should patch structured source files, then rerender.

Do not hand-edit rendered notes unless debugging a renderer issue. Normal cleanup should flow through:

1. patch source data
2. rerun `make ingest`
3. inspect rendered output

### Conservative Resolution

Resolve references only when there is a strong deterministic title match to a paper that already exists in the vault.

If a match is partial, ambiguous, or uncertain, leave it unresolved.

### Paper-Specific Over Generic

When reviewing enrichment content, prefer short, specific statements tied to the actual paper over broad language that could describe many papers in the field.

## Track 1: Enrichment Quality Review

### Objective

Review new enrichment JSON files for consistency, grounding, and synthesis value.

### Review Checks

For each reviewed enrichment entry, confirm:

- `summary` is specific to the paper's actual contribution
- `why_it_matters` is useful at the vault level, not a generic statement of importance
- `method_setup` correctly identifies the paper type or research setup
- `key_claims` are concise, distinct, and non-redundant
- `limitations` contain real constraints rather than filler caveats
- `evaluates` entries are short, stable phrases
- unresolved comparison or dependency references are removed if evidence is weak

### Edit Rules

When patching a weak entry:

- shorten before expanding
- remove filler before rewriting content
- keep claims close to what the paper actually supports
- avoid adding speculative interpretation that is not grounded in the paper
- preserve schema and field names exactly

### Priority Order

Review in this order:

1. foundational systems papers
2. memory papers
3. benchmark and evaluation papers
4. broad surveys and conceptual papers

Rationale:

- foundational and memory papers are most likely to become synthesis anchors
- evaluation papers affect how other notes are interpreted
- surveys are useful, but a weak survey note usually creates less downstream damage than a weak foundational note

### Expected Output

- patched files in `paper_inbox/enrichment/`
- cleaner rerendered notes in `paper_notes/`

## Track 2: Unresolved Reference Resolution

### Objective

Convert unresolved title references into local links wherever the referenced paper already exists in the vault.

### Resolution Targets

Inspect unresolved relation fields produced by enrichment, especially:

- `builds_on_unresolved`
- `compares_to_unresolved`

### Resolution Procedure

For each unresolved reference:

1. inspect the unresolved title
2. normalize it using the existing deterministic title-matching rules
3. check whether a matching vault paper note already exists
4. if a strong match exists, rerender through `make ingest`
5. if no strong match exists, keep it unresolved

### Resolution Rules

- prefer exact matches or strongly normalized matches
- do not invent links from topic similarity or author overlap alone
- do not resolve against papers that are not already imported into the vault
- keep external works unresolved until they exist as local paper notes

### Expected Output

- fewer unresolved relation entries in rendered notes
- more local paper-to-paper navigation across existing notes

## Suggested Execution Sequence

Run cleanup in the following order:

1. review and patch the highest-value enrichment entries
2. rerun `make ingest`
3. inspect rendered notes for obvious generic filler or malformed sections
4. inspect unresolved reference counts and repeated unresolved titles
5. import obvious missing foundational papers only if the missing paper is clearly worth local inclusion
6. rerun `make ingest` again
7. spot-check the most important notes after rerender

## Acceptance Criteria

Cleanup is successful when:

- enriched notes read cleanly without obvious generic filler
- unresolved references are mostly limited to papers not yet present in the vault
- important papers gain more local cross-links
- no schema drift is introduced
- rerendering remains the only path used to update note projections

## Optional Follow-Ups

If this cleanup pattern becomes recurring, add lightweight support for it:

- a report of unresolved references by frequency
- a script to surface likely resolvable unresolved titles
- a reusable review checklist for future enrichment batches
- a small before/after metric on unresolved-reference counts

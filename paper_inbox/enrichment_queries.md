# Enrichment Queries

Use these fixed questions with `answer_pdf_queries` for approved papers:

1. What is the main contribution of this paper in 1-2 sentences?
2. Which paper type best fits this paper: survey, benchmark, system, position, or application?
3. What evaluation setting, benchmark, or task suite does this paper introduce or use?
4. What prior systems, methods, or baselines does it explicitly compare against?
5. What prior work does it explicitly build on?
6. What limitations do the authors describe or acknowledge?

Map the results into `paper_inbox/enrichment.example.json`.
Store referenced papers as plain titles in:
- `builds_on_unresolved`
- `compares_to_unresolved`

`make ingest` resolves those titles into local links when matching papers exist in the vault.

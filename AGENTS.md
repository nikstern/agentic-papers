Obsidian Vault

Purpose:
- Research vault for single-agent systems, multi-agent systems, memory, evaluation, and retrieval.

Stores:
- Referenced research papers
- Topic-level synthesis
- Parts of authored content

Core rules:
- Treat this repo as a grounded research memory and discussion substrate, not just a note archive.
- Prefer vault evidence over generic prior knowledge.
- Follow deterministic workflows for discovery, approval, import, enrichment, ingest, and rerender.
- Do not hand-edit generated paper summaries as source of truth.

Authoritative layers:
- `paper_inbox/papers.csv`: authoritative paper registry and lifecycle state
- `paper_inbox/enrichment/*.json`: authoritative extracted metadata and summaries
- `paper_notes/*.md`: generated notes with user-owned `## My Notes`
- `topic_maps/*.md`: synthesis hubs across related papers

Default research workflow:
1. Identify the question type:
   - exact paper-link lookup
   - corpus-level semantic question
   - narrow direct-note or topic-map lookup
2. Retrieve evidence from the vault before answering when retrieval is useful.
3. Answer from retrieved evidence, not from vague memory.
4. For critique or comparison answers, surface:
   - key claim
   - evidence setting or benchmark
   - main limitation
   - relevant comparison or baseline

Retrieval routing:
- Use structured relation lookup first for exact paper-link questions such as:
  - which paper evaluates X
  - which papers build on Y
  - what compares to Z
- Use Qdrant-backed retrieval by default for:
  - semantic questions
  - topic exploration
  - similarity search
  - critique prompts
  - broad comparison questions
- Fall back to direct note or topic-map reading when:
  - the question is narrow
  - the semantic index is stale or missing
  - retrieval would add unnecessary overhead

Relation sources:
- Prefer note frontmatter relations such as:
  - `evaluates`
  - `builds_on`
  - `compares_to`
- Exact relation answers may be incomplete if those links were not captured during enrichment.

Search workflow:
- Qdrant-backed search code lives under `search/`.
- Query the corpus through the provided CLIs rather than calling Qdrant directly:
  - `source .venv/bin/activate && python search/search_qdrant.py "<query>"`
    Use for raw semantic nearest-neighbor search over indexed sections.
  - `source .venv/bin/activate && python search/ask_corpus.py "<question>"`
    Use for grouped paper evidence and discussion-oriented retrieval.
- Useful filters:
  - `--topic memory-context`
  - `--type system`
  - `--year 2025`
  - `--limit 5`
- `search/ask_corpus.py` is the preferred entry point for exact paper-link questions because it uses hybrid relation lookup before semantic fallback.

Index maintenance:
- `make ingest` rerenders notes, refreshes the pending enrichment queue, and refreshes the search index.
- `make import-enrichment FILE=...` imports enrichment, rerenders notes, and refreshes the search index.
- `make enrich-pending` runs the local automatic enrichment loop when `OPENAI_API_KEY` is configured.
- `make ingest-and-enrich` runs the full local loop: ingest, queue enrichment, enrich, rerender, and reindex.
- Local embedded Qdrant is single-process; concurrent access should use a server deployment instead.

External papers:
- Use the `arxiv` MCP server for arXiv discovery and for downloading or reading paper content.
- Papers found outside the vault are not vault knowledge until they are imported, approved, and ingested.
- If a newly ingested paper is central to the current discussion, prefer enriching it before relying heavily on the generated note.

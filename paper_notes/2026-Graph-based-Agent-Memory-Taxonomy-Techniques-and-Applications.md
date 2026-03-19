---
paper_id: 14
title: "Graph-based Agent Memory: Taxonomy, Techniques, and Applications"
year: 2026
authors: "Yang et al."
url: "https://arxiv.org/abs/2602.05665"
paper_type: "survey"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "graph-based memory"
  - "structured retrieval"
  - "memory evolution mechanisms"
builds_on:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
compares_to: []
builds_on_unresolved:
  - "Knowledge Graphs"
  - "GraphRAG"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This survey studies graph-based agent memory as a structured memory paradigm for LLM agents, covering taxonomy, extraction, storage, retrieval, evolution, and applications.

# Why It Matters
It is a useful anchor for the structured-memory branch of the vault because it treats graphs as the key representation for relational, hierarchical, and evolving agent memory.

# Method / Setup
The paper surveys graph memory forms such as knowledge, temporal, hierarchical, and hybrid graphs, then analyzes graph-oriented retrieval and evolution methods across the memory lifecycle.

# Key Claims
- Graph-based memory offers a strong unifying representation for relational agent memory.
- Structured memory is increasingly necessary for long-horizon reasoning and self-improvement.
- Future progress depends on better graph quality, scalability, and trustworthy memory operations.

# Limitations
- The survey catalogs many graph techniques but does not validate a single new system.
- The implementation burden of graph memory can be high in practice.

# Connections
- [[Memory-Context]]
- `evaluates` graph-based memory
- `evaluates` structured retrieval
- `evaluates` memory evolution mechanisms
- `builds_on` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `builds_on_unresolved` Knowledge Graphs
- `builds_on_unresolved` GraphRAG

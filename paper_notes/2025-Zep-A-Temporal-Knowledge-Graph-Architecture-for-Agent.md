---
paper_id: 38
title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
year: 2025
authors: "Rasmussen et al."
url: "https://arxiv.org/abs/2501.13956"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "deep memory retrieval"
  - "long-term interactive memory"
  - "temporal knowledge graph memory"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
compares_to:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
builds_on_unresolved:
  - "GraphRAG"
  - "Retrieval-Augmented Generation"
compares_to_unresolved:
  - "full-conversation context"
  - "session summaries"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Zep introduces a temporally-aware knowledge graph memory layer for AI agents that fuses conversational and structured data, improving memory retrieval and temporal reasoning over prior memory systems.

# Why It Matters
It is a strong graph-memory systems paper for the vault because it explicitly positions itself against MemGPT and argues that temporal, structured memory can outperform flatter memory mechanisms on realistic retrieval tasks.

# Method / Setup
The system builds and updates a temporal knowledge graph through Graphiti, retrieves context using semantic, keyword, and graph traversal signals, and evaluates on the Deep Memory Retrieval benchmark and LongMemEval against MemGPT, full-conversation context, and session-summary baselines.

# Key Claims
- Temporal knowledge graphs can outperform MemGPT on deep memory retrieval tasks.
- Structured graph memory improves complex, enterprise-style long-term reasoning while reducing response latency.
- Combining semantic similarity, keyword search, and graph traversal yields stronger memory retrieval than flatter memory stores.

# Limitations
- The DMR benchmark is limited by small scale and single-turn fact retrieval, so it does not fully represent enterprise use cases.
- The system depends on substantial graph construction and retrieval infrastructure, which can raise deployment complexity.
- Performance on some LongMemEval settings remains model-sensitive and leaves room for further tuning.

# Connections
- [[Memory-Context]]
- `evaluates` deep memory retrieval
- `evaluates` long-term interactive memory
- `evaluates` temporal knowledge graph memory
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `compares_to` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `builds_on_unresolved` GraphRAG
- `builds_on_unresolved` Retrieval-Augmented Generation
- `compares_to_unresolved` full-conversation context
- `compares_to_unresolved` session summaries
<!-- GENERATED:END -->

## My Notes


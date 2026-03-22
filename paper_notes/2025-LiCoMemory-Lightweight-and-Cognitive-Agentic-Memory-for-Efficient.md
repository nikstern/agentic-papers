---
paper_id: 75
title: "LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning"
year: 2025
authors: "Huang et al."
url: "https://arxiv.org/abs/2511.01448"
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
  - "LongMemEval"
  - "LoCoMo"
  - "multi-session reasoning"
  - "temporal reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Zep"
  - "Mem0"
  - "A-Mem"
compares_to_unresolved:
  - "Zep"
  - "Mem0"
  - "MemOS"
  - "A-Mem"
  - "MemoryBank"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
LiCoMemory introduces CogniGraph, a lightweight hierarchical memory graph for long-term LLM reasoning that separates session summaries, entity-relation structure, and source chunks. It aims to support real-time updates, low-latency retrieval, and temporally aware reasoning across long conversational histories.

# Why It Matters
It is directly relevant to efficient external memory design because it focuses on lightweight structure, retrieval coherence, and real-time memory operations.

# Method / Setup
Agent memory framework with a three-layer CogniGraph over session summaries, entity-relation nodes, and dialogue chunks, combined with hierarchical retrieval and unified reranking over semantic relevance and temporal recency.

# Key Claims
- Decoupling semantic storage from graph structure reduces redundancy and makes graph-based memory updates much cheaper.
- Hierarchical retrieval over summaries, triples, and source chunks improves long-term reasoning coherence compared with flatter memory systems.
- Temporal-aware reranking materially helps on multi-session and temporal reasoning tasks.

# Limitations
- The current system is limited to text-based conversational memory rather than multimodal memory.
- Graph construction and refinement still rely on LLM calls, which can become costly as memory grows.

# Connections
- [[Memory-Context]]
- `evaluates` LongMemEval
- `evaluates` LoCoMo
- `evaluates` multi-session reasoning
- `evaluates` temporal reasoning
- `builds_on_unresolved` Zep
- `builds_on_unresolved` Mem0
- `builds_on_unresolved` A-Mem
- `compares_to_unresolved` Zep
- `compares_to_unresolved` Mem0
- `compares_to_unresolved` MemOS
- `compares_to_unresolved` A-Mem
- `compares_to_unresolved` MemoryBank
<!-- GENERATED:END -->

## My Notes


---
paper_id: 44
title: "Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation"
year: 2026
authors: "Hu et al."
url: "https://arxiv.org/abs/2602.02007"
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
  - "agent memory retrieval"
  - "context redundancy reduction"
  - "token-efficient long-horizon QA"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
compares_to:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
builds_on_unresolved:
  - "Retrieval-Augmented Generation"
  - "MemoryOS"
compares_to_unresolved:
  - "Naive RAG"
  - "MemoryOS"
  - "LightMem"
  - "Nemori"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
xMemory argues that standard RAG is the wrong retrieval abstraction for agent memory and replaces it with hierarchical memory construction plus adaptive evidence aggregation.

# Why It Matters
This is one of the most directly relevant 2026 papers for context engineering because it focuses on how to assemble compact, non-redundant context from long interaction histories.

# Method / Setup
The method builds a hierarchy of messages, episodes, semantic units, and themes, then performs representative selection and uncertainty-gated expansion during retrieval; it is evaluated on LoCoMo and PerLTQA with multiple LLM backbones.

# Key Claims
- Agent memory retrieval should optimize for anti-redundancy and evidence integrity rather than reuse standard top-k RAG.
- Hierarchical decoupling and aggregation improve answer quality while reducing token usage.
- Adaptive uncertainty-based expansion yields denser, more answer-sufficient context than naive retrieval or generic pruning.

# Limitations
- The hierarchy and adaptive retrieval strategy introduce more system complexity than simple vector-store pipelines.
- The method is evaluated mainly on conversational and personal-memory benchmarks.
- Application-level privacy and memory governance are left to downstream systems.

# Connections
- [[Memory-Context]]
- `evaluates` agent memory retrieval
- `evaluates` context redundancy reduction
- `evaluates` token-efficient long-horizon QA
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `builds_on` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `builds_on_unresolved` Retrieval-Augmented Generation
- `builds_on_unresolved` MemoryOS
- `compares_to_unresolved` Naive RAG
- `compares_to_unresolved` MemoryOS
- `compares_to_unresolved` LightMem
- `compares_to_unresolved` Nemori
<!-- GENERATED:END -->

## My Notes


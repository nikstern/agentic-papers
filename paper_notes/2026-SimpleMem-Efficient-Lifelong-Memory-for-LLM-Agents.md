---
paper_id: 39
title: "SimpleMem: Efficient Lifelong Memory for LLM Agents"
year: 2026
authors: "Liu et al."
url: "https://arxiv.org/abs/2601.02553"
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
  - "lifelong conversational memory"
  - "memory efficiency"
  - "temporal and multi-hop reasoning"
builds_on: []
compares_to:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
builds_on_unresolved:
  - "Complementary Learning Systems"
compares_to_unresolved:
  - "LoCoMo"
  - "ReadAgent"
  - "MemoryBank"
  - "LightMem"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
SimpleMem proposes an efficient lifelong memory framework for LLM agents that compresses, normalizes, consolidates, and adaptively retrieves conversational memory rather than storing raw history or relying on repeated planning loops.

# Why It Matters
It is a high-value follow-on systems paper because it directly compares against MemGPT, Mem0, and A-MEM while making a stronger efficiency argument around semantic compression and adaptive retrieval.

# Method / Setup
The framework combines entropy-aware filtering, structured memory unit normalization, recursive consolidation, and query-aware retrieval, and evaluates on the LoCoMo benchmark across multiple reasoning types and model backbones against LoCoMo, ReadAgent, MemoryBank, MemGPT, A-MEM, LightMem, and Mem0.

# Key Claims
- Semantic compression can greatly reduce token and latency costs without sacrificing long-term memory quality.
- SimpleMem outperforms strong baselines such as Mem0 and MemGPT on LoCoMo-style long-horizon conversational tasks.
- Structured normalization and consolidation are especially helpful for temporal and multi-hop reasoning.

# Limitations
- The evaluation is centered on dialogue-heavy long-term memory settings rather than broader tool-using or multimodal agent environments.
- The method depends on multiple coordinated stages, which increases systems complexity relative to simpler memory stores.
- The reported gains are strongest on benchmarked conversational workloads, so broader real-world generalization still needs validation.

# Connections
- [[Memory-Context]]
- `evaluates` lifelong conversational memory
- `evaluates` memory efficiency
- `evaluates` temporal and multi-hop reasoning
- `compares_to` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on_unresolved` Complementary Learning Systems
- `compares_to_unresolved` LoCoMo
- `compares_to_unresolved` ReadAgent
- `compares_to_unresolved` MemoryBank
- `compares_to_unresolved` LightMem
<!-- GENERATED:END -->

## My Notes


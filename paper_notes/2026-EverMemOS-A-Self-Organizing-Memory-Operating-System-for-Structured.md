---
paper_id: 42
title: "EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning"
year: 2026
authors: "Hu et al."
url: "https://arxiv.org/abs/2601.02163"
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
  - "memory-augmented reasoning"
  - "long-horizon conversational memory"
  - "profile consistency and temporal reasoning"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
  - "[[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]"
compares_to:
  - "[[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]"
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
builds_on_unresolved:
  - "Generative Agents"
compares_to_unresolved:
  - "MemOS"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
EverMemOS proposes a memory operating system that converts interaction traces into structured memory cells, consolidates them into higher-level scenes, and reconstructs task-specific context at retrieval time.

# Why It Matters
It is a strong context-engineering paper because it frames memory as lifecycle management and consolidation rather than flat storage plus top-k search.

# Method / Setup
The system builds MemCells with episodes, atomic facts, foresight, and metadata, clusters them into MemScenes, and uses reconstructive retrieval with sufficiency checks; it is evaluated on LoCoMo, LongMemEval, and PersonaMem-v2.

# Key Claims
- Lifecycle-based consolidation produces better long-horizon reasoning than fragmented memory stores.
- Structured memory scenes improve multi-hop and temporal reasoning by integrating evidence before retrieval.
- Profile-style consolidation helps preserve user traits and temporary states more reliably than episode-only memory.

# Limitations
- The system has multiple LLM-mediated stages, which adds latency and engineering overhead.
- Most evidence comes from conversational and memory-augmented reasoning benchmarks rather than multimodal or tool-heavy settings.
- The approach still relies on the quality of segmentation and consolidation prompts.

# Connections
- [[Memory-Context]]
- `evaluates` memory-augmented reasoning
- `evaluates` long-horizon conversational memory
- `evaluates` profile consistency and temporal reasoning
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `builds_on` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on` [[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]
- `compares_to` [[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]
- `compares_to` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `compares_to` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on_unresolved` Generative Agents
- `compares_to_unresolved` MemOS
<!-- GENERATED:END -->

## My Notes


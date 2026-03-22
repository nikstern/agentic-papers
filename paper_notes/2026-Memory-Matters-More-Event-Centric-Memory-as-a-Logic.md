---
paper_id: 43
title: "Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning"
year: 2026
authors: "Hu et al."
url: "https://arxiv.org/abs/2601.04726"
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
  - "event-structured agent memory"
  - "multi-hop and temporal reasoning"
  - "logic-aware memory retrieval"
builds_on:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
compares_to:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
builds_on_unresolved:
  - "Event Segmentation Theory"
  - "HippoRAG"
  - "CAM"
compares_to_unresolved:
  - "HippoRAG"
  - "CAM"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
CompassMem organizes agent memory as event units linked by logical relations and lets the agent actively traverse that graph to retrieve evidence for reasoning.

# Why It Matters
It advances context engineering by showing that memory structure and retrieval path matter as much as storing more context.

# Method / Setup
The framework segments experience into events, extracts temporal and causal relations into an event graph, and uses planner and explorer modules for multi-path memory search; evaluation is on LoCoMo and NarrativeQA.

# Key Claims
- Event-centric memory graphs outperform flat retrieval and weaker graph memories on multi-hop and temporal reasoning.
- Logic-aware navigation turns memory into an active reasoning map rather than a passive store.
- Topic-aware localization and query refinement improve evidence discovery for long-context tasks.

# Limitations
- The pipeline depends on LLM-based event segmentation and relation extraction, which can introduce noise.
- The multi-agent search process increases token use relative to simpler retrieval systems.
- Results are concentrated on narrative and conversational reasoning settings.

# Connections
- [[Memory-Context]]
- `evaluates` event-structured agent memory
- `evaluates` multi-hop and temporal reasoning
- `evaluates` logic-aware memory retrieval
- `builds_on` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on_unresolved` Event Segmentation Theory
- `builds_on_unresolved` HippoRAG
- `builds_on_unresolved` CAM
- `compares_to_unresolved` HippoRAG
- `compares_to_unresolved` CAM
<!-- GENERATED:END -->

## My Notes


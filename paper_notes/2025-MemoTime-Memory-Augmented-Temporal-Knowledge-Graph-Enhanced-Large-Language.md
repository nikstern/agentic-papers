---
paper_id: 74
title: "MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning"
year: 2025
authors: "Tan et al."
url: "https://arxiv.org/abs/2510.13614"
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
  - "MultiTQ"
  - "TimeQuestions"
  - "temporal knowledge graph question answering"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Paths-over-graph: Knowledge graph empowered large language model reasoning"
compares_to_unresolved:
  - "TempAgent"
  - "GenTKGQA"
  - "TimeR4"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
MemoTime augments LLM reasoning over temporal knowledge graphs with hierarchical temporal decomposition, toolkit-guided retrieval, and a reusable experience memory. It is designed to answer complex temporal questions involving multiple entities, operators, and evolving event sequences more faithfully.

# Why It Matters
It is relevant if you care about memory as a support for temporally grounded reasoning rather than only conversational recall.

# Method / Setup
System for temporal knowledge graph QA that combines temporal grounding, a Tree-of-Time hierarchical controller, hybrid graph-plus-embedding temporal retrieval, temporal pruning, and an adaptive experience pool for reuse of successful reasoning traces.

# Key Claims
- Structured temporal decomposition and monotonic reasoning improve faithfulness on multi-hop temporal question answering.
- Experience memory helps stabilize toolkit selection and reuse successful temporal reasoning traces over time.
- The framework improves temporal QA performance across multiple LLM backbones without requiring fine-tuning.

# Limitations
- The method is specialized to temporal knowledge graph reasoning rather than general long-term agent memory.
- Its runtime still depends on a fairly involved retrieval and recursive reasoning pipeline.

# Connections
- [[Memory-Context]]
- `evaluates` MultiTQ
- `evaluates` TimeQuestions
- `evaluates` temporal knowledge graph question answering
- `builds_on_unresolved` Paths-over-graph: Knowledge graph empowered large language model reasoning
- `compares_to_unresolved` TempAgent
- `compares_to_unresolved` GenTKGQA
- `compares_to_unresolved` TimeR4
<!-- GENERATED:END -->

## My Notes


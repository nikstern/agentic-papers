---
paper_id: 18
title: "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems"
year: 2025
authors: "Zhang et al."
url: "https://arxiv.org/abs/2506.07398"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "multi-agent reasoning"
  - "embodied action"
  - "game tasks"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "MemoryBank"
  - "Generative Agents"
  - "Voyager"
compares_to_unresolved:
  - "MetaGPT"
  - "ChatDev"
relations: []
source: "alphaxiv-mcp"
---

# Summary
G-Memory introduces a hierarchical memory architecture for multi-agent systems with interaction graphs, query graphs, and insight graphs to support self-evolving collaboration over time.

# Why It Matters
It is a high-value anchor for shared multi-agent memory because it explicitly treats memory as a hierarchical, MAS-specific substrate rather than a single-agent add-on.

# Method / Setup
G-Memory retrieves relevant historical queries, traverses upward to abstract insights and downward to condensed interaction traces, then updates the memory hierarchy after each task; it is evaluated across multiple multi-agent frameworks and task domains.

# Key Claims
- Hierarchical memory improves multi-agent performance across reasoning, embodied action, and game tasks.
- Both high-level insight memory and fine-grained interaction memory matter.
- The design improves results without excessive token overhead compared with alternative memory designs.

# Limitations
- The paper still evaluates in benchmark settings rather than large enterprise deployments.
- Safety and robustness concerns remain if the underlying models or memories are compromised.

# Connections
- [[Memory Context]]
- `evaluates` multi-agent reasoning
- `evaluates` embodied action
- `evaluates` game tasks
- `builds_on_unresolved` MemoryBank
- `builds_on_unresolved` Generative Agents
- `builds_on_unresolved` Voyager
- `compares_to_unresolved` MetaGPT
- `compares_to_unresolved` ChatDev

---
paper_id: 9
title: "A Survey on the Memory Mechanism of Large Language Model based Agents"
year: 2024
authors: "Zhang et al."
url: "https://arxiv.org/abs/2404.13501"
paper_type: "survey"
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
  - "agent memory taxonomies"
  - "memory dynamics"
  - "memory system design"
builds_on:
  - "[[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]"
compares_to: []
builds_on_unresolved:
  - "Reflexion"
  - "RAG"
  - "Generative Agents"
compares_to_unresolved:
  - "MemBench"
  - "LoCoMo"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey reviews memory mechanisms in LLM-based agents, organizing the area around memory forms, functions, and dynamics rather than a simple short-term versus long-term split.

# Why It Matters
It is a strong reference point for the vault’s memory line because it treats agent memory as an evolving systems problem rather than a single retrieval trick.

# Method / Setup
The paper formalizes agent memory, distinguishes it from generic RAG and context engineering, and surveys token-level, parametric, and latent memory forms together with formation, retrieval, and evolution processes.

# Key Claims
- Agent memory should be analyzed by representational form, cognitive function, and lifecycle dynamics together.
- Memory is a core module for long-horizon, adaptive agent behavior.
- Future work needs better multimodal, trustworthy, and shared memory systems.

# Limitations
- As a survey, it synthesizes the field but does not validate a new memory mechanism itself.
- The area is moving quickly, so concrete implementations may age faster than the conceptual taxonomy.

# Connections
- [[Memory-Context]]
- `evaluates` agent memory taxonomies
- `evaluates` memory dynamics
- `evaluates` memory system design
- `builds_on` [[2023-MemGPT-Towards-LLMs-as-Operating-Systems]]
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` RAG
- `builds_on_unresolved` Generative Agents
- `compares_to_unresolved` MemBench
- `compares_to_unresolved` LoCoMo
<!-- GENERATED:END -->

## My Notes


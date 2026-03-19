---
paper_id: 8
title: "A-MEM: Agentic Memory for LLM Agents"
year: 2025
authors: "Xu et al."
url: "https://arxiv.org/abs/2502.12110"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "long-term conversational memory"
  - "multi-hop reasoning"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "MemGPT"
  - "MemoryBank"
  - "ReadAgent"
  - "LoCoMo"
relations: []
source: "alphaxiv-mcp"
---

# Summary
A-MEM is a memory system for LLM agents that dynamically organizes notes, links related memories, and evolves existing memory entries over time.

# Why It Matters
It is a strong systems anchor for agentic memory because it moves beyond static storage and retrieval toward adaptive memory organization.

# Method / Setup
The system constructs structured notes, retrieves top-k related memories, uses LLMs to generate links, and updates prior memories through memory evolution; the paper evaluates this on long-term conversational tasks such as LoCoMo and DialSim against memory baselines.

# Key Claims
- Dynamic linking and memory evolution improve long-term agent performance.
- A-MEM outperforms memory baselines especially on multi-hop reasoning tasks.
- The architecture reduces token usage substantially relative to some baselines.

# Limitations
- The evaluation is concentrated on conversational long-term memory settings.
- The paper leaves multimodal memory and broader open-world deployment as future work.

# Connections
- [[Memory Context]]
- `evaluates` long-term conversational memory
- `evaluates` multi-hop reasoning
- `compares_to_unresolved` MemGPT
- `compares_to_unresolved` MemoryBank
- `compares_to_unresolved` ReadAgent
- `compares_to_unresolved` LoCoMo

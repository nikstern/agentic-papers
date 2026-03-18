---
paper_id: 20
title: Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory
year: 2025
authors: Yuen et al.
url: https://arxiv.org/abs/2508.08997
paper_type: system
primary_topic: memory-context
secondary_topics: []
status: ingested
tags: [papers, memory-context]
evaluates:
  - structured planning
  - collaborative system design
builds_on:
  - [[2023 - MemGPT Towards LLMs as Operating Systems]]
compares_to:
  - [[2025 - G-Memory Tracing Hierarchical Memory for Multi-Agent Systems]]
builds_on_unresolved:
  - Retrieval-Augmented Generation
compares_to_unresolved: []
relations: []
source: alphaxiv-mcp
---

# Summary
Intrinsic Memory Agents equips each agent in a multi-agent LLM system with its own structured, role-specific memory that is updated from its own outputs to preserve perspective and procedural consistency.

# Why It Matters
It is a strong systems paper for heterogeneous shared-memory settings because it argues against homogeneous memory and shows the value of structured contextual memory per agent.

# Method / Setup
The method defines role-specific JSON memory templates, injects those memories into agent context, and updates memory after each turn based on the agent's own output; it is evaluated on PDDL planning and a collaborative data-pipeline design task.

# Key Claims
- Agent-specific structured memory improves collaborative task quality.
- The approach reduces role drift and preserves procedural coherence.
- Higher-quality outputs are achieved without needing more conversation turns.

# Limitations
- Memory templates are manually specified, which limits adaptability.
- The approach uses more tokens per conversation than simpler baselines.

# Connections
- [[Memory Context]]
- `evaluates` structured planning
- `evaluates` collaborative system design
- `builds_on` [[2023 - MemGPT Towards LLMs as Operating Systems]]
- `compares_to` [[2025 - G-Memory Tracing Hierarchical Memory for Multi-Agent Systems]]
- `builds_on_unresolved` Retrieval-Augmented Generation

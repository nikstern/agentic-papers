---
paper_id: 41
title: "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents"
year: 2026
authors: "Yu et al."
url: "https://arxiv.org/abs/2601.01885"
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
  - "long-horizon agent memory management"
  - "reinforcement-learned context control"
  - "memory quality and task performance"
builds_on:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
  - "[[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]"
compares_to:
  - "[[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]"
  - "[[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]"
builds_on_unresolved:
  - "LangMem"
compares_to_unresolved:
  - "No-Memory"
  - "LangMem"
  - "Mem0g"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
AgeMem turns long-term and short-term memory management into explicit tool actions that are optimized together inside the agent policy rather than bolted on as separate heuristics.

# Why It Matters
It is one of the clearest 2026 papers treating context engineering as an end-to-end control problem, not just a retrieval module.

# Method / Setup
The paper exposes memory operations such as add, update, delete, retrieve, summarize, and filter as agent tools and trains the policy with a three-stage reinforcement learning setup across long-horizon benchmarks including ALFWorld, SciWorld, PDDL, BabyAI, and HotpotQA.

# Key Claims
- Unified management of long-term and short-term memory improves long-horizon agent performance over systems that optimize the two separately.
- Reinforcement learning can teach an agent when to store, retrieve, summarize, or discard context rather than relying on fixed rules.
- The learned policy improves both answer quality and memory quality across diverse tasks.

# Limitations
- The method depends on multi-stage reinforcement learning, which increases training cost and implementation complexity.
- The evaluation emphasizes benchmarked long-horizon tasks rather than broad real-world deployments.
- Interpretability and governance of learned forgetting or deletion decisions remain limited.

# Connections
- [[Memory-Context]]
- `evaluates` long-horizon agent memory management
- `evaluates` reinforcement-learned context control
- `evaluates` memory quality and task performance
- `builds_on` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `builds_on` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on` [[2025-Zep-A-Temporal-Knowledge-Graph-Architecture-for-Agent]]
- `compares_to` [[2025-A-MEM-Agentic-Memory-for-LLM-Agents]]
- `compares_to` [[2025-Mem0-Building-Production-Ready-AI-Agents-with-Scalable-Long-Term]]
- `builds_on_unresolved` LangMem
- `compares_to_unresolved` No-Memory
- `compares_to_unresolved` LangMem
- `compares_to_unresolved` Mem0g
<!-- GENERATED:END -->

## My Notes


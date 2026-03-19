---
paper_id: 6
title: "Multi-Agent Collaboration Mechanisms: A Survey of LLMs"
year: 2025
authors: "Tran et al."
url: "https://arxiv.org/abs/2501.06322"
paper_type: "survey"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "collaboration mechanisms"
  - "coordination protocols"
  - "multi-agent organizational structures"
builds_on:
  - "[[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]"
  - "[[2023 - CAMEL Communicative Agents for Mind Exploration of Large]]"
compares_to: []
builds_on_unresolved:
  - "AutoGen"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This survey studies collaboration mechanisms in LLM-based multi-agent systems through the lenses of collaboration type, organizational structure, strategy, and coordination protocol.

# Why It Matters
It is directly useful for the vault because it treats collaboration itself as the object of study, making it easier to compare design choices across agent systems.

# Method / Setup
The paper surveys cooperative, competitive, and coopetitive systems, analyzes centralized, decentralized, and hierarchical structures, and reviews communication and handoff mechanisms across application domains.

# Key Claims
- Collaboration design is a first-class systems variable for multi-agent performance.
- Different task settings call for different collaboration structures and strategies.
- Evaluation of multi-agent systems needs to account for coordination behavior, not just final outputs.

# Limitations
- The paper is broad and therefore higher level than domain-specific system analyses.
- It emphasizes conceptual organization over benchmarked empirical comparison.

# Connections
- [[LLM Multi-Agent Systems]]
- `evaluates` collaboration mechanisms
- `evaluates` coordination protocols
- `evaluates` multi-agent organizational structures
- `builds_on` [[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]
- `builds_on` [[2023 - CAMEL Communicative Agents for Mind Exploration of Large]]
- `builds_on_unresolved` AutoGen

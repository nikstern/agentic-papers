---
paper_id: 3
title: "ChatDev: Communicative Agents for Software Development"
year: 2023
authors: "Qian et al."
url: "https://arxiv.org/abs/2307.07924"
paper_type: "system"
primary_topic: "software-agents"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "software-agents"
evaluates:
  - "software prototyping"
  - "code executability"
  - "multi-agent communication quality"
builds_on:
  - "[[2023 - CAMEL Communicative Agents for Mind Exploration of Large]]"
  - "[[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]"
compares_to:
  - "[[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]"
builds_on_unresolved: []
compares_to_unresolved:
  - "GPT-Engineer"
relations: []
source: "manual"
---

# Summary
ChatDev casts software development as a chat chain in which specialized LLM agents collaborate across design, coding, and testing through multi-turn dialogue and communicative dehallucination.

# Why It Matters
It is an early influential multi-agent software engineering system that made communication patterns, role prompting, and iterative debugging central design variables rather than implementation details.

# Method / Setup
The framework organizes a software company around specialized roles, uses phase-specific chat chains, adds communicative dehallucination for clarification and debugging, and evaluates outputs on a software requirement dataset against single-agent and multi-agent baselines.

# Key Claims
- Role-specialized multi-agent chat improves end-to-end software development quality.
- Communicative dehallucination reduces common coding mistakes and missing details.
- Structured multi-phase collaboration outperforms both single-agent coding and more rigid multi-agent baselines.

# Limitations
- The framework is still most credible for prototype-level software rather than production systems.
- Multi-agent coordination raises token and latency costs relative to single-agent approaches.

# Connections
- [[Software Agents]]
- `evaluates` software prototyping
- `evaluates` code executability
- `evaluates` multi-agent communication quality
- `builds_on` [[2023 - CAMEL Communicative Agents for Mind Exploration of Large]]
- `builds_on` [[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]
- `compares_to` [[2023 - MetaGPT Meta Programming for A Multi-Agent Collaborative Framework]]
- `compares_to_unresolved` GPT-Engineer

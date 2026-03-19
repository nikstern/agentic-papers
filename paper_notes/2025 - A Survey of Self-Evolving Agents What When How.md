---
paper_id: 27
title: "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence"
year: 2025
authors: "Xu et al."
url: "https://arxiv.org/abs/2507.21046"
paper_type: "survey"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "self-evolving agents"
  - "adaptation mechanisms"
  - "agent lifecycle design"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "lifelong learning"
  - "curriculum learning"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This survey organizes the field of self-evolving agents around what evolves, when it evolves, how it evolves, and where those mechanisms matter in practice.

# Why It Matters
It is one of the clearest references in the vault for moving from static agents toward agents that adapt their models, memory, tools, and architecture over time.

# Method / Setup
The paper surveys self-evolution across models, context, tools, and architecture, distinguishes intra-test-time from inter-test-time adaptation, and compares reward-based, imitation-based, and population-based evolution strategies.

# Key Claims
- Self-evolution should be treated as a first-class agent design paradigm rather than a minor feature.
- Agent evolution spans much more than model fine-tuning alone.
- Evaluation of self-evolving agents needs to measure adaptivity, retention, generalization, efficiency, and safety together.

# Limitations
- The field is young, so many proposed directions are ahead of standardized benchmarks.
- As a survey, it provides a roadmap rather than a single validated system.

# Connections
- [[LLM Multi-Agent Systems]]
- `evaluates` self-evolving agents
- `evaluates` adaptation mechanisms
- `evaluates` agent lifecycle design
- `builds_on_unresolved` lifelong learning
- `builds_on_unresolved` curriculum learning

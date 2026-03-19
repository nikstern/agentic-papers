---
paper_id: 12
title: "How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior"
year: 2025
authors: "Xiong et al."
url: "https://arxiv.org/abs/2505.16067"
paper_type: "application"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "memory management policies"
  - "experience replay in agents"
  - "long-term agent robustness"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This empirical study examines how memory addition and deletion policies affect long-term LLM agent behavior, especially when agents learn from their own imperfect trajectories.

# Why It Matters
It adds hard evidence to the memory discussion by showing that memory management policy can materially improve or degrade agent performance over time.

# Method / Setup
The paper studies synthetic and real agents under different memory addition and deletion strategies, analyzes retrieval behavior, and evaluates effects under task shifts and memory constraints.

# Key Claims
- LLM agents exhibit an experience-following property in which retrieved experiences strongly shape future outputs.
- Poor memory curation causes error propagation and misaligned experience replay.
- Reliable evaluators and selective deletion improve long-term agent performance.

# Limitations
- The results depend on the quality of trajectory evaluators.
- The tasks are diverse but still only sample a subset of possible agent settings.

# Connections
- [[Memory Context]]
- `evaluates` memory management policies
- `evaluates` experience replay in agents
- `evaluates` long-term agent robustness

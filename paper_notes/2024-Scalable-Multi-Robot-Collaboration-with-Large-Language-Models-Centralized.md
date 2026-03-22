---
paper_id: 66
title: "Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems?"
year: 2024
authors: "Chen et al."
url: "https://arxiv.org/abs/2309.15943"
paper_type: "system"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "multi-robot task planning"
  - "centralized vs decentralized coordination"
  - "warehouse-style coordination tasks"
  - "3d multi-robot manipulation"
builds_on:
  - "[[2023-Task-and-Motion-Planning-with-Large-Language-Models]]"
compares_to: []
builds_on_unresolved:
  - "LLM-based multi-robot planning"
  - "iterative re-prompting with state feedback"
compares_to_unresolved:
  - "decentralized multi-agent system"
  - "centralized multi-agent system"
  - "hybrid multi-agent system 1"
  - "hybrid multi-agent system 2"
  - "GPT-3.5"
  - "GPT-4"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper studies the scalability of LLM-based multi-robot planning by comparing centralized, decentralized, and hybrid communication frameworks for cooperative task planning.

# Why It Matters
It is one of the clearest systems papers on the architecture tradeoff between centralized and decentralized LLM coordination in multi-robot settings, with an explicit focus on token efficiency and scaling.

# Method / Setup
The authors evaluate four LLM planning frameworks across multiple warehouse-style 2D environments and a 3D manipulation setting, measuring task success, plan efficiency, API usage, and token consumption.

# Key Claims
- Hybrid centralized-decentralized planning scales better than fully decentralized dialogue or fully centralized planning alone.
- State-action history is more useful than full dialogue history for preserving planning quality under token constraints.
- Stronger underlying LLMs materially improve multi-robot coordination performance.

# Limitations
- The study is still limited to simulated tasks rather than real-world large-scale robot deployments.
- Performance depends on prompt design, verifier structure, and the quality of the underlying LLM.
- The framework focuses on iterative task planning and does not solve low-level control or perception end to end.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` multi-robot task planning
- `evaluates` centralized vs decentralized coordination
- `evaluates` warehouse-style coordination tasks
- `evaluates` 3d multi-robot manipulation
- `builds_on` [[2023-Task-and-Motion-Planning-with-Large-Language-Models]]
- `builds_on_unresolved` LLM-based multi-robot planning
- `builds_on_unresolved` iterative re-prompting with state feedback
- `compares_to_unresolved` decentralized multi-agent system
- `compares_to_unresolved` centralized multi-agent system
- `compares_to_unresolved` hybrid multi-agent system 1
- `compares_to_unresolved` hybrid multi-agent system 2
- `compares_to_unresolved` GPT-3.5
- `compares_to_unresolved` GPT-4
<!-- GENERATED:END -->

## My Notes


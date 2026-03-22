---
paper_id: 62
title: "A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration"
year: 2023
authors: "Liu et al."
url: "https://arxiv.org/abs/2310.02170"
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
  - "multi-agent collaboration"
  - "code generation"
  - "decision making"
  - "general reasoning"
  - "arithmetic reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "CAMEL"
  - "AgentVerse"
  - "LLM Debate"
compares_to_unresolved:
  - "CAMEL"
  - "AgentVerse"
  - "LATS"
  - "Reflexion"
  - "BOLAA"
  - "LLM-Blender"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
DyLAN frames multi-agent LLM collaboration as a dynamic agent network where agents are selected, ranked, and re-formed during inference instead of being fixed from the start.

# Why It Matters
It is an important systems paper for adaptive multi-agent coordination because it treats team composition itself as an optimization problem rather than a static design choice.

# Method / Setup
The method models collaboration as temporal feed-forward networks, introduces an unsupervised agent-importance score for team optimization, and evaluates performance on code generation, decision making, general reasoning, and arithmetic reasoning tasks.

# Key Claims
- Task-oriented agent selection improves multi-agent performance over static teams.
- Dynamic team reformation can improve both accuracy and efficiency by filtering weak contributors during inference.
- A small optimized team can outperform a larger unfiltered team.

# Limitations
- The method depends on the quality of agent ranking and importance estimation.
- The evaluation focuses on text-based reasoning and coding tasks rather than embodied settings.
- Its dynamic orchestration adds coordination overhead compared with simpler fixed-agent baselines.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` multi-agent collaboration
- `evaluates` code generation
- `evaluates` decision making
- `evaluates` general reasoning
- `evaluates` arithmetic reasoning
- `builds_on_unresolved` CAMEL
- `builds_on_unresolved` AgentVerse
- `builds_on_unresolved` LLM Debate
- `compares_to_unresolved` CAMEL
- `compares_to_unresolved` AgentVerse
- `compares_to_unresolved` LATS
- `compares_to_unresolved` Reflexion
- `compares_to_unresolved` BOLAA
- `compares_to_unresolved` LLM-Blender
<!-- GENERATED:END -->

## My Notes


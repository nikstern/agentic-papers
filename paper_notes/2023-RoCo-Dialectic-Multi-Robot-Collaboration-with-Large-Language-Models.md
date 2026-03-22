---
paper_id: 61
title: "RoCo: Dialectic Multi-Robot Collaboration with Large Language Models"
year: 2023
authors: "Mandi et al."
url: "https://arxiv.org/abs/2307.04738"
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
  - "multi-robot collaboration"
  - "human-robot collaboration"
  - "embodied task planning"
  - "RoCoBench"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "SayCan"
  - "Inner Monologue"
  - "task and motion planning"
compares_to_unresolved:
  - "oracle planner"
  - "direct waypoints"
  - "hard-coded waypoints"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
RoCo proposes a large-language-model-driven framework for multi-robot collaboration in which agents coordinate through dialogue, generate subtask plans with waypoint hints, and hand off execution to motion planning.

# Why It Matters
It is an early embodied multi-agent systems paper that grounds LLM coordination in real robot collaboration constraints rather than only text-based interaction.

# Method / Setup
The paper introduces the RoCo framework and the RoCoBench benchmark, evaluates robot-robot and human-robot collaboration tasks, and compares dialogue-guided planning and waypoint generation against simpler planning baselines.

# Key Claims
- LLM-mediated dialogue can support flexible multi-robot coordination without task-specific training.
- LLM-generated waypoint suggestions can improve planning for complex placement and collision-heavy manipulation steps.
- The framework adapts across task semantics, workspace overlap, and heterogeneous agent capabilities.

# Limitations
- Performance depends on perception quality and can break down when object detection is wrong.
- The system has only been demonstrated with small teams and limited task families.
- LLM spatial reasoning can still generate implausible or suboptimal paths in harder scenarios.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` multi-robot collaboration
- `evaluates` human-robot collaboration
- `evaluates` embodied task planning
- `evaluates` RoCoBench
- `builds_on_unresolved` SayCan
- `builds_on_unresolved` Inner Monologue
- `builds_on_unresolved` task and motion planning
- `compares_to_unresolved` oracle planner
- `compares_to_unresolved` direct waypoints
- `compares_to_unresolved` hard-coded waypoints
<!-- GENERATED:END -->

## My Notes


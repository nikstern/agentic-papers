---
paper_id: 64
title: "Task and Motion Planning with Large Language Models for Object Rearrangement"
year: 2023
authors: "Ding et al."
url: "https://arxiv.org/abs/2303.06247"
paper_type: "system"
primary_topic: "software-agents"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "software-agents"
evaluates:
  - "object rearrangement"
  - "task and motion planning"
  - "table-setting tasks"
  - "human preference over arrangements"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "GROP"
  - "Task and Motion Planning"
compares_to_unresolved:
  - "Task Planning with Random Arrangement"
  - "LLM-based Arrangement and Task Planning"
  - "GROP"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper combines large language model commonsense with task and motion planning to generate semantically valid and physically executable object rearrangement plans from underspecified natural-language requests.

# Why It Matters
It is a strong embodied systems paper because it shows how LLM commonsense can be grounded into precise geometric placements and robot planning rather than only high-level action lists.

# Method / Setup
The method queries an LLM for symbolic and geometric object relations, filters candidate arrangements for logical and physical consistency, and then uses task-motion planning to optimize execution in object rearrangement tasks.

# Key Claims
- LLMs can provide useful commonsense priors for underspecified object arrangement tasks.
- Combining LLM-derived semantic structure with task-motion planning improves both arrangement quality and execution efficiency.
- The approach can produce human-preferred arrangements in embodied rearrangement settings.

# Limitations
- The method depends on LLM outputs that can be inconsistent without additional logical filtering.
- It focuses on a constrained family of rearrangement tasks rather than general embodied manipulation.
- Physical success still depends on downstream perception and planning robustness.

# Connections
- [[Software-Agents]]
- `evaluates` object rearrangement
- `evaluates` task and motion planning
- `evaluates` table-setting tasks
- `evaluates` human preference over arrangements
- `builds_on_unresolved` GROP
- `builds_on_unresolved` Task and Motion Planning
- `compares_to_unresolved` Task Planning with Random Arrangement
- `compares_to_unresolved` LLM-based Arrangement and Task Planning
- `compares_to_unresolved` GROP
<!-- GENERATED:END -->

## My Notes


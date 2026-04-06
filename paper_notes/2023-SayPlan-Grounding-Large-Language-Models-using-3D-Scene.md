---
paper_id: 114
title: "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning"
year: 2023
authors: "Rana et al."
url: "https://arxiv.org/abs/2307.06135"
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
  - "office 3D scene graph planning tasks"
  - "home 3D scene graph planning tasks"
builds_on:
  - "[[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]"
  - "[[2023-LLM-Planner-Few-Shot-Grounded-Planning-for-Embodied-Agents-with]]"
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
compares_to_unresolved:
  - "LLM-As-Planner"
  - "LLM+P"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
SayPlan grounds LLM-based robot planning in large environments by combining 3D scene graphs, LLM-guided semantic search, and iterative plan verification. It uses a scene-graph simulator to verify plans and provide textual feedback for self-correction.

# Why It Matters
It is a key paper on scaling LLM robot planning beyond small rooms into multi-room and multi-floor environments. The work showed how structured world models can keep planning grounded and token-efficient.

# Method / Setup
The authors evaluate semantic search and causal planning in office and home environments represented as 3D scene graphs, with tasks of varying complexity and comparisons against direct LLM planning and LLM plus classical path-planning variants.

# Key Claims
- 3D scene graphs let LLM planners scale to larger environments without overflowing context windows.
- Iterative verification and replanning substantially improve executability of long-horizon robot plans.
- Reducing the LLM planning horizon and delegating detailed navigation to classical planning improves reliability.

# Limitations
- The method assumes access to a high-quality prebuilt 3D scene graph and simulator API.
- LLMs still struggle with some logical, numerical, and negation-style graph reasoning.
- A small fraction of failures come from hallucinated nodes or insufficient replanning depth.

# Connections
- [[Software-Agents]]
- `evaluates` office 3D scene graph planning tasks
- `evaluates` home 3D scene graph planning tasks
- `builds_on` [[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]
- `builds_on` [[2023-LLM-Planner-Few-Shot-Grounded-Planning-for-Embodied-Agents-with]]
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `compares_to_unresolved` LLM-As-Planner
- `compares_to_unresolved` LLM+P
<!-- GENERATED:END -->

## My Notes


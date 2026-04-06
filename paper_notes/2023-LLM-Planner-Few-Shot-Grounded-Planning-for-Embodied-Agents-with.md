---
paper_id: 113
title: "LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models"
year: 2023
authors: "Song et al."
url: "https://arxiv.org/abs/2212.04088"
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
  - "ALFRED"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "Language Models as Zero-Shot Planners"
  - "HLSM: Bridging Vision and Language with Hierarchical Semantic Maps"
compares_to_unresolved:
  - "HLSM"
  - "FILM"
  - "HiTUT"
  - "E.T."
  - "M-TRACK"
  - "SayCan"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper presents a few-shot LLM-based high-level planner for embodied agents that dynamically replans using visible objects from the current environment. It uses in-context examples and grounded re-planning to generate subgoal sequences for long-horizon tasks.

# Why It Matters
It is a strong early result on sample-efficient LLM planning for embodied agents in partially observable environments. The paper showed competitive ALFRED performance with far less paired training data than standard embodied baselines.

# Method / Setup
The method is evaluated on ALFRED with a hierarchical setup that uses GPT-3 for high-level planning and HLSM components for perception and low-level control, comparing static and grounded re-planning under a strict few-shot regime.

# Key Claims
- LLMs can generate useful embodied high-level plans from very small numbers of demonstrations.
- Grounded re-planning with current visible objects improves robustness over static plans.
- Generative high-level planning can outperform adapted ranking-based baselines such as SayCan in ALFRED-like settings.

# Limitations
- End-to-end success is constrained by low-level planner and perception errors.
- The method still depends on prompt design, retrieval quality, and object visibility.
- High-level planning accuracy does not fully translate into task completion in difficult environments.

# Connections
- [[Software-Agents]]
- `evaluates` ALFRED
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` Language Models as Zero-Shot Planners
- `builds_on_unresolved` HLSM: Bridging Vision and Language with Hierarchical Semantic Maps
- `compares_to_unresolved` HLSM
- `compares_to_unresolved` FILM
- `compares_to_unresolved` HiTUT
- `compares_to_unresolved` E.T.
- `compares_to_unresolved` M-TRACK
- `compares_to_unresolved` SayCan
<!-- GENERATED:END -->

## My Notes


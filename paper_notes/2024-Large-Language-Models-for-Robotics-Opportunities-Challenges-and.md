---
paper_id: 116
title: "Large Language Models for Robotics: Opportunities, Challenges, and Perspectives"
year: 2024
authors: "Wang et al."
url: "https://arxiv.org/abs/2401.04334"
paper_type: "survey"
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
  - "robotic manipulation tasks from Google Open X-Embodiment style data"
builds_on:
  - "[[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]"
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper surveys opportunities and challenges in using large language models for robotics and includes a practical GPT-4V-based framework for embodied task planning. It examines how multimodal models can combine visual perception and language understanding for robotic manipulation.

# Why It Matters
It provides a useful map of the LLM-for-robotics space while also illustrating an early multimodal planning workflow with GPT-4V. The paper is a good entry point for the planning, manipulation, and reasoning perspectives on embodied robotics.

# Method / Setup
The paper discusses planning, manipulation, and reasoning applications of LLMs in robotics and evaluates a GPT-4V prompt-based planning framework on manipulation examples drawn from Google Open X-Embodiment style tasks.

# Key Claims
- Multimodal LLMs can better bridge natural-language instructions and embodied robot planning than text-only models.
- Prompted GPT-4V can generate plausible task plans across diverse manipulation scenarios.
- LLMs offer a flexible interface for planning, reasoning, and human-robot interaction.

# Limitations
- Current multimodal LLMs still have limited visual perception compared with specialized vision systems.
- The framework lacks strong physical and temporal reasoning for dynamic scenes.
- The evaluation emphasizes planning quality more than full closed-loop execution.

# Connections
- [[Software-Agents]]
- `evaluates` robotic manipulation tasks from Google Open X-Embodiment style data
- `builds_on` [[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
<!-- GENERATED:END -->

## My Notes


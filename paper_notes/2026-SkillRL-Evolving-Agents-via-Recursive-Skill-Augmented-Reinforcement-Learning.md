---
paper_id: 91
title: "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning"
year: 2026
authors: "Xia et al."
url: "https://arxiv.org/abs/2602.08234"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "pending"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "ALFWorld"
  - "WebShop"
  - "search-augmented QA"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "GRPO"
  - "ReAct"
  - "Reflexion"
  - "Mem0"
  - "ExpeL"
compares_to_unresolved:
  - "GRPO"
  - "RLOO"
  - "MemRL"
  - "Mem0"
  - "SimpleMem"
  - "EvolveR"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
SkillRL converts raw agent experiences into compact reusable skills, organizes them in a hierarchical skill library, and recursively evolves that library during reinforcement learning.

# Why It Matters
It is a strong paper for the experience-selection thread because it argues that agents should distill reusable strategic skills from trajectories rather than retrieve raw experiences directly.

# Method / Setup
The framework distills successful and failed trajectories into general and task-specific skills using a teacher model, initializes the agent with skill-aware supervised fine-tuning, and then uses GRPO while recursively expanding the skill bank from validation failures.

# Key Claims
- Abstract skills are more useful than raw trajectory memories for improving LLM agents.
- A hierarchical skill library reduces context footprint while improving generalization and robustness.
- The skill library should co-evolve with the policy during reinforcement learning rather than remain static.

# Limitations
- The system depends on a strong teacher model for skill distillation and refinement.
- Maintaining and evolving a hierarchical skill bank adds substantial pipeline complexity.

# Connections
- [[Memory-Context]]
- `evaluates` ALFWorld
- `evaluates` WebShop
- `evaluates` search-augmented QA
- `builds_on_unresolved` GRPO
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` Reflexion
- `builds_on_unresolved` Mem0
- `builds_on_unresolved` ExpeL
- `compares_to_unresolved` GRPO
- `compares_to_unresolved` RLOO
- `compares_to_unresolved` MemRL
- `compares_to_unresolved` Mem0
- `compares_to_unresolved` SimpleMem
- `compares_to_unresolved` EvolveR
<!-- GENERATED:END -->

## My Notes


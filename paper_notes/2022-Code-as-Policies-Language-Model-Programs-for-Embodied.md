---
paper_id: 111
title: "Code as Policies: Language Model Programs for Embodied Control"
year: 2022
authors: "Liang et al."
url: "https://arxiv.org/abs/2209.07753"
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
  - "RoboCodeGen"
  - "HumanEval"
  - "real robot drawing and manipulation tasks"
builds_on:
  - "[[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]"
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "Socratic Models"
compares_to_unresolved:
  - "Chain-of-Thought Prompting"
  - "vanilla natural language prompting"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes using code-writing language models to synthesize executable robot policies directly from natural-language instructions. Instead of only producing high-level plans, the model generates Python programs that call perception and control APIs for embodied control.

# Why It Matters
It is a key paper for grounding LLM reasoning into executable embodied behavior with interpretable policy code. The work also showed that hierarchical code generation can improve both robotics-specific and general code generation.

# Method / Setup
The paper evaluates hierarchical code generation on the RoboCodeGen and HumanEval benchmarks and demonstrates real robot tasks including drawing, tabletop manipulation, navigation, and simple reactive control.

# Key Claims
- Language models can generate robot policy code that captures spatial reasoning and behavioral commonsense.
- Hierarchical code generation improves performance on robotics and general code-generation benchmarks.
- Generated code can ground language into perception-action loops without large robot-specific training datasets.

# Limitations
- Capabilities are constrained by the available perception APIs and low-level control primitives.
- The approach cannot guarantee correctness or feasibility of generated code ahead of execution.
- The abstraction level of instructions still needs to stay close to what the prompted APIs can support.

# Connections
- [[Software-Agents]]
- `evaluates` RoboCodeGen
- `evaluates` HumanEval
- `evaluates` real robot drawing and manipulation tasks
- `builds_on` [[2022-Inner-Monologue-Embodied-Reasoning-through-Planning-with-Language]]
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` Socratic Models
- `compares_to_unresolved` Chain-of-Thought Prompting
- `compares_to_unresolved` vanilla natural language prompting
<!-- GENERATED:END -->

## My Notes


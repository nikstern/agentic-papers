---
paper_id: 110
title: "Inner Monologue: Embodied Reasoning through Planning with Language Models"
year: 2022
authors: "Huang et al."
url: "https://arxiv.org/abs/2207.05608"
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
  - "simulated tabletop rearrangement"
  - "real-world tabletop rearrangement"
  - "real-world mobile manipulation"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "Language Models as Zero-Shot Planners"
compares_to_unresolved:
  - "SayCan"
  - "CLIPort"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces a closed-loop LLM planning framework that feeds natural-language environment feedback back into the planner so robots can replan and recover during embodied tasks. The core idea is an "inner monologue" that combines high-level language reasoning with observations about success, objects, and task progress.

# Why It Matters
It is an early and influential paper on making LLM-based robot planning adaptive rather than open-loop. It showed that language feedback can materially improve robustness in real and simulated embodied settings.

# Method / Setup
The authors evaluate simulated tabletop rearrangement, real-world tabletop rearrangement, and real-world mobile manipulation, varying the types of feedback available to the LLM such as object descriptions, success signals, scene progress, and human answers.

# Key Claims
- Closed-loop language feedback improves long-horizon embodied planning over open-loop prompting.
- Success and scene feedback help the planner recover from failed actions and environmental disturbances.
- LLMs can exhibit emergent embodied behaviors such as replanning, clarifying questions, and adaptation to changed instructions when grounded with feedback.

# Limitations
- The framework depends on external perception, success detection, and low-level skills rather than end-to-end embodied control.
- Performance is bottlenecked by the reliability of underlying robot policies and feedback modules.
- Some emergent behaviors are inconsistent and not fully reliable.

# Connections
- [[Software-Agents]]
- `evaluates` simulated tabletop rearrangement
- `evaluates` real-world tabletop rearrangement
- `evaluates` real-world mobile manipulation
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` Language Models as Zero-Shot Planners
- `compares_to_unresolved` SayCan
- `compares_to_unresolved` CLIPort
<!-- GENERATED:END -->

## My Notes


---
paper_id: 115
title: "Look Before You Leap: Unveiling the Power of GPT-4V in Robotic Vision-Language Planning"
year: 2023
authors: "Hu et al."
url: "https://arxiv.org/abs/2311.17842"
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
  - "real-world long-horizon manipulation tasks"
  - "RAVENS tabletop rearrangement"
builds_on:
  - "[[2023-PaLM-E-An-Embodied-Multimodal-Language-Model]]"
compares_to: []
builds_on_unresolved:
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "Grounded Decoding"
compares_to_unresolved:
  - "SayCan"
  - "Grounded Decoding"
  - "CLIPort"
  - "GPT-4"
  - "Llama 2"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces ViLa, a robotic vision-language planning approach that uses GPT-4V directly as a grounded planner over images and language. The system replans in closed loop from visual feedback rather than depending on separate affordance models to mediate perception.

# Why It Matters
It is one of the clearest demonstrations that strong VLMs can outperform text-only LLM planners on embodied manipulation tasks by reasoning directly over visual context. The paper highlights the value of unified multimodal planning for spatial layouts, object attributes, and dynamic replanning.

# Method / Setup
The authors evaluate 16 real-world long-horizon manipulation tasks and 16 simulated RAVENS tabletop rearrangement tasks, comparing ViLa against SayCan, Grounded Decoding, CLIPort, and LLM-only planning baselines.

# Key Claims
- Direct vision-language planning improves grounded commonsense reasoning for robotics over text-only planners.
- Closed-loop visual feedback materially improves recovery and robustness in dynamic environments.
- VLMs support flexible multimodal goal specification such as images, drawings, pointing, and mixed image-plus-language prompts.

# Limitations
- The method still relies on existing primitive skills for actual execution.
- The planner is a black-box VLM whose failures can be hard to analyze or verify.
- Performance remains sensitive to prompt design and the quality of visual perception.

# Connections
- [[Software-Agents]]
- `evaluates` real-world long-horizon manipulation tasks
- `evaluates` RAVENS tabletop rearrangement
- `builds_on` [[2023-PaLM-E-An-Embodied-Multimodal-Language-Model]]
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` Grounded Decoding
- `compares_to_unresolved` SayCan
- `compares_to_unresolved` Grounded Decoding
- `compares_to_unresolved` CLIPort
- `compares_to_unresolved` GPT-4
- `compares_to_unresolved` Llama 2
<!-- GENERATED:END -->

## My Notes


---
paper_id: 112
title: "PaLM-E: An Embodied Multimodal Language Model"
year: 2023
authors: "Driess et al."
url: "https://arxiv.org/abs/2303.03378"
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
  - "tabletop manipulation"
  - "visual question answering"
  - "language-table style robot tasks"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "PaLM: Scaling Language Modeling with Pathways"
  - "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances"
  - "Interactive Language: Talking to Robots in Real Time"
compares_to_unresolved:
  - "PaLI"
  - "SayCan"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
PaLM-E is an embodied multimodal language model that directly injects images and state observations into a large language model to support planning, visual question answering, and robot control. The model treats language and sensor inputs as a unified multimodal sentence.

# Why It Matters
It is one of the foundational papers for multimodal embodied language models in robotics. The work showed that co-training robotics with broader vision-language data can improve embodied performance and preserve strong language capabilities.

# Method / Setup
The authors train multimodal variants of PaLM with robot, visual question answering, captioning, and language data, then evaluate on tabletop manipulation, language-table style embodied tasks, and visual QA benchmarks such as OK-VQA.

# Key Claims
- A single multimodal LLM can jointly handle perception, language reasoning, and embodied planning.
- Multi-task co-training improves robotic task success and cross-domain transfer.
- Larger models retain language ability better during multimodal adaptation.

# Limitations
- The approach requires large-scale multimodal training and substantial compute.
- Robotics performance still depends on downstream low-level skills and data quality.
- Robustness to novel real-world conditions and out-of-distribution settings remains limited.

# Connections
- [[Software-Agents]]
- `evaluates` tabletop manipulation
- `evaluates` visual question answering
- `evaluates` language-table style robot tasks
- `builds_on_unresolved` PaLM: Scaling Language Modeling with Pathways
- `builds_on_unresolved` Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- `builds_on_unresolved` Interactive Language: Talking to Robots in Real Time
- `compares_to_unresolved` PaLI
- `compares_to_unresolved` SayCan
<!-- GENERATED:END -->

## My Notes


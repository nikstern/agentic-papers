---
paper_id: 65
title: "Building Cooperative Embodied Agents Modularly with Large Language Models"
year: 2023
authors: "Zhang et al."
url: "https://arxiv.org/abs/2307.02485"
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
  - "cooperative embodied agents"
  - "decentralized multi-agent cooperation"
  - "human-ai cooperation"
  - "TDW-MAT"
  - "C-WAH"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "VirtualHome"
  - "ThreeDWorld"
  - "DEC-POMDP"
compares_to_unresolved:
  - "Rule-based Hierarchical Planner"
  - "MCTS-based Hierarchical Planner"
  - "Multi-Agent Transformer"
  - "LLAMA-2"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
CoELA is a modular cognitive-inspired framework that uses large language models for planning and communication in decentralized cooperative embodied tasks with costly natural-language interaction.

# Why It Matters
It is a key embodied multi-agent paper because it tests whether LLMs can support real cooperation under partial observability and communication costs rather than unrestricted chat.

# Method / Setup
The framework combines perception, memory, communication, planning, and execution modules and is evaluated on the TDW-MAT and C-WAH environments for AI-AI and human-AI cooperation.

# Key Claims
- LLMs can drive effective decentralized embodied cooperation when embedded in a modular architecture.
- Natural-language communication improves trust and effectiveness in human-AI cooperation.
- Open models can approach stronger proprietary-model performance after targeted fine-tuning.

# Limitations
- Current LLMs still struggle with robust 3D spatial reasoning and low-level embodied control reasoning.
- Communication among AI agents is not yet consistently strong enough to always yield large gains over non-communicating planners.
- The framework remains dependent on external perception and procedural modules rather than end-to-end embodied reasoning.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` cooperative embodied agents
- `evaluates` decentralized multi-agent cooperation
- `evaluates` human-ai cooperation
- `evaluates` TDW-MAT
- `evaluates` C-WAH
- `builds_on_unresolved` VirtualHome
- `builds_on_unresolved` ThreeDWorld
- `builds_on_unresolved` DEC-POMDP
- `compares_to_unresolved` Rule-based Hierarchical Planner
- `compares_to_unresolved` MCTS-based Hierarchical Planner
- `compares_to_unresolved` Multi-Agent Transformer
- `compares_to_unresolved` LLAMA-2
<!-- GENERATED:END -->

## My Notes


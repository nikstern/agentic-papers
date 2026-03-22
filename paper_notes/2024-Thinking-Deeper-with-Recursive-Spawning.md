---
paper_id: 56
title: "Thinking Deeper with Recursive Spawning"
year: 2024
authors: "Schroeder et al."
url: "https://arxiv.org/abs/2405.17402"
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
  - "recursive agent decomposition"
  - "agent tasks"
  - "grounded question answering"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "RAP"
  - "Reflexion"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
THREAD treats LLM generation as an execution thread that can recursively spawn child threads for subproblems and then rejoin with compact results.

# Why It Matters
It is an important adjacent systems paper because it operationalizes recursive decomposition for practical agent tasks and question answering.

# Method / Setup
The framework uses recursive spawning with parent-child information flow functions and evaluates on agent and grounded QA benchmarks such as ALFWorld, WebShop, TextCraft, DataCommons QA, and MIMIC-III ICU QA.

# Key Claims
- Recursive spawning allows more adaptive intermediate work than single-context generation.
- THREAD improves performance on several agent and QA tasks across both large and small models.
- A unified recursive scaffold can replace more rigid planner-executor patterns in some settings.

# Limitations
- The system relies heavily on prompt design rather than learned control policies.
- Error handling remains mostly implicit rather than explicitly modeled.
- Parent-child communication can be lossy depending on what context is passed.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` recursive agent decomposition
- `evaluates` agent tasks
- `evaluates` grounded question answering
- `compares_to_unresolved` RAP
- `compares_to_unresolved` Reflexion
<!-- GENERATED:END -->

## My Notes


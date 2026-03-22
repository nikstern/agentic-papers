---
paper_id: 83
title: "A Survey of Context Engineering for Large Language Models"
year: 2025
authors: "Mei et al."
url: "https://arxiv.org/abs/2507.13334"
paper_type: "survey"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "context engineering methods"
  - "evaluation frameworks"
  - "benchmark datasets"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "prompt engineering"
  - "retrieval-augmented generation"
  - "memory systems"
  - "tool-integrated reasoning"
  - "multi-agent systems"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey formalizes context engineering as a distinct discipline for optimizing the information payloads given to LLMs, moving beyond ad hoc prompt design toward a unified systems view.

# Why It Matters
It is the most direct survey anchor for the context-engineering line in the vault because it unifies prompt engineering, RAG, memory, tool use, and multi-agent systems under one framing.

# Method / Setup
The paper surveys more than 1400 works and organizes the area into foundational components for context retrieval, processing, and management plus system implementations such as RAG, memory systems, tool-integrated reasoning, and multi-agent systems.

# Key Claims
- Context engineering should be treated as a formal discipline rather than a loose collection of prompting tricks.
- A unified taxonomy clarifies the links between prompting, retrieval, memory, tool use, and multi-agent coordination.
- A major open problem is the gap between LLMs' ability to understand rich context and their weaker ability to generate equally sophisticated long-form outputs.

# Limitations
- As a survey, it does not validate a new context-engineering mechanism empirically.
- The field is fragmented and moving quickly, so parts of the synthesis may age rapidly as systems and benchmarks evolve.

# Connections
- [[Memory-Context]]
- `evaluates` context engineering methods
- `evaluates` evaluation frameworks
- `evaluates` benchmark datasets
- `builds_on_unresolved` prompt engineering
- `builds_on_unresolved` retrieval-augmented generation
- `builds_on_unresolved` memory systems
- `builds_on_unresolved` tool-integrated reasoning
- `builds_on_unresolved` multi-agent systems
<!-- GENERATED:END -->

## My Notes


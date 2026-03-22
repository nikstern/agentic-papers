---
paper_id: 79
title: "TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Term Memory for Scalable Code Generation"
year: 2025
authors: "Shen and Joung"
url: "https://arxiv.org/abs/2510.23010"
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
  - "HumanEval"
  - "BigCodeBench"
  - "ClassEval"
  - "code generation"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "MapCoder"
  - "ChatDev"
  - "MetaGPT"
compares_to_unresolved:
  - "MapCoder"
  - "Reflexion"
  - "Self-Planning"
  - "Chain-of-Thought"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
TALM is a dynamic tree-structured multi-agent code generation framework with localized re-reasoning and long-term memory. It decomposes tasks hierarchically, validates child outputs, and reuses prior experiences to improve scalable code generation.

# Why It Matters
It is relevant to software-agent work because it combines structured multi-agent decomposition with long-term memory and selective error recovery for code generation.

# Method / Setup
Tree-structured multi-agent framework for code generation with specialized code and validation agents, localized re-reasoning, and a vector-backed long-term memory module, evaluated on HumanEval, BigCodeBench, and ClassEval.

# Key Claims
- Dynamic tree-structured collaboration is more flexible than rigid multi-agent pipelines for complex code generation tasks.
- Localized re-reasoning improves robustness and avoids expensive full restarts when decomposition errors occur.
- Long-term memory helps performance most on harder long-context coding benchmarks by enabling reuse of successful strategies.

# Limitations
- The framework introduces orchestration complexity and more moving parts than simpler prompting-based coding systems.
- Its effectiveness still depends on tuned tree-shape hyperparameters and was evaluated on a limited benchmark suite.

# Connections
- [[Software-Agents]]
- `evaluates` HumanEval
- `evaluates` BigCodeBench
- `evaluates` ClassEval
- `evaluates` code generation
- `builds_on_unresolved` MapCoder
- `builds_on_unresolved` ChatDev
- `builds_on_unresolved` MetaGPT
- `compares_to_unresolved` MapCoder
- `compares_to_unresolved` Reflexion
- `compares_to_unresolved` Self-Planning
- `compares_to_unresolved` Chain-of-Thought
<!-- GENERATED:END -->

## My Notes


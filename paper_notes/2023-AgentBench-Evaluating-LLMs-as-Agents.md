---
paper_id: 63
title: "AgentBench: Evaluating LLMs as Agents"
year: 2023
authors: "Liu et al."
url: "https://arxiv.org/abs/2308.03688"
paper_type: "benchmark"
primary_topic: "agent-evaluation"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "agent-evaluation"
evaluates:
  - "llms as agents"
  - "interactive agent evaluation"
  - "operating system tasks"
  - "database tasks"
  - "knowledge graph tasks"
  - "web shopping"
  - "web browsing"
  - "house-holding"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ALFWorld"
  - "WebShop"
  - "Mind2Web"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
AgentBench introduces a standardized benchmark for evaluating large language models as agents across interactive operating system, database, knowledge graph, game, and web environments.

# Why It Matters
It is a foundational benchmark paper for agent evaluation because it shifts measurement from static QA-style tasks to interactive, environment-grounded execution.

# Method / Setup
The benchmark evaluates 29 LLMs with a consistent Chain-of-Thought/ReAct-style setup over eight environments spanning code-grounded, game-grounded, and web-grounded tasks.

# Key Claims
- LLM agents should be evaluated in interactive environments rather than only on static benchmarks.
- Top proprietary models substantially outperform open models on agentic tasks.
- Long-horizon reasoning, instruction following, and repetitive failure loops are major current bottlenecks for LLM agents.

# Limitations
- The benchmark is limited to text-oriented interaction and does not cover full multimodal or physical embodiment.
- Its prompting setup intentionally uses simple reasoning strategies rather than stronger search or reflection scaffolds.
- Benchmark coverage is broad but still not exhaustive relative to real-world agent deployment.

# Connections
- [[Agent-Evaluation]]
- `evaluates` llms as agents
- `evaluates` interactive agent evaluation
- `evaluates` operating system tasks
- `evaluates` database tasks
- `evaluates` knowledge graph tasks
- `evaluates` web shopping
- `evaluates` web browsing
- `evaluates` house-holding
- `builds_on_unresolved` ALFWorld
- `builds_on_unresolved` WebShop
- `builds_on_unresolved` Mind2Web
<!-- GENERATED:END -->

## My Notes


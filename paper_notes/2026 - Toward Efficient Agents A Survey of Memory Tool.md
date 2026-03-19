---
paper_id: 26
title: "Toward Efficient Agents: A Survey of Memory, Tool learning, and Planning"
year: 2026
authors: "Yang et al."
url: "https://arxiv.org/abs/2601.14192"
paper_type: "survey"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "efficient agent design"
  - "memory efficiency"
  - "tool-learning efficiency"
  - "planning efficiency"
builds_on:
  - "[[2023 - MemGPT Towards LLMs as Operating Systems]]"
compares_to:
  - "[[2024 - A Survey on the Memory Mechanism of Large]]"
  - "[[2025 - Rethinking Memory in LLM based Agents Representations Operations]]"
builds_on_unresolved:
  - "Voyager"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
This survey focuses on the efficiency of LLM-based agents, organizing the field around memory, tool learning, and planning while treating agent performance as a Pareto trade-off between effectiveness and resource cost.

# Why It Matters
It gives the vault a systems-oriented view of efficient agents and is especially relevant if you care about deployability, context growth, latency, and token cost.

# Method / Setup
The paper reviews efficiency techniques across memory construction and access, tool selection and invocation, and single-agent and multi-agent planning, then summarizes common metrics and benchmark practices for efficiency-aware evaluation.

# Key Claims
- Agent efficiency should be analyzed at the system level rather than only at the base-model level.
- Memory, tool use, and planning are the dominant sources of agent inefficiency and require different optimization strategies.
- A useful notion of efficient agents is performance under explicit cost and latency constraints, not raw task success alone.

# Limitations
- The survey emphasizes taxonomy and synthesis more than direct head-to-head empirical validation.
- It highlights the lack of unified evaluation standards, so many efficiency comparisons remain difficult to normalize across papers.

# Connections
- [[LLM Multi-Agent Systems]]
- `evaluates` efficient agent design
- `evaluates` memory efficiency
- `evaluates` tool-learning efficiency
- `evaluates` planning efficiency
- `builds_on` [[2023 - MemGPT Towards LLMs as Operating Systems]]
- `compares_to` [[2024 - A Survey on the Memory Mechanism of Large]]
- `compares_to` [[2025 - Rethinking Memory in LLM based Agents Representations Operations]]
- `builds_on_unresolved` Voyager

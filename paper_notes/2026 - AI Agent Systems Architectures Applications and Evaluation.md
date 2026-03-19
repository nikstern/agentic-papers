---
paper_id: 24
title: "AI Agent Systems: Architectures, Applications, and Evaluation"
year: 2026
authors: "Xu et al."
url: "https://arxiv.org/abs/2601.01743"
paper_type: "survey"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "ai agent architectures"
  - "agent evaluation frameworks"
  - "tool-use and planning systems"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "ReAct"
  - "MRKL"
  - "Tree of Thoughts"
  - "Toolformer"
compares_to_unresolved:
  - "AgentBench"
  - "WebArena"
  - "ToolBench"
  - "SWE-bench"
  - "GAIA"
relations: []
source: "alphaxiv-mcp"
---

# Summary
This survey frames AI agents as systems that couple a foundation model with memory, tools, verifiers, and an execution loop, then organizes the field around architectures, orchestration patterns, applications, and evaluation.

# Why It Matters
It is a broad 2026 overview paper that can anchor the vault's multi-agent and agent-systems layer with a unified taxonomy and evaluation framing.

# Method / Setup
The paper is a survey that synthesizes agent architectures such as RAG, ReAct-style control loops, MRKL-style tool routing, critic and reflection mechanisms, search-based deliberation, and multi-agent orchestration, then proposes a multidimensional evaluation framework.

# Key Claims
- AI agents should be understood as systems problems, not just as stronger base models.
- A useful agent taxonomy needs to cover policy cores, memory, tools, verifiers, planners, and environments together.
- Agent evaluation should include task success, efficiency, tool correctness, trajectory quality, robustness, and safety rather than a single headline metric.

# Limitations
- It is a synthesis paper rather than an empirical benchmark or system implementation.
- Its breadth is high, but that also means some subareas are treated at a higher level than specialized surveys.

# Connections
- [[LLM Multi-Agent Systems]]
- `evaluates` ai agent architectures
- `evaluates` agent evaluation frameworks
- `evaluates` tool-use and planning systems
- `builds_on_unresolved` ReAct
- `builds_on_unresolved` MRKL
- `builds_on_unresolved` Tree of Thoughts
- `builds_on_unresolved` Toolformer
- `compares_to_unresolved` AgentBench
- `compares_to_unresolved` WebArena
- `compares_to_unresolved` ToolBench
- `compares_to_unresolved` SWE-bench
- `compares_to_unresolved` GAIA

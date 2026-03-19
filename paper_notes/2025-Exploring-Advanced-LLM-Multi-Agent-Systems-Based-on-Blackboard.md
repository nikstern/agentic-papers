---
paper_id: 23
title: "Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture"
year: 2025
authors: "Han and Zhang"
url: "https://arxiv.org/abs/2507.01701"
paper_type: "system"
primary_topic: "llm-multi-agent-systems"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "llm-multi-agent-systems"
evaluates:
  - "dynamic multi-agent coordination"
  - "shared blackboard reasoning"
  - "reasoning and math tasks"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "blackboard architecture"
compares_to_unresolved:
  - "GPTSwarm"
  - "AFlow"
  - "MaAS"
relations: []
source: "alphaxiv-mcp"
---

# Summary
This paper revives the blackboard architecture for LLM multi-agent systems, using a shared workspace where dynamically selected agents contribute and refine problem-solving state.

# Why It Matters
It shows a concrete alternative to fixed-role chat workflows and training-heavy autonomous systems by making shared state and dynamic coordination the center of the design.

# Method / Setup
The framework combines a blackboard, a control unit that selects agents based on current state, dynamically generated experts, and predefined roles such as planner, critic, cleaner, and decider, then evaluates the system on reasoning and math benchmarks.

# Key Claims
- Blackboard-style shared state enables flexible and effective multi-agent collaboration.
- Dynamic agent selection can outperform fixed workflows while remaining token-efficient.
- Classical AI coordination architectures remain relevant when paired with strong LLMs.

# Limitations
- The initial implementation uses a limited set of predefined agent roles and benchmark tasks.
- The framework still depends on careful blackboard management to avoid clutter and drift.

# Connections
- [[LLM-Multi-Agent-Systems]]
- `evaluates` dynamic multi-agent coordination
- `evaluates` shared blackboard reasoning
- `evaluates` reasoning and math tasks
- `builds_on_unresolved` blackboard architecture
- `compares_to_unresolved` GPTSwarm
- `compares_to_unresolved` AFlow
- `compares_to_unresolved` MaAS

---
paper_id: 4
title: "MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents"
year: 2025
authors: "Zhu et al."
url: "https://arxiv.org/abs/2503.01935"
paper_type: "benchmark"
primary_topic: "agent-evaluation"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "agent-evaluation"
evaluates:
  - "multi-agent collaboration"
  - "multi-agent competition"
  - "coordination protocols"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "AgentBench"
  - "ResearchTown"
relations: []
source: "manual"
---

# Summary
MultiAgentBench introduces a benchmark and framework for evaluating collaboration and competition in LLM-based multi-agent systems across research, coding, database, game, and negotiation scenarios.

# Why It Matters
It gives the vault a benchmark-centered anchor for studying whether multi-agent systems actually coordinate well rather than merely producing plausible outputs.

# Method / Setup
The paper introduces the MARBLE framework, evaluates multiple coordination topologies and planning strategies, and scores systems with task metrics plus communication and planning quality signals across collaborative and adversarial environments.

# Key Claims
- Single-agent benchmarks are insufficient for evaluating multi-agent behavior.
- Coordination topology and planning strategy materially affect outcomes.
- Task success and coordination quality need to be measured separately.

# Limitations
- Benchmark coverage is broad but still incomplete relative to open-world multi-agent use.
- Some coordination scores depend on LLM-based judging rather than fully objective metrics.

# Connections
- [[Agent Evaluation]]
- `evaluates` multi-agent collaboration
- `evaluates` multi-agent competition
- `evaluates` coordination protocols
- `compares_to_unresolved` AgentBench
- `compares_to_unresolved` ResearchTown

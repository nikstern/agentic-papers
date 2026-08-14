---
paper_id: 123
title: "The Hanabi Challenge: A New Frontier for AI Research"
year: 2019
authors: "Bard et al."
url: "https://arxiv.org/abs/1902.00506"
paper_type: "benchmark"
primary_topic: "multi-agent-foundations"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "multi-agent-foundations"
evaluates:
  - "cooperative multi-agent learning"
  - "self-play"
  - "ad-hoc team play"
  - "partner compatibility"
  - "belief and intention reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "decentralized Markov decision processes"
  - "theory of mind"
  - "dynamic epistemic logic"
compares_to_unresolved:
  - "ACHA"
  - "BAD"
  - "Rainbow"
  - "rule-based Hanabi agents"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
The Hanabi Challenge proposes Hanabi as a benchmark for cooperative agents that must act under imperfect information, limited communication, and conventions that encode beliefs and intentions.

# Why It Matters
It supplies a concrete foundation for common-ground, partner-modeling, and protocol-compatibility failures that are easy to overlook when LLM-agent teams are evaluated only in self-play or with fixed prompts.

# Method / Setup
The paper introduces the open-source Hanabi Learning Environment, defines self-play and ad-hoc-team evaluation settings, and benchmarks learning and hand-coded agents across two-to-five-player games. Ad-hoc evaluation pairs independently trained policies that may use incompatible conventions.

# Key Claims
- Hanabi makes reasoning about partners' beliefs, intentions, and conventions central to cooperative success.
- Strong self-play performance does not imply compatibility with unfamiliar partners.
- Contemporary learning agents can perform reasonably in self-play yet remain brittle in ad-hoc teams.
- Multi-agent evaluation should include held-out partner populations rather than only teams trained together.

# Limitations
- Hanabi is a stylized card game, so results do not directly establish performance in open-ended real-world collaboration.
- The paper's ad-hoc experiments cover a limited pool of learning agents and do not directly evaluate human partners.
- Some hand-coded agents could not be included in cross-play because their implementations were incompatible.
- A high game score does not by itself isolate theory-of-mind reasoning from learned conventions or search.

# Connections
- [[Multi-Agent-Foundations]]
- `evaluates` cooperative multi-agent learning
- `evaluates` self-play
- `evaluates` ad-hoc team play
- `evaluates` partner compatibility
- `evaluates` belief and intention reasoning
- `builds_on_unresolved` decentralized Markov decision processes
- `builds_on_unresolved` theory of mind
- `builds_on_unresolved` dynamic epistemic logic
- `compares_to_unresolved` ACHA
- `compares_to_unresolved` BAD
- `compares_to_unresolved` Rainbow
- `compares_to_unresolved` rule-based Hanabi agents
<!-- GENERATED:END -->

## My Notes


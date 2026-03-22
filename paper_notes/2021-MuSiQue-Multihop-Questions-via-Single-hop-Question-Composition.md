---
paper_id: 77
title: "MuSiQue: Multihop Questions via Single-hop Question Composition"
year: 2021
authors: "Trivedi et al."
url: "https://arxiv.org/abs/2108.00573"
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
  - "multihop question answering"
  - "MuSiQue-Ans"
  - "MuSiQue-Full"
  - "connected reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "HotpotQA"
  - "2WikiMultihopQA"
  - "Is multihop QA in DiRe condition? Measuring and reducing disconnected reasoning"
compares_to_unresolved:
  - "HotpotQA"
  - "2WikiMultihopQA"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
MuSiQue is a multihop question answering benchmark built by composing single-hop questions in a way that explicitly enforces connected reasoning. It is designed to reduce shortcut solutions and make multihop QA evaluation more faithful.

# Why It Matters
It is a useful benchmark paper for reasoning evaluation because it focuses on eliminating disconnected reasoning and dataset artifacts rather than only scaling benchmark size.

# Method / Setup
Benchmark construction pipeline that composes single-hop QA pairs into multihop questions, filters disconnected reasoning with model-based checks, minimizes train-test leakage, adds hard distractors, and includes unanswerable counterparts in MuSiQue-Full.

# Key Claims
- Existing multihop QA benchmarks allow too many shortcut solutions through disconnected reasoning and dataset artifacts.
- Bottom-up composition from single-hop questions makes it possible to enforce genuine multihop dependencies by construction.
- MuSiQue creates a larger human-model gap and is substantially harder to game with artifact-based baselines than earlier benchmarks.

# Limitations
- The benchmark is specialized to multihop QA over Wikipedia-style sources rather than general agentic reasoning in open environments.
- Its construction pipeline is comparatively elaborate and depends on careful filtering and crowdsourcing.

# Connections
- [[Agent-Evaluation]]
- `evaluates` multihop question answering
- `evaluates` MuSiQue-Ans
- `evaluates` MuSiQue-Full
- `evaluates` connected reasoning
- `builds_on_unresolved` HotpotQA
- `builds_on_unresolved` 2WikiMultihopQA
- `builds_on_unresolved` Is multihop QA in DiRe condition? Measuring and reducing disconnected reasoning
- `compares_to_unresolved` HotpotQA
- `compares_to_unresolved` 2WikiMultihopQA
<!-- GENERATED:END -->

## My Notes


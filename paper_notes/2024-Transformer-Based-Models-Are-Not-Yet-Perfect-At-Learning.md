---
paper_id: 60
title: "Transformer-Based Models Are Not Yet Perfect At Learning to Emulate Structural Recursion"
year: 2024
authors: "Zhang et al."
url: "https://arxiv.org/abs/2401.12947"
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
  - "structural recursion evaluation"
  - "mechanistic analysis of recursion"
  - "tree traversal tasks"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "standard Transformer models"
  - "pre-trained LLMs"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper studies whether transformer-based models truly learn structural recursion or instead rely on brittle non-recursive shortcuts.

# Why It Matters
It is an important negative and diagnostic paper that helps calibrate claims about recursion in current language models.

# Method / Setup
The authors define a framework for structural recursion, test small Transformers, pre-trained models, and frontier LLMs on recursive tasks such as binary successor and tree traversals, and use mechanistic analysis to inspect learned strategies.

# Key Claims
- Transformers often solve recursive tasks through shortcuts rather than true recursive generalization.
- Edge cases and increased depth expose systematic failures in learned heuristics.
- Current prompting and pretraining are not enough to reliably induce structural recursion.

# Limitations
- The tasks are stylized and do not cover all real-world recursion demands.
- The paper is more diagnostic than constructive.
- Some conclusions are based on targeted synthetic tasks rather than broad naturalistic benchmarks.

# Connections
- [[Agent-Evaluation]]
- `evaluates` structural recursion evaluation
- `evaluates` mechanistic analysis of recursion
- `evaluates` tree traversal tasks
- `compares_to_unresolved` standard Transformer models
- `compares_to_unresolved` pre-trained LLMs
<!-- GENERATED:END -->

## My Notes


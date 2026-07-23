---
paper_id: 119
title: "How Do Language Models Compose Functions?"
year: 2025
authors: "Khandelwal and Pavlick"
url: "https://arxiv.org/abs/2510.01685"
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
  - "Feedforward LLM performance on compositional two-hop factual recall tasks."
  - "Residual stream representations to identify processing mechanisms."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "compositionality gap in language models"
  - "debates on compositional vs idiomatic cognitive processing mechanisms"
  - "embedding space geometry as a factor in model behavior"
compares_to_unresolved:
  - "prior claims that compositionality is necessary for compositional behavior"
  - "purely symbolic compositional models versus LLMs without explicit symbolic components"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
The paper investigates how feedforward large language models (LLMs) solve two-hop factual recall tasks represented compositionally as y=g(f(x)). It confirms the persistent 'compositionality gap' where solving components f(x) and g(z) individually does not guarantee solving the composition, and identifies two processing mechanisms: compositional and direct.

# Why It Matters
Understanding whether LLMs process tasks compositionally or directly informs theories of how these models achieve complex reasoning and their limitations, with implications for improving generalization and explainability in AI.

# Method / Setup
The study analyzes feedforward LLMs on two-hop factual recall tasks, decodes residual stream representations to distinguish compositional and direct mechanisms, and examines embedding space geometry's relation to the employed processing method.

# Key Claims
- LLMs still exhibit a compositionality gap despite improvements and model size increases.
- LLMs utilize two distinct processing mechanisms: compositional (computing intermediate variables) and direct (bypassing intermediates).
- Mechanism choice correlates with embedding space geometry: idiomatic (direct) mechanism dominates when tasks align with input-output translations in embedding spaces.
- Both processing mechanisms are comparably effective in producing correct outputs.

# Limitations
- Study focuses only on feedforward LLMs and two-hop factual recall tasks, limiting generalizability to other architectures and tasks.
- Analysis relies on detectability of intermediate variable representations, which might miss subtler forms of compositional processing.
- Exploration is preliminary and does not fully establish causality between embedding geometry and processing mechanism.

# Connections
- [[Agent-Evaluation]]
- `evaluates` Feedforward LLM performance on compositional two-hop factual recall tasks.
- `evaluates` Residual stream representations to identify processing mechanisms.
- `builds_on_unresolved` compositionality gap in language models
- `builds_on_unresolved` debates on compositional vs idiomatic cognitive processing mechanisms
- `builds_on_unresolved` embedding space geometry as a factor in model behavior
- `compares_to_unresolved` prior claims that compositionality is necessary for compositional behavior
- `compares_to_unresolved` purely symbolic compositional models versus LLMs without explicit symbolic components
<!-- GENERATED:END -->

## My Notes


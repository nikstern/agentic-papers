---
paper_id: 29
title: "Let the Agent Search: Autonomous Exploration Beats Rigid Workflows in Temporal Question Answering"
year: 2026
authors: "Lv et al."
url: "https://arxiv.org/abs/2603.01853"
paper_type: "system"
primary_topic: "search-retrieval"
secondary_topics: []
status: "cited"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "search-retrieval"
evaluates:
  - "temporal question answering"
  - "autonomous search"
  - "training-free retrieval agents"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Temp-R1"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
AT2QA treats temporal question answering as an autonomous search problem, letting an LLM agent iteratively explore a temporal knowledge graph instead of following a rigid retrieval workflow.

# Why It Matters
It is a strong example of agentic retrieval beating workflow-heavy pipelines, and it supports the vault’s broader interest in autonomous search over fixed orchestration.

# Method / Setup
The system equips an off-the-shelf LLM with a temporal search tool, lets it iteratively plan, retrieve, self-correct, and self-validate, and augments it with a training-free experience library distilled from successful trajectories.

# Key Claims
- Autonomous exploration can outperform both rigid workflows and heavy fine-tuning in temporal QA.
- LLMs already contain strong latent temporal reasoning abilities that better interfaces can unlock.
- Self-correction and explicit evidence retrieval are especially important for complex multi-hop temporal questions.

# Limitations
- The setting is specialized to temporal knowledge graph question answering.
- Autonomous exploration can still be slower and less predictable than fixed pipelines.

# Connections
- [[Search-Retrieval]]
- `evaluates` temporal question answering
- `evaluates` autonomous search
- `evaluates` training-free retrieval agents
- `compares_to_unresolved` Temp-R1
<!-- GENERATED:END -->

## My Notes


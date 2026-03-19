---
paper_id: 33
title: "Chain-of-Symbol Prompting Elicits Planning in Large Langauge Models"
year: 2023
authors: "Hu et al."
url: "https://arxiv.org/abs/2305.10276"
paper_type: "application"
primary_topic: "task-allocation"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "task-allocation"
evaluates:
  - "spatial reasoning"
  - "planning with symbolic traces"
  - "prompt efficiency"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain-of-Thought"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Chain-of-Symbol prompting replaces verbose natural-language reasoning traces with compact symbolic intermediate representations, especially for structured spatial reasoning tasks.

# Why It Matters
It is relevant to planning and reasoning in the vault because it shows that smaller, more structured intermediate representations can improve both reasoning quality and efficiency.

# Method / Setup
The paper converts chain-of-thought examples into symbolic forms for spatial planning and reasoning tasks such as Brick World, navigation, and manipulation, then compares symbolic prompting with natural-language CoT across models.

# Key Claims
- Symbolic intermediate representations can outperform natural-language CoT on structured spatial tasks.
- Compact symbolic reasoning can cut token use substantially while improving accuracy.
- Larger models appear better able to benefit from abstract symbolic reasoning traces.

# Limitations
- The benefits are demonstrated mainly on spatially structured reasoning tasks.
- The prompting style depends on manually designed symbolic formats and examples.

# Connections
- [[Task-Allocation]]
- `evaluates` spatial reasoning
- `evaluates` planning with symbolic traces
- `evaluates` prompt efficiency
- `builds_on_unresolved` Chain-of-Thought
<!-- GENERATED:END -->

## My Notes


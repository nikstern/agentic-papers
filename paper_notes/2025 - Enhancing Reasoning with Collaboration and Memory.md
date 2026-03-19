---
paper_id: 21
title: "Enhancing Reasoning with Collaboration and Memory"
year: 2025
authors: "Michelman et al."
url: "https://arxiv.org/abs/2503.05944"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "reasoning with memory"
  - "self-consistency"
  - "multi-agent reasoning"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain-of-Thought"
  - "Analogical Prompting"
  - "self-consistency"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---

# Summary
Enhancing Reasoning with Collaboration and Memory compares collaboration patterns and memory-retrieval strategies to test when external exemplars help reasoning and when random context can outperform similarity-based retrieval.

# Why It Matters
It is a useful bridge between the vault's memory and reasoning threads because it tests retrieval and collaboration choices directly instead of assuming similarity-based memory is optimal.

# Method / Setup
The study evaluates single-agent prompting, self-consistency, varied-context prompting, and summarizer-agent collaboration across reasoning tasks, and compares frozen versus learned memory banks with random and similarity-based retrieval.

# Key Claims
- Randomly varied exemplars can outperform similarity-based memory retrieval in some reasoning settings.
- Frozen memory can be as effective as incrementally learned memory while being cheaper to maintain.
- Reasoning, collaboration, and memory design interact in non-obvious ways.

# Limitations
- The experiments cover a limited set of models and reasoning tasks.
- The gains from more elaborate collaboration strategies are sensitive to base model quality.

# Connections
- [[Memory Context]]
- `evaluates` reasoning with memory
- `evaluates` self-consistency
- `evaluates` multi-agent reasoning
- `builds_on_unresolved` Chain-of-Thought
- `builds_on_unresolved` Analogical Prompting
- `builds_on_unresolved` self-consistency

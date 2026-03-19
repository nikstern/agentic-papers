---
paper_id: 34
title: "Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models"
year: 2024
authors: "Yang et al."
url: "https://arxiv.org/abs/2406.04271"
paper_type: "system"
primary_topic: "memory-context"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "memory-context"
evaluates:
  - "reasoning templates"
  - "memory-augmented reasoning"
  - "reasoning efficiency"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain-of-Thought"
  - "Tree of Thoughts"
compares_to_unresolved:
  - "Graph of Thoughts"
  - "Meta Prompting"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Buffer of Thoughts equips LLMs with a meta-buffer of distilled thought templates that can be retrieved and adapted for new reasoning problems.

# Why It Matters
It is a useful memory-reasoning bridge paper because it treats reusable reasoning structures as a memory object, not just a prompt artifact.

# Method / Setup
The framework distills high-level thought templates from solved problems, stores them in a meta-buffer, retrieves relevant templates for new tasks, and updates the buffer over time through a buffer manager.

# Key Claims
- Reusable thought templates improve accuracy, efficiency, and robustness on reasoning tasks.
- Smaller models can approach or exceed larger-model performance when paired with a strong thought buffer.
- Problem distillation and memory of reasoning patterns are both critical components.

# Limitations
- The system depends on the quality of distilled templates and retrieval.
- Creative or poorly structured tasks may benefit less than structured reasoning benchmarks.

# Connections
- [[Memory-Context]]
- `evaluates` reasoning templates
- `evaluates` memory-augmented reasoning
- `evaluates` reasoning efficiency
- `builds_on_unresolved` Chain-of-Thought
- `builds_on_unresolved` Tree of Thoughts
- `compares_to_unresolved` Graph of Thoughts
- `compares_to_unresolved` Meta Prompting
<!-- GENERATED:END -->

## My Notes


---
paper_id: 68
title: "A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models"
year: 2024
authors: "Tonmoy et al."
url: "https://arxiv.org/abs/2401.01313"
paper_type: "survey"
primary_topic: "hallucination-factuality"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "hallucination-factuality"
evaluates:
  - "hallucination mitigation techniques"
  - "retrieval-augmented generation"
  - "self-refinement and verification methods"
  - "fine-tuning and decoding interventions"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Survey of Hallucination in Natural Language Generation"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey categorizes LLM hallucination mitigation methods across prompt engineering, retrieval augmentation, self-refinement, decoding, knowledge-graph grounding, faithfulness-aware objectives, and supervised fine-tuning. It emphasizes practical mitigation choices and the tradeoffs that limit current systems.

# Why It Matters
It gives the vault a mitigation-focused overview rather than a general hallucination survey, which is useful for intervention design.

# Method / Setup
Survey of more than thirty hallucination mitigation techniques, organized into prompt engineering and model-development approaches with task settings, datasets, metrics, evaluated models, and reported limitations.

# Key Claims
- Retrieval-augmented generation is a dominant mitigation family, but its effectiveness depends heavily on retrieval quality and grounding fidelity.
- Self-refinement and verification-style prompting can reduce hallucinations without retraining the base model.
- No single mitigation approach is sufficient across tasks, and cost, domain dependence, and evaluation difficulty remain major bottlenecks.

# Limitations
- It is a survey rather than a head-to-head empirical benchmark under one unified experimental protocol.
- Many reviewed methods increase inference cost or depend on external resources, which the paper identifies as an unresolved practical constraint.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` hallucination mitigation techniques
- `evaluates` retrieval-augmented generation
- `evaluates` self-refinement and verification methods
- `evaluates` fine-tuning and decoding interventions
- `builds_on_unresolved` Survey of Hallucination in Natural Language Generation
<!-- GENERATED:END -->

## My Notes


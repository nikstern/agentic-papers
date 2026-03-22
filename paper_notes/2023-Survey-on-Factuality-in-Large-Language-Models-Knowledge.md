---
paper_id: 69
title: "Survey on Factuality in Large Language Models: Knowledge, Retrieval and Domain-Specificity"
year: 2023
authors: "Wang et al."
url: "https://arxiv.org/abs/2310.07521"
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
  - "factuality evaluation metrics"
  - "factuality benchmarks"
  - "retrieval-augmented generation"
  - "domain-specific factuality"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "A Survey of Large Language Models"
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey studies factuality in LLMs through knowledge, retrieval, and domain-specific reliability, separating factuality issues from broader hallucination framing while reviewing evaluation, causes, and enhancement methods. It covers both standalone LLMs and retrieval-augmented systems.

# Why It Matters
It complements hallucination surveys by centering factual reliability and domain-grounded evaluation, especially for high-stakes use cases.

# Method / Setup
Survey paper reviewing factuality definitions, evaluation metrics and benchmarks, causes of factual errors at model, retrieval, and inference levels, and methods to improve factuality in standalone, retrieval-augmented, and domain-specific LLMs.

# Key Claims
- Factuality problems in LLMs stem from model knowledge gaps, retrieval failures, and inference-time error propagation rather than a single failure source.
- Reliable factuality evaluation requires broader metrics and domain-specific benchmarks, not just generic generation scores.
- Improving factuality often requires combining retrieval, adaptation, and domain-specific training rather than relying on prompting alone.

# Limitations
- It is broad and synthetic, so it does not provide a single unified empirical comparison of factuality interventions.
- Its emphasis is on factuality as a broader reliability problem, which means some pure hallucination-detection threads are only one part of the coverage.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` factuality evaluation metrics
- `evaluates` factuality benchmarks
- `evaluates` retrieval-augmented generation
- `evaluates` domain-specific factuality
- `builds_on_unresolved` A Survey of Large Language Models
<!-- GENERATED:END -->

## My Notes


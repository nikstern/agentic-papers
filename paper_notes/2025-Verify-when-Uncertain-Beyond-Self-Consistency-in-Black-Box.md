---
paper_id: 73
title: "Verify when Uncertain: Beyond Self-Consistency in Black Box Hallucination Detection"
year: 2025
authors: "Xue et al."
url: "https://arxiv.org/abs/2502.15845"
paper_type: "application"
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
  - "SQuAD"
  - "TriviaQA"
  - "Natural Questions"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Detecting Hallucinations in Large Language Models Using Semantic Entropy"
compares_to_unresolved:
  - "Detecting Hallucinations in Large Language Models Using Semantic Entropy"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper studies black-box hallucination detection and argues that self-consistency methods are near their performance ceiling unless they are augmented with verifier models. It introduces a budget-aware two-stage method that selectively uses cross-model verification when the target model appears uncertain.

# Why It Matters
It is a useful recent empirical paper because it reframes hallucination detection as a cost-aware verification problem rather than only a self-consistency problem.

# Method / Setup
Black-box hallucination detection study across SQuAD, TriviaQA, and Natural Questions using self-consistency and cross-model consistency, with AUROC and AURAC evaluation plus a budget-aware two-stage algorithm that queries a verifier only for uncertain cases.

# Key Claims
- Existing self-consistency methods are already close to their standalone performance ceiling.
- Cross-model consistency substantially improves black-box hallucination detection over self-consistency alone.
- A two-stage verify-when-uncertain policy captures most of the performance gain while cutting verifier cost.

# Limitations
- The method still depends on access to an additional verifier model, so it adds cost and system complexity.
- The empirical focus is on black-box QA-style settings rather than every generation task where hallucinations appear.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` SQuAD
- `evaluates` TriviaQA
- `evaluates` Natural Questions
- `builds_on_unresolved` Detecting Hallucinations in Large Language Models Using Semantic Entropy
- `compares_to_unresolved` Detecting Hallucinations in Large Language Models Using Semantic Entropy
<!-- GENERATED:END -->

## My Notes


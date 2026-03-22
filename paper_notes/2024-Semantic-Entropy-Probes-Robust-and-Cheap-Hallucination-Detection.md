---
paper_id: 72
title: "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs"
year: 2024
authors: "Farquhar et al."
url: "https://arxiv.org/abs/2406.15927"
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
  - "BioASQ"
  - "TriviaQA"
  - "Natural Questions Open"
  - "SQuAD"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Detecting Hallucinations in Large Language Models Using Semantic Entropy"
  - "Language Models (Mostly) Know What They Know"
compares_to_unresolved:
  - "Detecting Hallucinations in Large Language Models Using Semantic Entropy"
  - "Language Models (Mostly) Know What They Know"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes Semantic Entropy Probes, a cheap hallucination detector that predicts semantic uncertainty directly from LLM hidden states rather than sampling many generations. It aims to keep the robustness of semantic-entropy-style uncertainty signals while cutting inference cost substantially.

# Why It Matters
It is a strong empirical detection paper because it shows a practical uncertainty-based detector with better cross-domain generalization than simpler probing baselines.

# Method / Setup
Linear probes trained on hidden states to predict binarized semantic entropy, evaluated for hallucination detection across BioASQ, TriviaQA, Natural Questions Open, and SQuAD on models including Llama-2, Llama-3, Mistral, and Phi-3.

# Key Claims
- Hidden states encode semantic uncertainty strongly enough for simple probes to detect likely hallucinations.
- Semantic Entropy Probes generalize better across datasets than direct accuracy probes.
- Useful hallucination signals can be extracted before generation or from late hidden states with a single forward pass.

# Limitations
- The method still underperforms full multi-sample semantic entropy and requires semantic-entropy labels for probe training.
- The evaluation is centered on question answering rather than broader tasks like summarization or open-ended generation.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` BioASQ
- `evaluates` TriviaQA
- `evaluates` Natural Questions Open
- `evaluates` SQuAD
- `builds_on_unresolved` Detecting Hallucinations in Large Language Models Using Semantic Entropy
- `builds_on_unresolved` Language Models (Mostly) Know What They Know
- `compares_to_unresolved` Detecting Hallucinations in Large Language Models Using Semantic Entropy
- `compares_to_unresolved` Language Models (Mostly) Know What They Know
<!-- GENERATED:END -->

## My Notes


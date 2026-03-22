---
paper_id: 70
title: "The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models"
year: 2024
authors: "Li et al."
url: "https://arxiv.org/abs/2401.03205"
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
  - "HaluEval 2.0"
  - "biomedicine QA"
  - "finance QA"
  - "science QA"
  - "education QA"
  - "open-domain QA"
builds_on:
  - "[[2023-A-Survey-on-Hallucination-in-Large-Language-Models]]"
compares_to: []
builds_on_unresolved:
  - "HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models"
compares_to_unresolved:
  - "Alpaca"
  - "Vicuna"
  - "Llama 2-Chat"
  - "ChatGPT"
  - "Claude"
  - "Claude 2"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper is an empirical study of factuality hallucination in LLMs that analyzes detection, sources, and mitigation across domains, training stages, and inference choices. It introduces HaluEval 2.0 and studies how pre-training data, fine-tuning, decoding, retrieval, and self-reflection affect hallucination rates.

# Why It Matters
It is a strong empirical anchor paper because it studies where hallucinations come from and how much common interventions help under different conditions.

# Method / Setup
Empirical evaluation on HaluEval 2.0 with 8,770 questions across biomedicine, finance, science, education, and open-domain settings, using GPT-4-based fact extraction and fact judgment together with micro and macro hallucination rates.

# Key Claims
- Increasing pre-training scale alone only marginally reduces hallucinations, while domain-relevant data composition matters much more.
- Supervised fine-tuning, retrieval augmentation, and self-reflection can reduce hallucinations, but their effectiveness depends strongly on domain and model size.
- Decoding choices create different hallucination tradeoffs, with diversity-oriented decoding often hurting professional domains and greedy decoding hurting open-ended settings.

# Limitations
- The authors note limited visibility into proprietary training details and constrained ability to fully analyze pre-training and supervised fine-tuning choices.
- The paper studies mitigation empirically but does not introduce a fundamentally new mitigation method.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` HaluEval 2.0
- `evaluates` biomedicine QA
- `evaluates` finance QA
- `evaluates` science QA
- `evaluates` education QA
- `evaluates` open-domain QA
- `builds_on` [[2023-A-Survey-on-Hallucination-in-Large-Language-Models]]
- `builds_on_unresolved` HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models
- `compares_to_unresolved` Alpaca
- `compares_to_unresolved` Vicuna
- `compares_to_unresolved` Llama 2-Chat
- `compares_to_unresolved` ChatGPT
- `compares_to_unresolved` Claude
- `compares_to_unresolved` Claude 2
<!-- GENERATED:END -->

## My Notes


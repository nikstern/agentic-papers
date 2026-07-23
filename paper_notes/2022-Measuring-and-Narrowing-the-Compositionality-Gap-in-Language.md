---
paper_id: 118
title: "Measuring and Narrowing the Compositionality Gap in Language Models"
year: 2022
authors: "Press et al."
url: "https://arxiv.org/abs/2210.03350"
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
  - "GPT-3 family models (including InstructGPT) on multi-hop compositional question answering."
  - "Direct prompting, chain of thought prompting, self-ask prompting, and self-ask plus search engine methods."
  - "Performance on newly introduced Compositional Celebrities, Bamboogle, 2WikiMultiHopQA, and Musique datasets."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain of thought prompting methods for eliciting reasoning in large language models."
  - "Multi-hop question answering benchmarks like 2WikiMultiHopQA and Musique."
  - "Prior works exploring decomposing complex tasks into simpler sub-tasks for question answering."
compares_to_unresolved:
  - "Least-to-most prompting method requiring multiple model passes to answer compositional queries."
  - "Search engine retrieval alone and with LM postprocessing for open-domain question answering."
  - "Other decompositional methods that require supervised models or fine-tuning versus self-ask's zero-shot/few-shot approach."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces the compositionality gap metric to quantify large language models' (LMs) limitations in compositional reasoning, demonstrating that despite improvements in single-hop factual recall with scale, multi-hop compositional performance lags behind. It introduces self-ask, an elicitive prompting technique that explicitly decomposes questions into sub-questions to narrow this gap, and shows further improvements when integrating a search engine.

# Why It Matters
Understanding and reducing the compositionality gap is crucial for building language models capable of multi-step reasoning beyond memorization, enabling more reliable and explainable AI systems that can handle complex queries requiring factual composition.

# Method / Setup
The authors constructed the Compositional Celebrities dataset consisting of 8.6k two-hop compositional questions unlikely to have appeared jointly in training, then measured model performance on single-hop sub-questions and full compositions using GPT-3 variants, comparing direct prompting, chain of thought, self-ask prompting, and self-ask combined with search engine retrieval.

# Key Claims
- The compositionality gap remains roughly constant (~40%) across GPT-3 model sizes, indicating scale alone does not improve compositional reasoning.
- Elicitive prompts like chain of thought narrow the compositionality gap by enabling explicit intermediate reasoning steps.
- Self-ask prompting outperforms chain of thought by explicitly producing and answering sub-questions before giving the final answer.
- Integrating a search engine to answer sub-questions further improves accuracy, leveraging external up-to-date knowledge without model fine-tuning.
- Self-ask is effective across multiple datasets including Compositional Celebrities, 2WikiMultiHopQA, Musique, and the manually constructed Bamboogle dataset.

# Limitations
- Experiments are limited to 2-hop English question-answering datasets; generalization to other languages, reasoning types, or more hops remains untested.
- Models larger than 175 billion parameters were not evaluated; future models might exhibit different compositional behaviors.
- Evaluation relies on automatically and manually constructed datasets that may not capture all forms of compositional reasoning challenges.
- Integration with search engines depends on the search quality and API availability, affecting reproducibility and applicability.

# Connections
- [[Agent-Evaluation]]
- `evaluates` GPT-3 family models (including InstructGPT) on multi-hop compositional question answering.
- `evaluates` Direct prompting, chain of thought prompting, self-ask prompting, and self-ask plus search engine methods.
- `evaluates` Performance on newly introduced Compositional Celebrities, Bamboogle, 2WikiMultiHopQA, and Musique datasets.
- `builds_on_unresolved` Chain of thought prompting methods for eliciting reasoning in large language models.
- `builds_on_unresolved` Multi-hop question answering benchmarks like 2WikiMultiHopQA and Musique.
- `builds_on_unresolved` Prior works exploring decomposing complex tasks into simpler sub-tasks for question answering.
- `compares_to_unresolved` Least-to-most prompting method requiring multiple model passes to answer compositional queries.
- `compares_to_unresolved` Search engine retrieval alone and with LM postprocessing for open-domain question answering.
- `compares_to_unresolved` Other decompositional methods that require supervised models or fine-tuning versus self-ask's zero-shot/few-shot approach.
<!-- GENERATED:END -->

## My Notes


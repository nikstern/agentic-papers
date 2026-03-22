---
paper_id: 71
title: "Chain-of-Verification Reduces Hallucination in Large Language Models"
year: 2023
authors: "Dhuliawala et al."
url: "https://arxiv.org/abs/2309.11495"
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
  - "Wikidata list QA"
  - "Wiki-Category list generation"
  - "MultiSpanQA"
  - "biography generation"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
compares_to_unresolved:
  - "Llama 2 Chat"
  - "ChatGPT"
  - "PerplexityAI"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes Chain-of-Verification, a prompting pipeline where an LLM drafts an answer, plans verification questions, answers them, and then revises the response using those checks. It shows that structured self-verification reduces hallucinated facts across list QA, closed-book QA, and long-form generation.

# Why It Matters
It is one of the clearest empirical demonstrations that explicit self-verification can materially reduce factual hallucination at inference time.

# Method / Setup
Inference-time prompting pipeline evaluated on Wikidata list questions, Wiki-Category list generation, MultiSpanQA, and long-form biography generation, comparing standard prompting against several verification variants including factored and factor-plus-revise execution.

# Key Claims
- Separating verification from the original draft and answering verification questions independently reduces factual hallucination substantially.
- The model is often better at answering short verification questions correctly than at stating the same facts accurately in an unconstrained long-form draft.
- Chain-of-Verification improves precision and factuality on QA and biography generation, outperforming strong baseline prompting setups.

# Limitations
- The method increases inference cost because it requires multiple extra generations for planning, checking, and revising.
- It targets factual inaccuracies and does not eliminate other failure modes such as broader reasoning or opinion errors.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` Wikidata list QA
- `evaluates` Wiki-Category list generation
- `evaluates` MultiSpanQA
- `evaluates` biography generation
- `builds_on_unresolved` Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- `compares_to_unresolved` Llama 2 Chat
- `compares_to_unresolved` ChatGPT
- `compares_to_unresolved` PerplexityAI
<!-- GENERATED:END -->

## My Notes


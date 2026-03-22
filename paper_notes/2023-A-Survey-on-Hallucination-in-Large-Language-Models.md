---
paper_id: 67
title: "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions"
year: 2023
authors: "Huang et al."
url: "https://arxiv.org/abs/2311.05232"
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
  - "hallucination taxonomies"
  - "hallucination detection methods"
  - "hallucination mitigation strategies"
  - "retrieval-augmented generation failure modes"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Survey of Hallucination in Natural Language Generation"
  - "Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models"
compares_to_unresolved:
  - "Survey of Hallucination in Natural Language Generation"
  - "Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This survey organizes LLM hallucinations into factuality and faithfulness failures, then reviews causes, detection methods, benchmarks, and mitigation strategies. It also analyzes where retrieval-augmented systems still fail to eliminate hallucinations.

# Why It Matters
It is a strong general reference for the hallucination landscape and gives the vault a clear taxonomy plus a cause-to-mitigation framing.

# Method / Setup
Survey paper synthesizing prior work on hallucination taxonomy, causes across data/training/inference stages, detection methods, benchmarks, mitigation methods, and retrieval-augmented generation failure modes.

# Key Claims
- LLM hallucinations are better understood through a split between factuality hallucination and faithfulness hallucination.
- Hallucinations arise from interacting causes across data quality, training procedures, and inference-time decoding or reasoning failures.
- Retrieval augmentation helps but still fails through retrieval errors, noisy context, and weak contextual alignment during generation.

# Limitations
- As a survey, it synthesizes prior results rather than introducing a new empirical mitigation method.
- The coverage is strongest for text LLMs and earlier retrieval-augmented systems rather than every newer application setting.

# Connections
- [[Hallucination-Factuality]]
- `evaluates` hallucination taxonomies
- `evaluates` hallucination detection methods
- `evaluates` hallucination mitigation strategies
- `evaluates` retrieval-augmented generation failure modes
- `builds_on_unresolved` Survey of Hallucination in Natural Language Generation
- `builds_on_unresolved` Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models
- `compares_to_unresolved` Survey of Hallucination in Natural Language Generation
- `compares_to_unresolved` Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models
<!-- GENERATED:END -->

## My Notes


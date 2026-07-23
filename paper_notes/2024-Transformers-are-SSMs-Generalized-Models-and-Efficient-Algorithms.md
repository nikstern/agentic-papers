---
paper_id: 102
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
year: 2024
authors: "Dao and Gu"
url: "https://arxiv.org/abs/2405.21060"
paper_type: "position"
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
  - "Language modeling tasks comparing Mamba-2 and Transformer performance."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Selective State Space Models (Mamba)"
compares_to_unresolved:
  - "Transformer architectures"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper reveals strong theoretical connections between Transformers and state-space models (SSMs), introducing a unified framework via structured state space duality (SSD). It develops Mamba-2, a refined selective SSM architecture achieving 2-8X speedups with competitive language modeling performance.

# Why It Matters
Understanding the duality between Transformers and SSMs can lead to more efficient and scalable architectures for sequence modeling, advancing deep learning capabilities in language understanding.

# Method / Setup
The authors analyze decompositions of structured semiseparable matrices to establish formal duality between attention-based models and SSMs, culminating in the design and evaluation of the Mamba-2 model for language modeling tasks.

# Key Claims
- Transformers and SSMs are closely related through structured semiseparable matrices.
- The state space duality framework unifies and generalizes variants of attention and SSMs.
- Mamba-2, leveraging SSD, is 2-8X faster than previous selective SSMs while maintaining competitive performance on language modeling.

# Limitations
- The analysis and experiments focus primarily on small to medium scale tasks, leaving large-scale generalization unaddressed.
- The practical deployment and robustness of Mamba-2 in diverse language modeling scenarios require more validation.

# Connections
- [[Memory-Context]]
- `evaluates` Language modeling tasks comparing Mamba-2 and Transformer performance.
- `builds_on_unresolved` Selective State Space Models (Mamba)
- `compares_to_unresolved` Transformer architectures
<!-- GENERATED:END -->

## My Notes


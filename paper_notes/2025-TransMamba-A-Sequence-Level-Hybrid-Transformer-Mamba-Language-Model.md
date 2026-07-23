---
paper_id: 98
title: "TransMamba: A Sequence-Level Hybrid Transformer-Mamba Language Model"
year: 2025
authors: "Li et al."
url: "https://arxiv.org/abs/2503.24067"
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
  - "Transformer"
  - "Mamba2"
  - "Hybrid"
  - "TransMamba"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Transformer architectures"
  - "Mamba and State Space Models"
  - "Hybrid Transformer-Mamba models"
  - "Consistency of Attention and SSM duality"
compares_to_unresolved:
  - "Transformer"
  - "Mamba2"
  - "Hybrid Transformer-Mamba models"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
TransMamba is a novel language model framework that unifies Transformer and Mamba (a state space model) by sharing parameter matrices and dynamically switching between attention and SSM mechanisms at different token lengths and layers, enabled by a Memory Converter for lossless information flow and a TransPoint schedule for efficiency and performance trade-off.

# Why It Matters
It addresses the computational inefficiency of Transformers in long-sequence processing and the unstable contextual learning of Mamba by combining their complementary strengths, achieving superior training efficiency and performance for next-generation language modeling.

# Method / Setup
TransMamba uses shared QKV/CBx parameters between Transformer and Mamba, applies attention before a layer-specific token position called TransPoint, then switches to SSM after; a theoretical Memory Converter transforms attention outputs to SSM states without information loss, and flexible TransPoint scheduling balances effectiveness and efficiency across layers and sequence lengths.

# Key Claims
- Transformer and Mamba share a deeper mathematical consistency allowing unified parameterization.
- Memory Converter enables lossless transition between attention and SSM mechanisms at TransPoints.
- Flexible TransPoint scheduling across layers improves training efficiency and model performance.
- TransMamba achieves better or comparable accuracy than Transformer, Mamba, and hybrid baselines on diverse tasks, including long-context benchmarks.
- Training and inference TransPoint schedules can differ, allowing flexible inference strategies without major performance loss.

# Limitations
- Current experiments limited to model sizes up to 1.5B parameters; scaling laws remain unexplored.
- Optimal TransPoint positions depend on engineering optimization and may be further refined.
- Variants of Transformer and Mamba were not combined, limiting exploration of hybrid variants.

# Connections
- [[Memory-Context]]
- `evaluates` Transformer
- `evaluates` Mamba2
- `evaluates` Hybrid
- `evaluates` TransMamba
- `builds_on_unresolved` Transformer architectures
- `builds_on_unresolved` Mamba and State Space Models
- `builds_on_unresolved` Hybrid Transformer-Mamba models
- `builds_on_unresolved` Consistency of Attention and SSM duality
- `compares_to_unresolved` Transformer
- `compares_to_unresolved` Mamba2
- `compares_to_unresolved` Hybrid Transformer-Mamba models
<!-- GENERATED:END -->

## My Notes


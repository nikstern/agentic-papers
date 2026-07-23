---
paper_id: 100
title: "Jamba: A Hybrid Transformer-Mamba Language Model"
year: 2024
authors: "Lieber et al."
url: "https://arxiv.org/abs/2403.19887"
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
  - "Standard language model academic benchmarks including HellaSwag, WinoGrande, ARC, PIQA, BoolQ, QuAC, GSM8K, HumanEval, MMLU, and BBH."
  - "Long-context synthetic needle-in-a-haystack tasks up to 256K tokens."
  - "Naturalistic few-shot classification tasks with large label spaces."
  - "Long-context question answering benchmarks including NarrativeQA, LongFQA, Natural Questions, CUAD, and SFiction."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Transformer architecture limitations on long context and compute."
  - "Recent state-space models like Mamba for efficient sequence modeling."
  - "Mixture-of-experts (MoE) sparsity for scaling model capacity."
  - "Prior hybrid attempts combining SSMs and attention layers at smaller scales."
  - "Challenges in training large-scale hybrid architectures without positional embeddings."
compares_to_unresolved:
  - "Mixtral-8x7B as a comparable mixture-of-experts Transformer baseline."
  - "Llama-2 13B and 70B models for size and performance comparisons."
  - "Pure Transformer and pure Mamba models for architectural ablations."
  - "Other hybrid models like H3, Hyena, and StripedHyena with smaller or less effective hybrid designs."
  - "State-space augmented transformers attempts for combining SSM and attention."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
Jamba is a large language model using a hybrid Transformer-Mamba mixture-of-experts architecture aimed at efficient large-context processing. It combines Transformer and state-space Mamba layers with MoE modules to optimize throughput, memory usage, and scaling up to 256K token contexts.

# Why It Matters
Jamba demonstrates that hybrid architectures can achieve state-of-the-art performance comparable to pure Transformer models while enabling significantly longer context lengths with less memory overhead, supporting more efficient inference and training.

# Method / Setup
Jamba interleaves Transformer and Mamba layers at a 1:7 ratio, applies MoE to every other MLP layer with 16 experts using top-2 routing, and fits within a single 80GB GPU with int8 weights, enabling high throughput and long-context support. Training used 52B total params with 12B active params, leveraging RMSNorm for stability and no explicit positional encoding.

# Key Claims
- Hybrid Transformer-Mamba architecture outperforms pure Transformer or pure Mamba models on benchmarks.
- MoE integration improves capacity without increasing active compute significantly.
- Jamba supports context lengths up to 256K tokens with drastically reduced KV cache size relative to Transformers.
- Despite fewer attention layers, Jamba retains strong in-context learning capabilities similar to Transformers.
- Jamba achieves 3x throughput of comparable models like Mixtral, especially for long-context inputs.

# Limitations
- Jamba base model is not instruction-tuned, aligned, or moderated and thus unsuitable for direct production use.
- Current Jamba implementation uses specific hyperparameters tailored for single 80GB GPU setups; other configurations are unexplored.
- No evidence yet that pure Mamba layers alone support induction mechanisms required for in-context learning; the hybrid model relies on attention layers for this.
- Comparisons are primarily with few recent state-of-the-art open models; broader evaluation is limited.
- The production-grade system is released only with base pretraining, leaving downstream fine-tuning and application open for future work.

# Connections
- [[Memory-Context]]
- `evaluates` Standard language model academic benchmarks including HellaSwag, WinoGrande, ARC, PIQA, BoolQ, QuAC, GSM8K, HumanEval, MMLU, and BBH.
- `evaluates` Long-context synthetic needle-in-a-haystack tasks up to 256K tokens.
- `evaluates` Naturalistic few-shot classification tasks with large label spaces.
- `evaluates` Long-context question answering benchmarks including NarrativeQA, LongFQA, Natural Questions, CUAD, and SFiction.
- `builds_on_unresolved` Transformer architecture limitations on long context and compute.
- `builds_on_unresolved` Recent state-space models like Mamba for efficient sequence modeling.
- `builds_on_unresolved` Mixture-of-experts (MoE) sparsity for scaling model capacity.
- `builds_on_unresolved` Prior hybrid attempts combining SSMs and attention layers at smaller scales.
- `builds_on_unresolved` Challenges in training large-scale hybrid architectures without positional embeddings.
- `compares_to_unresolved` Mixtral-8x7B as a comparable mixture-of-experts Transformer baseline.
- `compares_to_unresolved` Llama-2 13B and 70B models for size and performance comparisons.
- `compares_to_unresolved` Pure Transformer and pure Mamba models for architectural ablations.
- `compares_to_unresolved` Other hybrid models like H3, Hyena, and StripedHyena with smaller or less effective hybrid designs.
- `compares_to_unresolved` State-space augmented transformers attempts for combining SSM and attention.
<!-- GENERATED:END -->

## My Notes


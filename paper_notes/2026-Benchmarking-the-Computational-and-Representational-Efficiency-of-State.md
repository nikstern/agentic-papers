---
paper_id: 95
title: "Benchmarking the Computational and Representational Efficiency of State Space Models against Transformers on Long-Context Dyadic Sessions"
year: 2026
authors: "Koledoye et al."
url: "https://arxiv.org/abs/2601.01237"
paper_type: "benchmark"
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
  - "Mamba State Space Model (SSM) architecture"
  - "LLaMA Transformer architecture"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Jelassi et al. 2024 on representational trade-offs between SSMs and Transformers"
  - "Gu and Dao 2023 on Mamba architecture\u2019s efficiency"
  - "Waleffe et al. 2024 benchmarking SSMs and Transformers at scale"
compares_to_unresolved:
  - "Transformer architectures with quadratic memory scaling (e.g., LLaMA)"
  - "State Space Models applied to long-context sequence modeling"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This study benchmarks Mamba State Space Models (SSMs) against LLaMA Transformers on long-context dyadic therapy sessions, evaluating computational and representational efficiency across sequence lengths from 512 to 8,192 tokens. Empirical results demonstrate Mamba's superior linear scaling in memory and inference time, alongside richer context utilization and better dynamic shift detection.

# Why It Matters
Efficient long-context sequence modeling is critical for applications like clinical NLP, where processing extended interactions without truncation is necessary; understanding trade-offs between SSM and Transformer architectures guides optimal model choice for such domains.

# Method / Setup
Using synthetic dyadic therapy transcripts, both 50M-parameter Mamba SSM and LLaMA Transformer models were evaluated on identical inputs, measuring GPU memory, inference time, hidden state dynamics, attention patterns, and effective context utilization across multiple sequence lengths up to 8,192 tokens.

# Key Claims
- Mamba achieves up to 12.46× memory efficiency and 10.67× faster inference than LLaMA Transformers at 4,096 tokens.
- SSMs scale linearly (O(N)) in computational resources, whereas Transformers scale quadratically (O(N²)), limiting Transformer's maximum context length due to memory constraints.
- Mamba utilizes approximately 90.2% of the sequence context with a mean effective range of 892 tokens compared to Transformer’s 12.7% and 235 tokens, demonstrating superior long-range context capture.
- SSMs provide more stable hidden state dynamics and better detection of dynamic shifts in therapeutic sessions (AUC-ROC 0.7834 vs 0.7123).
- Transformers offer interpretable token-level attention mechanisms and excel in associative recall tasks but struggle with long-context scalability.

# Limitations
- Evaluation uses synthetic therapy session data which may not fully capture real-world complexities.
- Models were randomly initialized without pretraining, so results do not reflect downstream task performance or pretrained model behavior.
- Transformer evaluation limited to 8,192 tokens due to hardware constraints, potentially biasing comparative results.
- Study focuses on a single SSM variant (Mamba) and one Transformer architecture (LLaMA), limiting generalization to other models.

# Connections
- [[Memory-Context]]
- `evaluates` Mamba State Space Model (SSM) architecture
- `evaluates` LLaMA Transformer architecture
- `builds_on_unresolved` Jelassi et al. 2024 on representational trade-offs between SSMs and Transformers
- `builds_on_unresolved` Gu and Dao 2023 on Mamba architecture’s efficiency
- `builds_on_unresolved` Waleffe et al. 2024 benchmarking SSMs and Transformers at scale
- `compares_to_unresolved` Transformer architectures with quadratic memory scaling (e.g., LLaMA)
- `compares_to_unresolved` State Space Models applied to long-context sequence modeling
<!-- GENERATED:END -->

## My Notes


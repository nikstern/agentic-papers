---
paper_id: 150
title: "Unified Training of Universal Time Series Forecasting Transformers"
year: 2024
authors: "Woo et al."
url: "https://arxiv.org/abs/2402.02592"
paper_type: "system"
primary_topic: "medical-time-series"
secondary_topics: []
status: "ingested"
priority: "0"
last_read: ""
enrichment_status: "enriched"
tags:
  - "papers"
  - "medical-time-series"
evaluates:
  - "Monash Time Series Forecasting Benchmark datasets for in-distribution evaluation."
  - "Multiple unseen datasets across energy, transport, climate, sales, and healthcare domains for zero-shot probabilistic forecasting."
  - "Long sequence forecasting benchmark datasets excluding overlap with LOTSA sources."
  - "Comparison against full-shot baselines including DeepAR, PatchTST, TiDE, TFT, AutoARIMA, and Seasonal Naive."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "TimeGPT-1 zero-shot forecasting model but lacking flexible probabilistic output."
  - "ForecastPFN synthetic-data trained zero-shot forecasting specialized to low-data settings."
  - "Lag-llama foundation model for forecasting using LLaMA architecture with restricted distribution heads."
  - "TimesFM decoder-only patch-based forecasting model without flexible distributions."
  - "TTM (Tiny Time Mixers) light mixture architectures for zero-shot forecasting."
  - "LLMTime leveraging large language models for time series as strings with categorical distributions."
compares_to_unresolved:
  - "DeepAR autoregressive recurrent network (Salinas et al. 2020) for probabilistic forecasting."
  - "PatchTST transformer-based model treating each variate independently."
  - "TiDE time series dense encoder for long-term forecasting."
  - "Temporal Fusion Transformer (TFT) for multi-horizon forecasting."
  - "AutoARIMA and Seasonal Naive classical statistical baselines."
  - "iTransformer, TimesNet, Crossformer, DLinear, SCINet and FEDformer for long sequence forecasting tasks."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
The paper introduces Moirai, a masked encoder-based universal transformer model for time series forecasting trained on LOTSA, a large-scale heterogeneous time series archive with over 27 billion observations from nine domains. Moirai addresses unique challenges of universal forecasting—including cross-frequency learning, arbitrary variate number handling, and flexible distribution modeling—achieving competitive or superior zero-shot forecasting performance compared to specialized full-shot models.

# Why It Matters
Traditional deep learning forecasting is constrained to one-model-per-dataset, limiting generalization and adaptability; Moirai demonstrates the feasibility of a single large model capable of universal time series forecasting across diverse datasets and domains, enabling efficiency and broad applicability without retraining per task.

# Method / Setup
Moirai employs multi patch size input/output projection layers to capture different frequency patterns, an Any-variate Attention mechanism enabling arbitrary multivariate inputs with permutation properties, and a mixture of parametric distributions for flexible probabilistic forecasting. It is pretrained on the LOTSA dataset with varying context and prediction lengths via masked encoder architecture and optimized using negative log-likelihood of the mixture distribution.

# Key Claims
- Moirai handles multiple time series frequencies effectively via multi patch size projections.
- Any-variate Attention allows Moirai to process time series with arbitrary dimensions while respecting permutation invariances.
- Flexible mixture distribution modeling improves probabilistic forecast quality over simpler parametric heads.
- Training on the large, diverse LOTSA dataset enables Moirai to generalize zero-shot to unseen datasets competitively with full-shot specialized models.
- Sequence packing during training substantially increases effective batch size and performance.
- Moirai achieves state-of-the-art in-distribution and out-of-distribution forecasting across diverse datasets without fine-tuning.

# Limitations
- Limited hyperparameter tuning due to resource constraints may restrict current model performance.
- Heuristic multi patch size mapping lacks unified, principled approach.
- Current architecture scales less effectively to very high-dimensional time series inputs.
- Masked encoder architecture may limit extensions requiring full autoregressive modeling.
- LOTSA dataset, while large, could be expanded with more domain and frequency diversity.
- Multi-modality (e.g., integration of tabular or textual data) is not addressed yet.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Monash Time Series Forecasting Benchmark datasets for in-distribution evaluation.
- `evaluates` Multiple unseen datasets across energy, transport, climate, sales, and healthcare domains for zero-shot probabilistic forecasting.
- `evaluates` Long sequence forecasting benchmark datasets excluding overlap with LOTSA sources.
- `evaluates` Comparison against full-shot baselines including DeepAR, PatchTST, TiDE, TFT, AutoARIMA, and Seasonal Naive.
- `builds_on_unresolved` TimeGPT-1 zero-shot forecasting model but lacking flexible probabilistic output.
- `builds_on_unresolved` ForecastPFN synthetic-data trained zero-shot forecasting specialized to low-data settings.
- `builds_on_unresolved` Lag-llama foundation model for forecasting using LLaMA architecture with restricted distribution heads.
- `builds_on_unresolved` TimesFM decoder-only patch-based forecasting model without flexible distributions.
- `builds_on_unresolved` TTM (Tiny Time Mixers) light mixture architectures for zero-shot forecasting.
- `builds_on_unresolved` LLMTime leveraging large language models for time series as strings with categorical distributions.
- `compares_to_unresolved` DeepAR autoregressive recurrent network (Salinas et al. 2020) for probabilistic forecasting.
- `compares_to_unresolved` PatchTST transformer-based model treating each variate independently.
- `compares_to_unresolved` TiDE time series dense encoder for long-term forecasting.
- `compares_to_unresolved` Temporal Fusion Transformer (TFT) for multi-horizon forecasting.
- `compares_to_unresolved` AutoARIMA and Seasonal Naive classical statistical baselines.
- `compares_to_unresolved` iTransformer, TimesNet, Crossformer, DLinear, SCINet and FEDformer for long sequence forecasting tasks.
<!-- GENERATED:END -->

## My Notes


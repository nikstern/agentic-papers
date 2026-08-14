---
paper_id: 128
title: "Low-Rank Adaptation of Time Series Foundational Models for Out-of-Domain Modality Forecasting"
year: 2024
authors: "Gupta et al."
url: "https://arxiv.org/abs/2405.10216"
paper_type: "application"
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
  - "Lag-Llama"
  - "MOIRAI"
  - "Chronos"
  - "Bhatti et al. (2024b) state-of-the-art vital sign forecasting"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Low-Rank Adaptation (LoRA) for large language models (Hu et al. 2021)"
  - "Transformer architectures for time series forecasting (Vaswani et al. 2017)"
  - "Lag-Llama (Rasul et al. 2023)"
  - "MOIRAI (Woo et al. 2024)"
  - "Chronos (Ansari et al. 2024)"
compares_to_unresolved:
  - "Bhatti et al. (2024b) vital sign forecasting with N-BEATS, N-HiTS, TFT models"
  - "full fine-tuning of TSFMs"
  - "zero-shot application of TSFMs"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper investigates the use of Low-Rank Adaptation (LoRA) for fine-tuning pre-trained time series foundational models (Lag-Llama, MOIRAI, Chronos) for out-of-domain forecasting of ICU patient vital signs. LoRA adapts attention weight matrices with low-rank updates to efficiently incorporate domain-specific knowledge, improving forecasting performance with fewer trainable parameters compared to full fine-tuning.

# Why It Matters
Efficiently fine-tuning large foundational time series models on limited domain-specific data enables practical deployment in sensitive healthcare settings, allowing better vital sign forecasting for critical patients without retraining entire models, thus saving computational resources and preserving generalizability.

# Method / Setup
The study fine-tunes three transformer-based TSFMs pre-trained on large, diverse datasets using LoRA applied to the multi-head attention weight matrices (Query, Key, Value, Output) with rank 2 and scaling factor 16, targeting univariate vital sign forecasting on the eICU dataset; performance is compared across zero-shot, full fine-tuning, and LoRA fine-tuning using MSE, DTW, and MAPE metrics.

# Key Claims
- LoRA fine-tuning significantly improves forecasting performance compared to zero-shot and is competitive with or exceeds full fine-tuning results for vital signs.
- Chronos model variants fine-tuned with LoRA can match or surpass state-of-the-art models trained from scratch on vital sign forecasting.
- LoRA reduces the number of trainable parameters substantially, preserving pre-trained weights and enabling efficient domain adaptation.
- Performance gains plateau at a certain LoRA rank, with smaller models benefiting more noticeably from increased rank.
- Full fine-tuning sometimes degrades performance, especially for larger models like MOIRAI, likely due to heavy parameterization in patch embedding layers omitted in LoRA.

# Limitations
- The study is limited to univariate forecasting of vital signs and does not address multivariate time series adaptation.
- Comparison with state-of-the-art models is not fully equitable since foundational models leverage extensive pretraining on massive datasets, whereas SOTA models are trained from scratch on smaller datasets.
- Applicability of LoRA fine-tuning to multivariate or multimodal time series foundational models remains unexplored.
- Effects of combining multiple PEFT methods were not evaluated and planned for future work.
- The impact of LoRA on other vital signs or clinical tasks beyond sepsis patient vital sign forecasting was not assessed.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Lag-Llama
- `evaluates` MOIRAI
- `evaluates` Chronos
- `evaluates` Bhatti et al. (2024b) state-of-the-art vital sign forecasting
- `builds_on_unresolved` Low-Rank Adaptation (LoRA) for large language models (Hu et al. 2021)
- `builds_on_unresolved` Transformer architectures for time series forecasting (Vaswani et al. 2017)
- `builds_on_unresolved` Lag-Llama (Rasul et al. 2023)
- `builds_on_unresolved` MOIRAI (Woo et al. 2024)
- `builds_on_unresolved` Chronos (Ansari et al. 2024)
- `compares_to_unresolved` Bhatti et al. (2024b) vital sign forecasting with N-BEATS, N-HiTS, TFT models
- `compares_to_unresolved` full fine-tuning of TSFMs
- `compares_to_unresolved` zero-shot application of TSFMs
<!-- GENERATED:END -->

## My Notes


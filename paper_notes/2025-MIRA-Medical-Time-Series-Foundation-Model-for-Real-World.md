---
paper_id: 125
title: "MIRA: Medical Time Series Foundation Model for Real-World Health Data"
year: 2025
authors: "Li et al."
url: "https://arxiv.org/abs/2506.07584"
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
  - "zero-shot forecasting across diverse downstream clinical datasets including ICU monitoring, epidemiological surveillance, ECG and EEG signals, and pediatric waveform datasets."
  - "performance under varying missing data rates, showing robustness up to 90% missingness."
  - "impact of model components via ablation studies for CT-RoPE, MoE block, and Neural ODE extrapolation."
  - "scaling behavior across model sizes from 73M to 455M parameters."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Neural Ordinary Differential Equations for continuous dynamics modeling."
  - "Existing generalist time series foundation models like Time-MoE, Moirai, and Chronos that lack robust handling of medical time series irregularities."
  - "Prior medical time series models that focus on classification but not continuous forecasting or irregular sampling."
  - "The limited generalizability of prior medical time series foundation models confined to narrow domains."
compares_to_unresolved:
  - "Generalist time series foundation models including Time-MoE, Moirai, Moirai-MoE, TimesFM, Chronos, Moment, TimeGPT which require regular sampling or interpolation."
  - "Task-specific irregular time series models such as ContiFormer, T-PatchGNN, Neural-CDE, and ODE-RNN requiring fine-tuning."
  - "Encoder-only, encoder-decoder, and decoder-only architectures for time series modelling with varying scales and pretraining corpora."
  - "Emerging medical time series foundation models focusing on classification or specific domains (e.g., EEG sleep staging)."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
MIRA is a decoder-only foundation model tailored for irregular medical time series forecasting, integrating Continuous-Time Rotary Positional Encoding (CT-RoPE), a frequency-specific mixture-of-experts layer, and a Neural ODE-based Continuous Dynamics Extrapolation block. Pretrained on a large corpus of 454 billion medical time points from diverse public datasets, it achieves superior zero-shot performance compared to state-of-the-art baselines across multiple clinical forecasting tasks.

# Why It Matters
MIRA addresses critical challenges of irregular intervals, heterogeneous sampling, and missing values in medical time series, enabling robust, scalable forecasting without task-specific tuning. Its medical-domain pretraining fosters cross-institutional transferability, reducing annotation burdens and enhancing clinical decision-making in data-scarce or privacy-sensitive contexts.

# Method / Setup
MIRA employs CT-RoPE to model continuous irregular timestamps, a sparse Mixture-of-Experts layer to handle multi-frequency temporal patterns, and a Neural ODE-based extrapolation block for continuous-time forecasting at arbitrary timestamps. The model is pretrained on five diverse, large-scale medical datasets and evaluated zero-shot on numerous downstream clinical benchmarks against 13 state-of-the-art models.

# Key Claims
- MIRA outperforms existing zero-shot and fine-tuned baselines on both out-of-distribution and in-distribution medical time series forecasting tasks, reducing forecasting errors by approximately 8% and 6%, respectively.
- The CT-RoPE facilitates fine-grained modeling of irregular time intervals, preserving relative positional information in continuous time.
- Frequency-specific mixture-of-experts promote temporal specialization and improve modeling of diverse frequency regimes inherent in medical signals.
- The Continuous Dynamics Extrapolation Block enables prediction at arbitrary future timestamps, overcoming limitations of fixed-grid autoregressive models.
- Domain-specific pretraining on large medical corpora yields significant performance gains over general-domain pretrained models, demonstrating the importance of data relevance.

# Limitations
- Pretraining and evaluation use publicly available de-identified datasets which may not fully capture complexities of real-world clinical environments.
- Residual privacy risks inherent in clinical data are acknowledged but not addressed within this work.
- The model's performance and generalizability in real-world deployment scenarios remain to be validated.
- Computational costs and resource requirements for large-scale pretraining and inference, particularly with the Neural ODE component, are not extensively discussed.

# Connections
- [[Medical-Time-Series]]
- `evaluates` zero-shot forecasting across diverse downstream clinical datasets including ICU monitoring, epidemiological surveillance, ECG and EEG signals, and pediatric waveform datasets.
- `evaluates` performance under varying missing data rates, showing robustness up to 90% missingness.
- `evaluates` impact of model components via ablation studies for CT-RoPE, MoE block, and Neural ODE extrapolation.
- `evaluates` scaling behavior across model sizes from 73M to 455M parameters.
- `builds_on_unresolved` Neural Ordinary Differential Equations for continuous dynamics modeling.
- `builds_on_unresolved` Existing generalist time series foundation models like Time-MoE, Moirai, and Chronos that lack robust handling of medical time series irregularities.
- `builds_on_unresolved` Prior medical time series models that focus on classification but not continuous forecasting or irregular sampling.
- `builds_on_unresolved` The limited generalizability of prior medical time series foundation models confined to narrow domains.
- `compares_to_unresolved` Generalist time series foundation models including Time-MoE, Moirai, Moirai-MoE, TimesFM, Chronos, Moment, TimeGPT which require regular sampling or interpolation.
- `compares_to_unresolved` Task-specific irregular time series models such as ContiFormer, T-PatchGNN, Neural-CDE, and ODE-RNN requiring fine-tuning.
- `compares_to_unresolved` Encoder-only, encoder-decoder, and decoder-only architectures for time series modelling with varying scales and pretraining corpora.
- `compares_to_unresolved` Emerging medical time series foundation models focusing on classification or specific domains (e.g., EEG sleep staging).
<!-- GENERATED:END -->

## My Notes


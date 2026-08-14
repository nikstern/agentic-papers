---
paper_id: 133
title: "A Transformer-based Diffusion Probabilistic Model for Heart Rate and Blood Pressure Forecasting in Intensive Care Unit"
year: 2023
authors: "Chang et al."
url: "https://arxiv.org/abs/2301.06625"
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
  - "MQ-RNN"
  - "DeepAR"
  - "DeepFactor"
  - "EnCQR"
  - "CSDI"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Generative Boosting (LSTM-based) models for HR prediction"
  - "Bidirectional LSTM models with DIRMO strategy"
  - "TOP-Net Bi-LSTM for tachycardia onset prediction"
  - "Temporal Fusion Transformer for vital sign quantile forecasting"
  - "CSDI diffusion model for time series imputation and forecasting"
compares_to_unresolved:
  - "CSDI diffusion probabilistic model for probabilistic time series forecasting"
  - "MQ-RNN quantile recurrent forecasters"
  - "DeepAR autoregressive recurrent networks"
  - "DeepFactor global and local factor models"
  - "EnCQR ensemble conformalized quantile regression"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes TDSTF, a Transformer-based diffusion probabilistic model designed to forecast sparse time series of vital signs (heart rate, systolic and diastolic blood pressure) in ICU patients, demonstrating substantial improvements over previous models on the MIMIC-III dataset.

# Why It Matters
Accurate and efficient forecasting of vital signs in ICUs enables timely clinical interventions, potentially improving patient outcomes and alleviating caregiver burden in critical care settings.

# Method / Setup
TDSTF integrates Transformer and diffusion probabilistic models, representing sparse ICU data as triplets of feature, time, and value with masks, trained to predict distributions of future vital signs using a diffusion denoising process optimized via mean squared error on added noise.

# Key Claims
- TDSTF achieves state-of-the-art performance on standardized average continuous ranked probability score (SACRPS) and mean squared error (MSE) for vital sign forecasting, outperforming multiple baselines including CSDI by 18.9% SACRPS and 34.3% MSE.
- The model is computationally efficient, with inference speeds over 17 times faster than the best baseline model.
- The input triplet representation and the Transformer-based architecture effectively handle extremely sparse and irregular ICU time series data without requiring imputation.
- TDSTF is robust to missing target data and captures complex temporal dependencies across a broad set of ICU features.
- The proposed model's structure balances performance and computational cost, as confirmed by ablation studies and noise schedule optimization.

# Limitations
- The Transformer input size limitations restrict the model's scalability due to quadratic memory and time complexity.
- The demographic characteristics of the MIMIC-III dataset (older, predominantly male patients) may bias the model and limit generalizability.
- The study focuses on three vital signs, with no inclusion of other important clinical variables like core body temperature or oxygen saturation.
- The model was evaluated retrospectively; real-time or prospective validation in clinical environments is pending.

# Connections
- [[Medical-Time-Series]]
- `evaluates` MQ-RNN
- `evaluates` DeepAR
- `evaluates` DeepFactor
- `evaluates` EnCQR
- `evaluates` CSDI
- `builds_on_unresolved` Generative Boosting (LSTM-based) models for HR prediction
- `builds_on_unresolved` Bidirectional LSTM models with DIRMO strategy
- `builds_on_unresolved` TOP-Net Bi-LSTM for tachycardia onset prediction
- `builds_on_unresolved` Temporal Fusion Transformer for vital sign quantile forecasting
- `builds_on_unresolved` CSDI diffusion model for time series imputation and forecasting
- `compares_to_unresolved` CSDI diffusion probabilistic model for probabilistic time series forecasting
- `compares_to_unresolved` MQ-RNN quantile recurrent forecasters
- `compares_to_unresolved` DeepAR autoregressive recurrent networks
- `compares_to_unresolved` DeepFactor global and local factor models
- `compares_to_unresolved` EnCQR ensemble conformalized quantile regression
<!-- GENERATED:END -->

## My Notes


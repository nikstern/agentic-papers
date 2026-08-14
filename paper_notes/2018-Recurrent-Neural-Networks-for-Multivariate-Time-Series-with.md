---
paper_id: 143
title: "Recurrent Neural Networks for Multivariate Time Series with Missing Values"
year: 2018
authors: "Che et al."
url: "https://arxiv.org/abs/1606.01865"
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
  - "Non-RNN baselines: Logistic Regression (LR), Support Vector Machines (SVM), Random Forest (RF)"
  - "RNN baselines: GRU-mean, GRU-forward, GRU-simple, LSTM-mean"
  - "GRU variations: GRU-DI, GRU-DS, GRU-DM, GRU-IMP"
  - "Synthetic datasets with varied missingness-label correlations"
  - "Real-world clinical datasets: MIMIC-III, PhysioNet Challenge 2012"
  - "Multi-task classification involving mortality, length-of-stay, cardiac condition, surgery recovery, and ICD-9 code prediction"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Standard gated recurrent units (GRU) for time series classification"
  - "Existing imputation techniques: mean imputation, forward imputation"
  - "Prior RNN-based methods incorporating missingness as concatenated features (masking and time interval)"
  - "Health care time series datasets with informative missing data patterns"
compares_to_unresolved:
  - "GRU-mean, GRU-forward, and GRU-simple baseline models"
  - "Non-RNN models (LR, SVM, RF) with various imputation and masking strategies"
  - "Related RNN models in health care not explicitly modeling missingness (e.g., Lipton et al., Choi et al., Pham et al.)"
  - "Other GRU variations applying trainable decays on input or hidden states separately or masking decay"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper proposes GRU-D, a novel recurrent neural network model based on gated recurrent units (GRU) designed to handle informative missingness in multivariate time series data. GRU-D integrates masking and time interval information of missing patterns directly into its architecture using trainable decay mechanisms, enhancing its ability to exploit missing data patterns alongside temporal dependencies.

# Why It Matters
Handling missing values effectively is critical in real-world multivariate time series data, such as clinical records, where missingness can be informative and correlated with outcomes. GRU-D enables improved predictive performance by explicitly modeling these missingness patterns, which traditional imputation or naïve approaches fail to capture.

# Method / Setup
GRU-D modifies standard GRU by introducing trainable decay rates that systematically decay input values towards empirical means and decay hidden states based on elapsed time since last observations. It incorporates masking vectors and time intervals as inputs, and learns decay parameters jointly via backpropagation on classification tasks. Evaluations use real-world healthcare datasets (MIMIC-III, PhysioNet), synthetic datasets, and various baselines including non-RNN models and other RNN variants.

# Key Claims
- GRU-D effectively captures and exploits informative missingness patterns through trainable decay mechanisms.
- Incorporating masking and time interval information directly into the GRU architecture improves prediction accuracy over imputation and simple concatenation baselines.
- GRU-D achieves state-of-the-art performance on multiple clinical time series classification tasks involving mortality and diagnoses.
- GRU-D enables earlier and more accurate predictions from partially observed time series compared to existing methods.
- The model scales effectively with growing dataset size, outperforming traditional machine learning and other RNN approaches.

# Limitations
- The model is primarily evaluated on clinical and synthetic datasets; generalizability to other domains is not thoroughly tested.
- The complexity added by trainable decays may increase training time and require careful hyperparameter tuning.
- GRU-D assumes missingness mechanisms that can be captured by decays; it might not fully model more complex missing data processes.
- Evaluation focuses on classification tasks; its effectiveness on other time series problems (e.g., forecasting) remains unverified.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Non-RNN baselines: Logistic Regression (LR), Support Vector Machines (SVM), Random Forest (RF)
- `evaluates` RNN baselines: GRU-mean, GRU-forward, GRU-simple, LSTM-mean
- `evaluates` GRU variations: GRU-DI, GRU-DS, GRU-DM, GRU-IMP
- `evaluates` Synthetic datasets with varied missingness-label correlations
- `evaluates` Real-world clinical datasets: MIMIC-III, PhysioNet Challenge 2012
- `evaluates` Multi-task classification involving mortality, length-of-stay, cardiac condition, surgery recovery, and ICD-9 code prediction
- `builds_on_unresolved` Standard gated recurrent units (GRU) for time series classification
- `builds_on_unresolved` Existing imputation techniques: mean imputation, forward imputation
- `builds_on_unresolved` Prior RNN-based methods incorporating missingness as concatenated features (masking and time interval)
- `builds_on_unresolved` Health care time series datasets with informative missing data patterns
- `compares_to_unresolved` GRU-mean, GRU-forward, and GRU-simple baseline models
- `compares_to_unresolved` Non-RNN models (LR, SVM, RF) with various imputation and masking strategies
- `compares_to_unresolved` Related RNN models in health care not explicitly modeling missingness (e.g., Lipton et al., Choi et al., Pham et al.)
- `compares_to_unresolved` Other GRU variations applying trainable decays on input or hidden states separately or masking decay
<!-- GENERATED:END -->

## My Notes


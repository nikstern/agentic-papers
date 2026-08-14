---
paper_id: 142
title: "Multitask Learning and Benchmarking with Clinical Time Series Data"
year: 2019
authors: "Harutyunyan et al."
url: "https://arxiv.org/abs/1703.07771"
paper_type: "benchmark"
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
  - "In-hospital mortality prediction models"
  - "Physiologic decompensation prediction models"
  - "Length-of-stay forecasting models"
  - "Acute care phenotype classification models"
  - "Effect of deep supervision and multitask training on LSTM models"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "PhysioNet/CinC Challenge 2012 for mortality prediction benchmark"
  - "Previous mortality prediction scores like APACHE and SAPS"
  - "Prior phenotype classification and multilabel classification approaches"
  - "Earlier studies using LSTM and neural networks in clinical time series"
  - "The lack of unified multitask clinical prediction benchmarks"
compares_to_unresolved:
  - "Rajkomar et al.'s deep learning models on private EHR datasets"
  - "Prior early warning scores for decompensation such as MEWS and NEWS"
  - "Parallel MIMIC-III benchmarking work without decompensation prediction"
  - "Traditional severity scores (e.g., SAPS) and logistic regression baselines"
  - "Other neural architectures including bidirectional LSTMs and attention models"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
The paper introduces four clinical prediction benchmarks derived from the MIMIC-III database covering in-hospital mortality, physiologic decompensation, length of stay, and phenotype classification. It proposes strong linear and neural network baselines, including channel-wise LSTMs and multitask learning, evaluates their performances, and provides a standard framework and dataset for benchmarking clinical time series prediction tasks.

# Why It Matters
Standardized benchmarks are crucial for advancing machine learning in healthcare by enabling reproducible evaluation and comparison of models across diverse clinical prediction tasks, addressing prior challenges in measuring progress due to variability and lack of public datasets.

# Method / Setup
The authors curated and processed ICU stay data from MIMIC-III, defined four distinct clinical prediction tasks representing classification and regression problems, and developed linear regression and LSTM-based models, including channel-wise and multitask LSTM architectures with deep supervision. They performed hyperparameter tuning, trained models with optimization techniques, and evaluated using metrics like AUC-ROC, Cohen's kappa, and precision-recall curves with bootstrapped confidence intervals.

# Key Claims
- LSTM-based models significantly outperform linear models across all four tasks.
- Channel-wise LSTMs improve prediction performance by processing individual input variables separately before integration.
- Multitask learning enhances performance for in-hospital mortality and decompensation prediction but may not improve phenotyping due to its intrinsic multitask nature.
- Deep supervision improves model performance for decompensation and length-of-stay prediction tasks.
- The four proposed benchmarks facilitate research on clinically relevant, heterogeneous temporal prediction tasks in intensive care settings.

# Limitations
- Data is collected from a single EHR system (MIMIC-III), which may contain systematic biases affecting generalizability.
- Phenotype classification uses retrospective labels without timing, limiting temporal phenotype prediction.
- Multitask training poses optimization challenges such as varying convergence rates and overfitting among tasks.
- The length-of-stay prediction task is intrinsically difficult, reflected in lower performance metrics compared to other tasks.
- Linear models with complex feature engineering might close the performance gap but were not extensively explored.

# Connections
- [[Medical-Time-Series]]
- `evaluates` In-hospital mortality prediction models
- `evaluates` Physiologic decompensation prediction models
- `evaluates` Length-of-stay forecasting models
- `evaluates` Acute care phenotype classification models
- `evaluates` Effect of deep supervision and multitask training on LSTM models
- `builds_on_unresolved` PhysioNet/CinC Challenge 2012 for mortality prediction benchmark
- `builds_on_unresolved` Previous mortality prediction scores like APACHE and SAPS
- `builds_on_unresolved` Prior phenotype classification and multilabel classification approaches
- `builds_on_unresolved` Earlier studies using LSTM and neural networks in clinical time series
- `builds_on_unresolved` The lack of unified multitask clinical prediction benchmarks
- `compares_to_unresolved` Rajkomar et al.'s deep learning models on private EHR datasets
- `compares_to_unresolved` Prior early warning scores for decompensation such as MEWS and NEWS
- `compares_to_unresolved` Parallel MIMIC-III benchmarking work without decompensation prediction
- `compares_to_unresolved` Traditional severity scores (e.g., SAPS) and logistic regression baselines
- `compares_to_unresolved` Other neural architectures including bidirectional LSTMs and attention models
<!-- GENERATED:END -->

## My Notes


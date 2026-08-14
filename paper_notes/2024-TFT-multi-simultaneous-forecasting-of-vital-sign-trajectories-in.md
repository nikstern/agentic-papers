---
paper_id: 127
title: "TFT-multi: simultaneous forecasting of vital sign trajectories in the ICU"
year: 2024
authors: "He and Chiang"
url: "https://arxiv.org/abs/2409.15586"
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
  - "Prophet univariate forecasting model"
  - "Original Temporal Fusion Transformer (TFT)"
  - "Vector Autoregression (VAR) multivariate model"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Temporal Fusion Transformer (TFT) for univariate multi-horizon forecasting"
  - "Prophet time series forecasting model"
  - "Vector Autoregressive (VAR) models for multivariate time series forecasting"
compares_to_unresolved:
  - "Univariate forecasting methods requiring separate models per variable"
  - "VAR model limitations handling variables failing Granger causality tests"
  - "Baseline AI and autoregressive methods like ARIMA in vital sign prediction"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
TFT-multi extends the Temporal Fusion Transformer to simultaneously forecast multiple ICU vital signs by leveraging their correlations, outperforming univariate and multivariate baselines on public and institutional datasets. The approach incorporates a masking loss to handle missing data and enables treatment effect estimation via hypothetical medication scenarios.

# Why It Matters
Simultaneous multi-vital forecasting better reflects clinical settings by improving accuracy, reducing computational burden, and supporting decision-making through treatment effect prediction, thereby enhancing ICU patient monitoring and precision care.

# Method / Setup
TFT-multi modifies TFT's input-output and loss functions to predict 5 vital signs at 15-minute intervals jointly, using quantile loss with masking to exclude imputed values. Models were trained on MIMIC-IV data with static and time series covariates using Adam optimizer and validated both internally and externally.

# Key Claims
- Joint prediction of multiple correlated vital signs outperforms univariate models like Prophet, original TFT, and multivariate VAR in predictive accuracy.
- The masking loss improves performance on sparsely sampled variables by avoiding overfitting to imputed data.
- TFT-multi requires less computational resources than training multiple univariate models separately.
- The model supports treatment effect estimation and hypothetical scenario forecasting for pressor administration.
- Extending the model to multiple variables captures interdependencies that improve prediction of vitals with high missingness.

# Limitations
- Calibration is limited for features with high missingness like SpO2 and temperature, affecting their prediction bounds and tracking of rapid fluctuations.
- Interpretability is limited as feature importance is aggregated globally and lacks subject-level explanations.
- Medication inputs for treatment effect modeling were simplified to binary administration without dose or timing subtleties.
- External validation data lacked detailed medication timing, limiting treatment effect assessments.
- The model currently focuses on ICU data and does not yet handle outpatient cohorts with greater missingness.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Prophet univariate forecasting model
- `evaluates` Original Temporal Fusion Transformer (TFT)
- `evaluates` Vector Autoregression (VAR) multivariate model
- `builds_on_unresolved` Temporal Fusion Transformer (TFT) for univariate multi-horizon forecasting
- `builds_on_unresolved` Prophet time series forecasting model
- `builds_on_unresolved` Vector Autoregressive (VAR) models for multivariate time series forecasting
- `compares_to_unresolved` Univariate forecasting methods requiring separate models per variable
- `compares_to_unresolved` VAR model limitations handling variables failing Granger causality tests
- `compares_to_unresolved` Baseline AI and autoregressive methods like ARIMA in vital sign prediction
<!-- GENERATED:END -->

## My Notes


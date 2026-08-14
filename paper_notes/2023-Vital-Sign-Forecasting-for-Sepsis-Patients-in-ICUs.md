---
paper_id: 126
title: "Vital Sign Forecasting for Sepsis Patients in ICUs"
year: 2023
authors: "Bhatti et al."
url: "https://arxiv.org/abs/2311.04770"
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
  - "N-BEATS model"
  - "N-HiTS model"
  - "Temporal Fusion Transformer (TFT) model"
  - "Persistence model as baseline"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "N-BEATS architecture"
  - "N-HiTS architecture"
  - "Temporal Fusion Transformer (TFT)"
  - "DILATE loss function for time series forecasting"
compares_to_unresolved:
  - "Traditional sepsis scoring systems like APACHE, SAPS, SOFA, qSOFA which lack early detection capability"
  - "Persistence (naive forecasting) baseline model"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
The paper introduces a deep learning system that forecasts vital signs (mean blood pressure, heart rate) up to 3 hours ahead in ICU patients with sepsis, using 6 hours of past data and three state-of-the-art models (N-BEATS, N-HiTS, TFT). The DILATE loss function is employed to capture shape and temporal dynamics critical for clinical decisions, evaluated on the eICU-CRD dataset.

# Why It Matters
Early and accurate forecasting of vital signs in septic ICU patients can enable timely interventions, potentially reducing mortality and improving patient outcomes by anticipating physiological deterioration such as septic shock. The approach aims to overcome limitations of traditional scoring systems which lack early detection capabilities.

# Method / Setup
The study uses vital sign data (MBP, HR, RR) from the publicly available eICU-CRD, sampled every 5 minutes, applying data preprocessing and min-max scaling with clinically sensible ranges. Three deep learning models (N-BEATS, N-HiTS, TFT) are trained and compared using 6-hour inputs to predict 3-hour futures, evaluated with MSE and DTW metrics, employing the DILATE loss function.

# Key Claims
- A deep learning multi-step forecasting system can predict vital signs indicative of septic shock progression in ICU patients.
- N-HiTS better retains short-term fluctuations, while TFT captures overall trends effectively.
- Using the DILATE loss function improves capturing the shape and temporal dynamics of vital signs critical for clinical decisions.
- Deep learning models outperform naive persistence models over longer forecast horizons, enhancing prediction accuracy.
- Forecasting vital signs from short windows of past data is feasible and beneficial in critical care settings.

# Limitations
- Models currently utilize only vital sign data, without integration of broader clinical parameters or multimodal data.
- Performance varies with inclusion of covariates; some models perform better without them, indicating potential model-specific tuning needs.
- Initial forecasting horizons show higher error than persistence, suggesting limitations in very short-term accuracy.
- The study focuses on a specific dataset (eICU-CRD) which may limit generalizability to other ICU populations or settings.
- Further validation and model refinement are needed before clinical deployment.

# Connections
- [[Medical-Time-Series]]
- `evaluates` N-BEATS model
- `evaluates` N-HiTS model
- `evaluates` Temporal Fusion Transformer (TFT) model
- `evaluates` Persistence model as baseline
- `builds_on_unresolved` N-BEATS architecture
- `builds_on_unresolved` N-HiTS architecture
- `builds_on_unresolved` Temporal Fusion Transformer (TFT)
- `builds_on_unresolved` DILATE loss function for time series forecasting
- `compares_to_unresolved` Traditional sepsis scoring systems like APACHE, SAPS, SOFA, qSOFA which lack early detection capability
- `compares_to_unresolved` Persistence (naive forecasting) baseline model
<!-- GENERATED:END -->

## My Notes


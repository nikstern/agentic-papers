---
paper_id: 147
title: "N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting"
year: 2023
authors: "Challu et al."
url: "https://arxiv.org/abs/2201.12886"
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
  - "Electricity Transformer Temperature dataset (ETTm2)"
  - "Exchange rate dataset"
  - "Electricity consumption dataset (ECL)"
  - "San Francisco Bay Area Highway Traffic dataset (TrafficL)"
  - "Weather dataset"
  - "Influenza-like illness dataset (ILI)"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "N-BEATS neural basis expansion analysis (Oreshkin et al. 2020)"
  - "Transformer-based multi-step forecasting methods such as Autoformer, Informer, LogTrans, and Reformer"
  - "Multi-step direct forecasting and joint forecasting strategies"
  - "Mixed data sampling regression (MIDAS) techniques for long-horizon forecasting"
  - "Interpolation techniques in time series forecasting for unevenly sampled data"
compares_to_unresolved:
  - "State-of-the-art Transformer-based models for long-horizon forecasting (Autoformer, Informer, LogTrans, Reformer)"
  - "N-BEATS architecture variants (interpretable and generic)"
  - "Dilated Recurrent Neural Networks (DilRNN)"
  - "Auto-ARIMA and Prophet models for univariate forecasting"
  - "Recent concurrent Transformer enhancements such as ETSformer and Preformer"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
N-HiTS is a novel neural forecasting model that enhances long-horizon time series prediction by integrating multi-rate input sampling and hierarchical interpolation, achieving state-of-the-art accuracy with significantly reduced computational cost compared to Transformer-based methods. The approach decomposes forecasts into components at different frequencies and scales, enabling interpretable, efficient, and accurate predictions.

# Why It Matters
Long-horizon time series forecasting is crucial for applications in healthcare, energy, and infrastructure but remains challenging due to computational complexity and prediction volatility. N-HiTS addresses these challenges, delivering substantial accuracy gains with much lower computational resources, thus enabling practical deployment in real-world scenarios.

# Method / Setup
N-HiTS extends the N-BEATS architecture by applying multi-rate max-pooling sampling to input time series at each block, and employs hierarchical interpolation to generate forecasts at varying temporal granularities across blocks. The model sequentially sums multi-scale forecasts specialized in different frequency bands, trained via MLP blocks with jointly optimized hyperparameters on large-scale benchmark datasets.

# Key Claims
- N-HiTS achieves an average 16% MSE and 14% MAE improvement over existing state-of-the-art Transformer-based multivariate forecasting models across six large datasets.
- The model reduces computational training time by up to 45 times compared to Transformer models and has significantly lower memory usage.
- Hierarchical interpolation enables efficient approximation of arbitrarily long forecasting horizons with smoothness guarantees.
- Multi-rate input sampling and hierarchical interpolation complement each other to improve both forecasting accuracy and computational efficiency.
- N-HiTS provides interpretable decomposition of forecasts into trend/seasonality components at multiple scales.
- The model maintains constant parameter and computational complexity regardless of dataset size due to its univariate setup with shared global parameters.
- Hierarchical interpolation technique benefits other architectures such as DilRNN when integrated.
- Top-down hierarchy (low-frequency components first) improves forecasting performance compared to bottom-up approaches.

# Limitations
- N-HiTS operates in a univariate setting, potentially limiting exploitation of multivariate correlations.
- The model uses fixed hyperparameter search spaces and architectures; optimal configurations may vary across domains.
- Comparisons to some recent concurrent methods are limited due to differences in experimental setups and lack of multiple runs for variance estimation.
- Interpretability benefits may be less pronounced in architectures other than N-HiTS with hierarchical interpolation.
- The efficacy of combining N-HiTS techniques with Transformer architectures remains an open question for future work.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Electricity Transformer Temperature dataset (ETTm2)
- `evaluates` Exchange rate dataset
- `evaluates` Electricity consumption dataset (ECL)
- `evaluates` San Francisco Bay Area Highway Traffic dataset (TrafficL)
- `evaluates` Weather dataset
- `evaluates` Influenza-like illness dataset (ILI)
- `builds_on_unresolved` N-BEATS neural basis expansion analysis (Oreshkin et al. 2020)
- `builds_on_unresolved` Transformer-based multi-step forecasting methods such as Autoformer, Informer, LogTrans, and Reformer
- `builds_on_unresolved` Multi-step direct forecasting and joint forecasting strategies
- `builds_on_unresolved` Mixed data sampling regression (MIDAS) techniques for long-horizon forecasting
- `builds_on_unresolved` Interpolation techniques in time series forecasting for unevenly sampled data
- `compares_to_unresolved` State-of-the-art Transformer-based models for long-horizon forecasting (Autoformer, Informer, LogTrans, Reformer)
- `compares_to_unresolved` N-BEATS architecture variants (interpretable and generic)
- `compares_to_unresolved` Dilated Recurrent Neural Networks (DilRNN)
- `compares_to_unresolved` Auto-ARIMA and Prophet models for univariate forecasting
- `compares_to_unresolved` Recent concurrent Transformer enhancements such as ETSformer and Preformer
<!-- GENERATED:END -->

## My Notes


---
paper_id: 148
title: "Shape and Time Distortion Loss for Training Deep Time Series Forecasting Models"
year: 2019
authors: "Le Guen and Thome"
url: "https://arxiv.org/abs/1909.09020"
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
  - "Mean Squared Error (MSE) loss"
  - "Smooth Dynamic Time Warping (DTW) loss"
  - "Ramp score"
  - "Temporal Distortion Index (TDI)"
  - "Hausdorff distance between detected change points"
  - "Weighted DTW and Band constrained DTW variants"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Dynamic Time Warping (DTW)"
  - "Smooth DTW differentiable loss"
  - "Temporal Distortion Index (TDI)"
compares_to_unresolved:
  - "Mean Squared Error (MSE) loss function"
  - "Weighted DTW and Band Constraint DTW"
  - "LSTNet"
  - "Tensor-Train RNN (TT-RNN)"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This paper introduces DILATE, a novel differentiable loss function combining shape and temporal distortion terms for training deep neural networks to forecast non-stationary multistep time series with sudden changes. DILATE improves prediction of sharp changes by explicitly disentangling shape and timing errors and enabling efficient back-propagation via a custom implementation.

# Why It Matters
Accurately forecasting non-stationary time series with abrupt regime changes is critical in domains like medical signals and energy forecasting; existing losses like MSE fail to capture timing errors. DILATE better reflects real forecasting quality, improving model performance on shape and temporal metrics, which matters for practical decision-making.

# Method / Setup
DILATE loss combines a differentiable soft Dynamic Time Warping (DTW) shape term and a smooth temporal distortion term based on the gradient of smoothed DTW. It is incorporated into training deep neural networks, such as fully connected and Seq2Seq recurrent models, with custom forward and backward passes implemented for scalability and efficiency. Hyperparameters balance shape versus temporal penalty.

# Key Claims
- DILATE explicitly disentangles shape and temporal errors to improve multistep forecasting on non-stationary data with sudden changes.
- DILATE loss outperforms standard MSE and smooth DTW losses across multiple datasets (synthetic, ECG5000, traffic) on shape (DTW, ramp score) and temporal (TDI, Hausdorff) evaluation metrics.
- DILATE is model-agnostic, effective for both fully connected and recurrent architectures, and improves over state-of-the-art forecasting models trained with MSE.
- Custom backward implementation of DILATE significantly speeds up computation compared to standard autodiff, enabling scalability to longer prediction horizons.
- DILATE's separate optimization of shape and temporal terms yields better disentanglement than intertwined temporal constraints in DTW variants.

# Limitations
- DILATE, while outperforming on shape and timing metrics, is sometimes outperformed on MSE, indicating a trade-off in optimization objectives.
- Experiments are limited to deterministic forecasting; extension to probabilistic forecasting is suggested as future work.
- The approach requires tuning the balance hyperparameter alpha for combining shape and temporal losses, which may require dataset-specific validation.
- The temporal loss relies on a smooth approximation of DTW gradients, which may have limitations in distinguishing complex temporal distortions.
- Evaluation focuses on univariate and mostly small to medium scale datasets; applicability to high-dimensional multivariate series requires further exploration.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Mean Squared Error (MSE) loss
- `evaluates` Smooth Dynamic Time Warping (DTW) loss
- `evaluates` Ramp score
- `evaluates` Temporal Distortion Index (TDI)
- `evaluates` Hausdorff distance between detected change points
- `evaluates` Weighted DTW and Band constrained DTW variants
- `builds_on_unresolved` Dynamic Time Warping (DTW)
- `builds_on_unresolved` Smooth DTW differentiable loss
- `builds_on_unresolved` Temporal Distortion Index (TDI)
- `compares_to_unresolved` Mean Squared Error (MSE) loss function
- `compares_to_unresolved` Weighted DTW and Band Constraint DTW
- `compares_to_unresolved` LSTNet
- `compares_to_unresolved` Tensor-Train RNN (TT-RNN)
<!-- GENERATED:END -->

## My Notes


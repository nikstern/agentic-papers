---
paper_id: 136
title: "Towards Real-Time Respiratory Motion Prediction based on Long Short-Term Memory Neural Networks"
year: 2019
authors: "Lin et al."
url: "https://arxiv.org/abs/1901.08638"
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
  - "Long Short-Term Memory neural networks for respiratory motion prediction"
  - "Impact of hyperparameter optimization on LSTM model accuracy"
builds_on: []
compares_to: []
builds_on_unresolved:
  - "Conventional artificial neural network models for respiratory motion prediction"
compares_to_unresolved:
  - "Artificial neural network baseline models for respiratory signal prediction"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This study develops and optimizes a Long Short-Term Memory (LSTM) neural network model for real-time respiratory motion prediction using 1703 clinical datasets to improve treatment accuracy in radiation therapy for thoracic and abdominal tumors.

# Why It Matters
Accurate respiratory motion prediction is critical to precisely target tumors during radiation therapy, minimizing healthy tissue damage and improving treatment outcomes.

# Method / Setup
The authors collected 1703 Real-Time Position Management datasets from three institutions, split into training, internal, and external validity groups, and performed an exhaustive grid search to optimize LSTM hyperparameters such as layers, hidden units, optimizer, learning rate, epochs, and lag length.

# Key Claims
- LSTM models outperform conventional artificial neural networks in predicting respiratory signals.
- Tuning LSTM hyperparameters reduces prediction error significantly, with a 20% MAE improvement over default settings.
- The optimized LSTM achieved low prediction errors (e.g., MAE of 0.037 on internal validity data) with a 500ms prediction window.
- The model generalizes well to external datasets, indicating robust predictive power across different clinical data.

# Limitations
- Prediction performance degrades on external datasets compared to internal validation, indicating some generalization limits.
- The study focuses solely on Real-Time Position Management data; other respiratory signal modalities are not considered.
- Predictions are evaluated only up to a 500ms window, limiting insight into longer-term respiratory motion forecasting.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Long Short-Term Memory neural networks for respiratory motion prediction
- `evaluates` Impact of hyperparameter optimization on LSTM model accuracy
- `builds_on_unresolved` Conventional artificial neural network models for respiratory motion prediction
- `compares_to_unresolved` Artificial neural network baseline models for respiratory signal prediction
<!-- GENERATED:END -->

## My Notes


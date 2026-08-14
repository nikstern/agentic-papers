---
paper_id: 141
title: "Pilot Deployment of a Machine-Learning Enhanced Prediction of Need for Hemorrhage Resuscitation After Trauma: The ShockMatrix Pilot Study"
year: 2024
authors: "Gauss et al."
url: "https://pubmed.ncbi.nlm.nih.gov/39468585/"
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
  - "need-for-hemorrhage-resuscitation prediction"
  - "recall-weighted trauma triage evaluation"
  - "real-time clinical workflow feasibility"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "RED FLAG score"
  - "Assessment of Blood Consumption score"
  - "trauma leader clinical judgment"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
ShockMatrix develops an XGBoost decision-support model from prehospital variables to predict need for hemorrhage resuscitation and then pilots real-time predictor collection and clinician-facing predictions in four trauma centers.

# Why It Matters
It connects retrospective prediction to workflow feasibility and uses a recall-weighted metric appropriate to high-cost missed interventions, making it a strong translational comparator for the JRESP proposal.

# Method / Setup
Model development uses 28,614 registry patients, including 3,249 positive hemorrhage-resuscitation cases, and compares several models and imputation methods with RED FLAG and ABC scores. A nine-variable XGBoost model is evaluated by F4 score; a subsequent three-month pilot collects predictions through a smartphone app and compares them with trauma-leader judgment.

# Key Claims
- The best nine-variable XGBoost model achieved an F4 score of 0.76 with a 95% interval of 0.73 to 0.78.
- Threshold adjustment could reach approximately 0.90 recall while retaining precision above 0.25 in validation analyses.
- Real-time collection was feasible without reported workflow disruption, and model likelihood ratios were comparable to clinicians in the small pilot.

# Limitations
- The deployment pilot included only 139 patients and 22 outcome-positive cases.
- The model uses a small structured feature set rather than continuous time-series forecasting.
- Feasibility and clinician comparison do not establish improved patient outcomes.

# Connections
- [[Medical-Time-Series]]
- `evaluates` need-for-hemorrhage-resuscitation prediction
- `evaluates` recall-weighted trauma triage evaluation
- `evaluates` real-time clinical workflow feasibility
- `compares_to_unresolved` RED FLAG score
- `compares_to_unresolved` Assessment of Blood Consumption score
- `compares_to_unresolved` trauma leader clinical judgment
<!-- GENERATED:END -->

## My Notes


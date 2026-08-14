---
paper_id: 144
title: "Development and Validation of a Deep Learning Model for Prediction of Adult Physiological Deterioration"
year: 2024
authors: "Delahanty et al."
url: "https://pubmed.ncbi.nlm.nih.gov/39258951/"
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
  - "adult physiological deterioration prediction"
  - "temporal validation of clinical early warning"
  - "sensitivity at comparable false-alarm rate"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved:
  - "Epic Deterioration Index"
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
DETERIO is a deep-learning system for predicting a consensus-defined composite of adult physiological deterioration in emergency-department and inpatient populations, formulated as a state value-estimation problem.

# Why It Matters
Its temporal validation and fixed-false-alarm comparison illustrate the evaluation standard needed to claim that Toto improves actionable deterioration prediction rather than only average discrimination.

# Method / Setup
The derivation data contain 330,729 patients from the inpatient and emergency departments of two hospitals in one health system, with a separate temporal validation cohort of 65,898 patients. DETERIO predicts Adult Inpatient Decompensation Event criteria up to 12 hours before the event and is compared with the Epic Deterioration Index.

# Key Claims
- Temporal-validation AUROC was 0.775 for inpatients and 0.856 for emergency-department patients.
- For inpatient temporal validation, DETERIO exceeded the Epic Deterioration Index and achieved higher sensitivity at a comparable false-alarm rate.
- A value-estimation formulation can provide risk trajectories, confidence, and explanations for deterioration-oriented triage.

# Limitations
- The evaluation remains retrospective and is confined to one health system despite including two hospitals.
- The composite deterioration endpoint groups heterogeneous clinical events.
- Prospective workflow impact, external transportability, and patient benefit were not established.

# Connections
- [[Medical-Time-Series]]
- `evaluates` adult physiological deterioration prediction
- `evaluates` temporal validation of clinical early warning
- `evaluates` sensitivity at comparable false-alarm rate
- `compares_to_unresolved` Epic Deterioration Index
<!-- GENERATED:END -->

## My Notes


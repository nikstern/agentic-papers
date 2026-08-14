---
paper_id: 137
title: "A Machine Learning Trauma Triage Model for Critical Care Transport"
year: 2025
authors: "Galvagno et al."
url: "https://pubmed.ncbi.nlm.nih.gov/40489113/"
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
  - "life-saving intervention prediction from continuous prehospital physiology"
  - "lead-time sensitivity of trauma intervention alerts"
  - "intervention-specific trauma triage models"
builds_on: []
compares_to: []
builds_on_unresolved: []
compares_to_unresolved: []
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This retrospective cohort study develops an ensemble machine-learning model that predicts delivery of life-saving interventions from continuous physiological waveform features and vital-sign patterns recorded during prehospital critical-care transport of trauma patients.

# Why It Matters
It is the closest published analogue to the proposed JRESP task: forecasting actionable trauma interventions from already-captured continuous physiology with an explicit prediction lead time.

# Method / Setup
The study includes 2,809 trauma patients and 15,088 two-minute epochs from a regional critical-care air transport system. Models use physiological features from preceding epochs to predict an LSI in a subsequent epoch, with analyses extending prediction up to 15 minutes before intervention and separating LSI subcategories.

# Key Claims
- The overall LSI model achieved AUROC 0.810 with 0.960 specificity but only 0.268 sensitivity at the reported operating point.
- Performance was similar or better for several intervention subcategories and remained useful when predicting first intervention events and at longer lead times.
- Continuous physiological features can support prehospital trauma triage, but performance depends strongly on the selected alert threshold.

# Limitations
- The study is retrospective and comes from one critical-care transport system, so deployment and cross-site generalization remain untested.
- Only 6% of epochs contained an LSI, making AUROC insufficient without precision-recall and operating-point analysis.
- The reported high-specificity operating point has low sensitivity, which would miss many intervention events.
- Intervention delivery reflects both patient physiology and clinician behavior and is not a pure latent-state label.

# Connections
- [[Medical-Time-Series]]
- `evaluates` life-saving intervention prediction from continuous prehospital physiology
- `evaluates` lead-time sensitivity of trauma intervention alerts
- `evaluates` intervention-specific trauma triage models
<!-- GENERATED:END -->

## My Notes


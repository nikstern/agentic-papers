---
paper_id: 132
title: "Benchmarking Early Deterioration Prediction Across Hospital-Rich and MCI-Like Emergency Triage Under Constrained Sensing"
year: 2026
authors: "Solaiman et al."
url: "https://arxiv.org/abs/2602.20168"
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
  - "Early deterioration prediction under hospital-rich conditions."
  - "Early deterioration prediction under MCI-like vitals-only conditions."
  - "Impact of removing individual vital signs on model performance."
  - "Prediction of in-hospital mortality and ICU transfer within 24 hours."
  - "Model interpretability using SHAP values across feature regimes."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "MIMIC-IV-ED datasets for emergency department patient data."
  - "Existing emergency triage prediction models relying on hospital-rich data."
  - "Leakage-aware benchmarking to prevent information contamination in clinical prediction."
  - "Machine learning methods such as Logistic Regression, Random Forest, and XGBoost for clinical tasks."
  - "SHAP interpretability framework for tabular clinical data."
compares_to_unresolved:
  - "Rule-based early warning scores such as NEWS2 and mass-casualty triage protocols like START and SALT."
  - "Prior machine learning triage models that use post-triage or longitudinal data not available at initial assessment."
  - "Sequence-based and recurrent models requiring longitudinal inputs, which were excluded here."
  - "Other emergency risk prediction benchmarks that lack strict leakage control or partial observability constraints."
  - "Deep learning models incorporating free-text triage notes not systematically assessed under constrained sensing."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
This study benchmarks early deterioration prediction models using a patient-level deduplicated cohort from MIMIC-IV-ED, contrasting hospital-rich triage with MCI-like vitals-only settings under realistic one-hour initial assessment constraints. Multiple interpretable models are evaluated for mortality and ICU transfer outcomes, revealing modest performance degradation when limited to vitals, with respiratory and oxygenation metrics as key predictive signals.

# Why It Matters
Accurate early triage prediction under constrained sensing can improve emergency care decision-making, especially in resource-limited or mass-casualty incident settings where extensive diagnostics are unavailable. This benchmark supports development of deployable, interpretable decision-support systems with clinically relevant evaluation and leakage-aware protocols.

# Method / Setup
Patient encounters from MIMIC-IV-ED are curated to include only first ED visits with features restricted to the first hour of arrival, split into hospital-rich (vitals, labs, observations, notes) and MCI-like (vitals only) regimes. Models including Logistic Regression, Random Forest, XGBoost, LightGBM, and TabNet are trained and evaluated under strict patient-level stratified splits, with ablation and SHAP analyses for interpretability.

# Key Claims
- Models trained on vitals-only data retain substantial predictive power despite limited sensing.
- Respiratory and oxygenation measures are the most influential predictors of early deterioration.
- Non-linear ensemble methods (e.g., XGBoost) outperform linear and neural tabular models in this setting.
- Model performance degrades gracefully under systematic removal of vital signs, indicating robustness.
- Interpretability analyses confirm clinical relevance of key physiological signals across feature regimes.

# Limitations
- Study is limited to snapshot-based prediction within the first hour; longitudinal modeling is unexplored.
- Results are based on a 10,000 patient subset; generalizability to full MIMIC-IV-ED or external cohorts remains to be validated.
- Symptom text features offer marginal benefit and were not systematically studied across all models.
- Constrained sensing simulated via vitals-only does not capture all complexities of real-world mass-casualty sensor limitations.
- Alternative dynamic or sequential architectures were not evaluated, potentially missing temporal information advantages.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Early deterioration prediction under hospital-rich conditions.
- `evaluates` Early deterioration prediction under MCI-like vitals-only conditions.
- `evaluates` Impact of removing individual vital signs on model performance.
- `evaluates` Prediction of in-hospital mortality and ICU transfer within 24 hours.
- `evaluates` Model interpretability using SHAP values across feature regimes.
- `builds_on_unresolved` MIMIC-IV-ED datasets for emergency department patient data.
- `builds_on_unresolved` Existing emergency triage prediction models relying on hospital-rich data.
- `builds_on_unresolved` Leakage-aware benchmarking to prevent information contamination in clinical prediction.
- `builds_on_unresolved` Machine learning methods such as Logistic Regression, Random Forest, and XGBoost for clinical tasks.
- `builds_on_unresolved` SHAP interpretability framework for tabular clinical data.
- `compares_to_unresolved` Rule-based early warning scores such as NEWS2 and mass-casualty triage protocols like START and SALT.
- `compares_to_unresolved` Prior machine learning triage models that use post-triage or longitudinal data not available at initial assessment.
- `compares_to_unresolved` Sequence-based and recurrent models requiring longitudinal inputs, which were excluded here.
- `compares_to_unresolved` Other emergency risk prediction benchmarks that lack strict leakage control or partial observability constraints.
- `compares_to_unresolved` Deep learning models incorporating free-text triage notes not systematically assessed under constrained sensing.
<!-- GENERATED:END -->

## My Notes


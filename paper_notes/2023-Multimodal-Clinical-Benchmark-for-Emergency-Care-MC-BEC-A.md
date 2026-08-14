---
paper_id: 131
title: "Multimodal Clinical Benchmark for Emergency Care (MC-BEC): A Comprehensive Benchmark for Evaluating Foundation Models in Emergency Medicine"
year: 2023
authors: "Chen et al."
url: "https://arxiv.org/abs/2311.04937"
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
  - "Patient decompensation prediction at 60, 90, and 120-minute windows using multimodal data."
  - "Disposition prediction (discharge vs. admission) based on entire ED visit data."
  - "ED revisit prediction at 3, 7, and 14 days post-discharge using full visit data."
  - "Model performance with incremental modality inclusion to assess monotonicity."
  - "Robustness to missing modalities through ablation tests."
  - "Fairness of prediction across patient demographics assessing true positive rate disparities."
builds_on: []
compares_to: []
builds_on_unresolved:
  - "MIMIC-IV-ED benchmark focusing on tabular data without waveforms or free text."
  - "EHRShot dataset limited to coded data and not publicly available."
  - "HiRID ICU benchmark providing high-resolution physiological data but lacking free text or waveforms."
  - "Foundational clinical language models like ClinicalBERT and code embedding approaches such as CodeEmb."
compares_to_unresolved:
  - "Single-task vs. multitask models showing trade-offs in performance for ED prediction tasks."
  - "LightGBM baseline models compared to Random Forest and XGBoost, with LightGBM performing best."
  - "Modality fusion methods highlighting challenges in performance monotonicity with increasing modalities."
  - "Existing critical care benchmarks limited in multimodal coverage and task breadth."
relations: []
source: "alphaxiv-mcp"
---
<!-- GENERATED:START -->
# Summary
MC-BEC is a benchmark using a rich multimodal dataset of over 100K Emergency Department visits to evaluate foundation models on clinically relevant tasks including predicting patient decompensation, disposition, and ED revisit. The benchmark includes diverse modalities such as vital signs, waveforms, clinical codes with textual descriptions, and free-text imaging reports, alongside a standardized evaluation framework.

# Why It Matters
Emergency Medicine requires rapid, accurate decisions integrating heterogeneous data; MC-BEC addresses gaps in existing benchmarks by supporting multimodal and multitask evaluation, fostering development of generalist clinical AI models that better reflect real-world emergency care complexity.

# Method / Setup
The dataset covers 102,731 ED visits with no patient overlap across splits, including structured, time series, waveform, and free-text data. Tasks predict near-term decompensation, disposition, and revisit at multiple time horizons. Models use modality-specific featurization and fusion; baselines employed multitask LightGBM with pretrained embeddings and a prompting-inspired schema for task representation. Evaluation metrics include AUPRC, modality monotonicity, robustness to missing modalities, and fairness across demographic groups.

# Key Claims
- MC-BEC enables evaluation of foundation models on multimodal, multitask clinical prediction capturing dynamic ED patient states.
- Model performance generally improves with addition of modalities, especially continuous monitoring and waveforms for decompensation and disposition tasks.
- Multitask models perform comparably but slightly worse than single-task models, suggesting room for improvement in multitask architectures.
- Model robustness to missing modalities varies by task; some modalities are critical for prediction performance.
- Fairness evaluation reveals demographic-related disparities in true positive rates, notably by race, age, and gender, highlighting bias risks in deployed models.

# Limitations
- MC-BEC does not evaluate foundation model capabilities on novel clinical tasks such as summarization or therapeutic planning.
- Socioeconomic status is not directly captured, limiting fairness assessment related to these factors.
- Baseline models rely on engineered features and LightGBM; more advanced end-to-end deep learning methods may improve performance but are not explored here.

# Connections
- [[Medical-Time-Series]]
- `evaluates` Patient decompensation prediction at 60, 90, and 120-minute windows using multimodal data.
- `evaluates` Disposition prediction (discharge vs. admission) based on entire ED visit data.
- `evaluates` ED revisit prediction at 3, 7, and 14 days post-discharge using full visit data.
- `evaluates` Model performance with incremental modality inclusion to assess monotonicity.
- `evaluates` Robustness to missing modalities through ablation tests.
- `evaluates` Fairness of prediction across patient demographics assessing true positive rate disparities.
- `builds_on_unresolved` MIMIC-IV-ED benchmark focusing on tabular data without waveforms or free text.
- `builds_on_unresolved` EHRShot dataset limited to coded data and not publicly available.
- `builds_on_unresolved` HiRID ICU benchmark providing high-resolution physiological data but lacking free text or waveforms.
- `builds_on_unresolved` Foundational clinical language models like ClinicalBERT and code embedding approaches such as CodeEmb.
- `compares_to_unresolved` Single-task vs. multitask models showing trade-offs in performance for ED prediction tasks.
- `compares_to_unresolved` LightGBM baseline models compared to Random Forest and XGBoost, with LightGBM performing best.
- `compares_to_unresolved` Modality fusion methods highlighting challenges in performance monotonicity with increasing modalities.
- `compares_to_unresolved` Existing critical care benchmarks limited in multimodal coverage and task breadth.
<!-- GENERATED:END -->

## My Notes


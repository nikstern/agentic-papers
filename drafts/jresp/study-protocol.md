# JRESP Public-Data Study Protocol

Status: draft; freeze before final cohort construction and model selection.

## Primary question

Does adding a Toto forecast or Toto-derived representation improve prediction of a future deterioration or intervention endpoint compared with a direct classifier that receives the same observed vital-sign history?

## Hypotheses

- **H1 — Forecasting:** Toto improves probabilistic or point forecasting of future vital signs over persistence, autoregressive, N-HiTS, and TFT baselines.
- **H2 — Incremental clinical utility:** a classifier using observed history plus Toto outputs improves outcome prediction over the same classifier using observed history alone.
- **H3 — Representation utility:** Toto embeddings improve outcome prediction under linear probing or controlled fine-tuning.
- **H4 — Transportability:** any improvement persists under temporal, hospital, or dataset shift without unacceptable calibration or alert burden.

H2 is the primary scientific hypothesis. H1 without H2 is evidence of forecasting transfer, not evidence of triage utility.

## Unit of prediction

Create repeated prediction examples within an encounter:

- an observation window ending at index time `t`;
- an exclusion gap after `t` to prevent near-event leakage;
- a forecast window for future vital signs;
- an outcome window for a future intervention or deterioration event.

Exact durations remain to be selected in backlog task 104. Candidate horizons should reflect both data density and realistic intervention lead time. Every example from one patient must remain in a single split.

## Candidate outcomes

Select one primary endpoint that can be defined consistently and timestamped reliably. Candidates include:

- circulatory failure;
- initiation of vasopressors;
- initiation of mechanical ventilation;
- large-volume transfusion or hemorrhage resuscitation when reliably documented;
- ICU transfer or a composite deterioration event;
- death only as a secondary, longer-horizon endpoint.

Do not code missing or ambiguously documented interventions as negative events. Do not construct a broad composite until component timing and clinical interpretation have been audited.

## Inputs

Primary physiological variables:

- heart rate;
- respiratory rate;
- oxygen saturation;
- systolic, diastolic, and mean blood pressure where available;
- temperature;
- explicit missingness masks and time since last observation.

Potential treatment variables such as supplemental oxygen require special handling. A treatment may be a useful predictor but can also leak the target or encode clinician behavior. Report physiology-only and physiology-plus-treatment analyses separately.

## Comparison groups

### Direct outcome models

1. Current-value thresholds and clinically established scores where valid.
2. Logistic regression on current values, summary statistics, slopes, variability, and missingness.
3. Gradient-boosted trees on the same features.
4. GRU-D or another missingness-aware sequential classifier.

### Forecasting models

1. Persistence and seasonal-naive forecasts.
2. Autoregressive statistical baseline.
3. N-HiTS.
4. Temporal Fusion Transformer.
5. Toto 1 zero-shot.
6. Toto 2 zero-shot.
7. Toto 1 post-training or fine-tuning, if supported.

### Toto outcome variants

1. Direct classifier using observed history only.
2. Same classifier plus Toto point forecasts.
3. Same classifier plus Toto distributional summaries or quantiles.
4. Linear probe on frozen Toto representations.
5. Controlled fine-tuning with a classification head.

Keep observation windows, preprocessing, splits, classifier capacity, and tuning budget aligned wherever a causal comparison is intended.

## Metrics

Primary outcome metrics:

- AUPRC;
- sensitivity and positive predictive value at prespecified alert burdens;
- calibration intercept, slope, and expected calibration error or Brier score;
- median and distribution of correct-alert lead time.

Secondary outcome metrics:

- AUROC;
- specificity and negative predictive value;
- decision-curve or net-benefit analysis when assumptions can be justified;
- per-patient false-alert rate.

Forecasting metrics:

- MAE and RMSE;
- pinball loss for quantile forecasts;
- CRPS when a full predictive distribution is available;
- interval coverage and width;
- DTW or DILATE-style shape/timing metrics as secondary analyses.

Never infer clinical utility from forecasting metrics alone.

## Splits and tuning

- Use patient-disjoint partitions.
- Prefer chronological development, validation, and test splits within the primary dataset.
- Reserve hospitals or an independent dataset for external validation where endpoint mapping is credible.
- Fit normalization, imputation statistics, thresholds, calibration, and hyperparameters on development data only.
- Freeze the complete analysis before opening the final test set.
- Report the number of patients, encounters, prediction windows, and positive events in every split.

## Leakage controls

- Exclude measurements recorded after index time.
- Add an explicit gap between observation and outcome windows.
- Audit chart-time versus event-time semantics.
- Prevent duplicated or overlapping encounters from crossing splits.
- Remove variables that directly encode a target intervention unless running a clearly labeled treatment-aware analysis.
- Ensure imputation and resampling never use future observations.
- Audit whether missingness patterns reflect post-event documentation.

## Statistical analysis

- Use patient-clustered bootstrap confidence intervals.
- Compare models on identical test examples.
- Correct for multiple comparisons across Toto variants and major endpoints.
- Report absolute and relative changes with uncertainty, not only significance.
- Perform a sample-size and event-count analysis before training expensive models.

## Decision gates

### Gate A — Feasible endpoint

Proceed only if the primary outcome is timestamped, sufficiently frequent, and clinically interpretable.

### Gate B — Reproducible baseline

Proceed to Toto comparisons only after direct baselines reproduce plausible discrimination and calibration without leakage.

### Gate C — Forecast validity

Treat Toto forecasting as viable only if it is competitive across more than one horizon and does not obtain gains from invalid interpolation or scaling.

### Gate D — Incremental utility

Claim outcome-model value only if Toto improves the prespecified primary metric and maintains calibration and alert burden.

### Gate E — Transportability

Describe a result as generalizable only after temporal or external validation. Otherwise, label it an internal retrospective finding.

## Negative-result interpretation

A null result is publishable if the comparison is adequately powered and controlled. Distinguish among:

- Toto does not forecast clinical physiology better;
- Toto forecasts better but forecasts do not improve the outcome task;
- embeddings help even when explicit forecasts do not;
- gains disappear under shift or clinically meaningful operating points.

These outcomes answer different scientific questions and should not be collapsed into a single success/failure label.

## DARPA contingency

DARPA data are not required for the primary study. If access is later granted:

- map variables and endpoints before opening outcome labels;
- preserve the official observation gap, prediction window, lead-time calculation, and scoring;
- evaluate frozen public-data models without new model selection;
- report any post hoc adaptation separately;
- do not compare the public proxy task numerically with the DARPA leaderboard as if the labels and metric were identical.


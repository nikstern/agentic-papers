# JRESP Planning Packet

- Status: exploratory protocol design
- Primary path: public clinical datasets
- Optional path: frozen external validation on DARPA data if access becomes available

## Objective

Determine whether Toto forecasts or representations add clinically useful predictive information about future deterioration or intervention needs beyond current vital signs, observed vital-sign history, missingness patterns, and strong direct classifiers.

This is initially a retrospective decision-support study. It is not a clinical deployment, medical-device validation, or claim of improved patient outcomes.

## Planning artifacts

- [[study-protocol]] defines the hypotheses, comparison groups, evaluation rules, leakage controls, and decision gates.
- [[dataset-endpoint-matrix]] records candidate datasets, feasible endpoints, access constraints, and intended experimental roles.
- [[jresp-toto-medical-triage-research-direction]] contains the concise research framing and DARPA task reference.
- [[Medical-Time-Series]] links the supporting literature.

## Backlog map

| Phase | Backlog | Deliverable |
|---|---:|---|
| Protocol | 104 | Frozen protocol and analysis plan |
| Data access | 105 | Approved access and DUA-safe handling plan |
| Cohorts | 106 | Versioned cohorts, labels, and quality report |
| Direct baselines | 107 | Threshold, linear, tree, and GRU-D results |
| Forecasting | 108 | Comparable forecasting benchmark |
| Primary experiment | 109 | Incremental-utility and ablation results |
| Robustness | 110 | Cross-site, shift, subgroup, and alert-burden analyses |
| Publication | 111 | Reproducible artifacts, manuscript, and blog post |
| Optional DARPA | 112 | Frozen external validation if access is granted |

## Recommended execution order

1. Run tasks 104 and 105 in parallel where practical.
2. Do not begin final cohort extraction until endpoint definitions and DUAs are fixed.
3. Complete task 107 before interpreting Toto results.
4. Run tasks 108 and 109 on the same frozen splits and observation windows.
5. Open the final test partitions only after thresholds, hyperparameters, and ablations are frozen.
6. Treat task 112 as non-blocking and do not tune on DARPA data.

## Current decisions

- Already-captured physiological trajectories are the primary input; sensor estimation is out of scope for the first study.
- The central comparison is direct outcome prediction versus forecast- or representation-assisted outcome prediction under identical available information.
- Public datasets determine the primary result. DARPA performance, if available, is a separate external-validation result.
- A model is not considered useful solely because it improves forecasting error or AUROC; calibration, lead time, sensitivity, precision, and alert burden must also be acceptable.

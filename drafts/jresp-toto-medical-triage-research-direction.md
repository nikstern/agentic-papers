# JRESP / Toto Medical Triage Research Direction

## Research question

Does a pretrained time-series forecaster or its learned representation improve early prediction of life-saving interventions or physiological deterioration from already-captured vital-sign histories, beyond current values, simple temporal summaries, and strong direct classifiers?

## Evaluation principle

Compare forecast-assisted prediction and direct outcome prediction with identical observation windows and patient-level splits. Report intervention lead time, AUPRC, calibration, sensitivity and precision at clinically meaningful false-alert rates, as well as forecasting metrics. Include simple thresholds and missingness-aware clinical models so any gain can be attributed to temporal modeling rather than preprocessing or label leakage.

## DARPA task reference

The [DARPA Triage Challenge Data Competition](https://www.darpa.mil/research/challenges/darpa-triage-challenge/events/event-1/data-competition) asks systems to predict sets of life-saving interventions at repeated evaluation points. The observation window ends at each evaluation point; the target window begins 15 minutes later and continues to the end of care or four hours after admission. The challenge evaluates both prediction accuracy and prediction lead time. This task definition should be reproduced explicitly when competition data are used.

## Core evidence groups

- Direct trauma and life-saving-intervention prediction: papers 137–141.
- Clinical deterioration, missingness, and representation learning: papers 142–145.
- Forecasting and foundation-model comparators: papers 146–150.

Sensor-estimation work is secondary unless the experiment later consumes raw waveforms. The initial study should focus on the incremental outcome-prediction value of already-captured physiological trajectories.

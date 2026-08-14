# JRESP Dataset and Endpoint Matrix

Status: working decision aid. Access, versions, and label quality must be verified before the protocol is frozen.

| Dataset | Candidate role | Relevant inputs | Candidate endpoints | Strengths | Principal risks |
|---|---|---|---|---|---|
| MIMIC-IV + MIMIC-IV-ED | Primary development dataset | Repeated ED/ICU vital signs linked to hospital and ICU records | ICU transfer, vasopressor initiation, ventilation, transfusion, composite deterioration | ED context, linkable longitudinal records, established tooling | Credentialed access; intervention documentation can be incomplete; single health system; charting times require audit |
| eICU-CRD | Multicenter external or secondary development dataset | Periodic ICU vital signs, treatments, labs, severity information | Vasopressors, ventilation, circulatory deterioration, mortality | Many hospitals and heterogeneous practice patterns | ICU rather than prehospital/ED triage; site-specific documentation; credentialed access; endpoint mapping may differ from MIMIC |
| HiRID | High-resolution endpoint benchmark | Dense ICU physiological time series | Circulatory failure and benchmark deterioration tasks | High temporal resolution and established benchmark definitions | ICU setting; institutional shift; access and current permitted-use terms must be confirmed |
| VitalDB | Forecasting sanity check or secondary physiological study | Dense perioperative vital signs and waveforms | Hypotension or intraoperative instability | High-resolution signals and an existing Toto/MAP project | Surgical population and endpoint differ substantially from emergency triage; avoid presenting it as LSI validation |
| DARPA Triage Challenge data | Optional frozen external validation | Trauma observations and intervention history | Official life-saving-intervention set | Closest match to intended mass-triage application | Access uncertain; proprietary task data; metric and label structure differ from public proxies |

## Recommended initial design

### Preferred path

1. Use MIMIC-IV with MIMIC-IV-ED for the main development and temporal test cohorts if a reliable timestamped endpoint can be constructed.
2. Use eICU for cross-hospital validation when an outcome can be mapped without changing its clinical meaning.
3. Use HiRID circulatory failure as a separate high-resolution benchmark rather than forcing it into the same pooled label.
4. Reuse VitalDB only for physiological forecasting or hypotension analyses, clearly separated from emergency-triage claims.
5. Add DARPA only as a frozen external test.

### Fallback path

If MIMIC intervention labels prove too ambiguous:

- promote the established HiRID circulatory-failure task to the primary outcome benchmark;
- use MIMIC/eICU deterioration or mortality as secondary tasks;
- narrow the claim from intervention prediction to early physiological deterioration prediction;
- preserve the direct-versus-forecast-assisted comparison unchanged.

## Endpoint selection checklist

Before selecting the primary endpoint, record:

- the clinical definition and component events;
- timestamp source and expected timing error;
- observation gap and prediction horizon;
- event prevalence by dataset and split;
- censoring and competing-event rules;
- whether a predictor can directly encode the event;
- concordance of the definition across datasets;
- the smallest clinically meaningful improvement;
- the alert burden at which performance will be compared.

## Access and compliance checklist

- Complete individual credentialing and required human-subjects training.
- Sign each dataset-specific agreement rather than assuming one agreement covers all MIMIC modules.
- Pin dataset versions and retain permitted derived artifacts only.
- Keep credentialed row-level data and model inputs local.
- Verify whether checkpoints, embeddings, synthetic derivatives, cohort counts, and code may be released.
- Do not send credentialed data to third-party APIs unless the applicable agreement and service terms explicitly permit it.

## Decision record template

When task 104 selects the primary dataset and endpoint, append a dated entry here:

```text
Date:
Dataset and version:
Primary endpoint:
Observation window:
Exclusion gap:
Outcome horizon:
Reason selected:
Rejected alternatives:
Known label limitations:
External validation mapping:
```


# Prompt 09: Vibe-code one baseline module at a time

| | |
|---|---|
| **Phase** | III - AI coding and baseline validation |
| **Gate** | G2 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Build the baseline in small, tested cycles: load data, preprocess, run the method, evaluate, save predictions.

## Before you run it: attach or prepare
- Protocol (Prompt 07)
- Environment log (Prompt 08)
- Official reference code if one exists

## Prompt (verbatim from the course Instructions PDF)
```text
You are my AI pair programmer. I am reproducing [PUBLISHED BASELINE] for [DATASET] to produce [OUTPUT]. Work in short cycles: (1) specify the module and assumptions, (2) generate minimal executable code, (3) explain the logic and input/output shapes, (4) supply a unit/sanity test, and (5) wait for my genuine execution output before continuing. Implement data loading/validation, preprocessing, baseline model or algorithm, training/processing, evaluation, saving predictions and basic plots. Prefer official reference implementations when licensing permits, and record any deliberate deviations. Do not present pseudocode as runnable code, rewrite unrelated modules, or claim successful execution without logs.
```
**Project values for the brackets:** [PUBLISHED BASELINE], [DATASET], [OUTPUT] from Prompts 06-07.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Run every module and its test; paste the real output back.
- [ ] Read each function and be able to explain it to an examiner.
- [ ] Record in the log which parts the AI wrote and which you changed.

## Save the output to
- src/ and scripts/ with working baseline
- Prompt-to-code log entries (ai_assistance_log.md)

## Common mistakes
- Pasting a whole generated project without reading it.
- Letting the AI rewrite files that already worked.

## Done when
Baseline runs end to end and writes predictions and a metrics file.

## Evidence ledger for this step
Add each important claim here and label it. Leave blank until you have checked.

| Claim | Label (VERIFIED / INFERRED / UNKNOWN) | Source or run that shows it |
|---|---|---|
| | | |

## AI log entry (fill in only AFTER you really use the prompt)
| Field | Entry |
|---|---|
| Date | |
| Tool and model/version | |
| Prompt version used | |
| What the AI proposed | |
| My decision | |
| How I verified it | |
| Change to code, data or results | |
| Outcome | |

> Copy this entry into `ai_assistance_log.md` so the main log stays complete.

## Outcome (as of 2026-11-17)
Modules src/data.py, encode.py, metrics.py, train.py, cnn.py; scripts run_baseline.py, run_cnn.py, run_main.py; each tested by the student before use.

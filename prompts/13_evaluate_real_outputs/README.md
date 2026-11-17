# Prompt 13: Evaluate using real outputs only

| | |
|---|---|
| **Phase** | IV - Contribution and evidence |
| **Gate** | G3 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Write evaluation code with integrity checks and produce results.csv, tables and figures straight from saved outputs.

## Before you run it: attach or prepare
- Prediction files / logs for every method
- Gold labels and the split file

## Prompt (verbatim from the course Instructions PDF)
```text
I have real experimental outputs in [CSV/LOG/FILE] for [METHODS], evaluated on [DATASET/SPLIT]. Write evaluation code that checks ID/label alignment, missing values, partitions and metric direction before computing [METRICS]. Compare methods under consistent conditions, summarize multiple runs or uncertainty where applicable, and export traceable results.csv plus publication-quality PNG/PDF figures. Show how to audit for leakage and incompatible comparator settings. Never invent example values inside the final evaluation tables or claim statistical significance without a valid test and assumptions. Ask for required files before interpreting my numerical results.
```
**Project values for the brackets:** [CSV/LOG/FILE], [METHODS], [DATASET/SPLIT], [METRICS] from the frozen protocol and real outputs.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Re-run the script from a clean state and confirm identical numbers.
- [ ] Check every figure value against results.csv.
- [ ] If you report a significance test, record the test, assumptions and the runs it used.

## Save the output to
- scripts/evaluate.py
- results/results.csv
- results/figures/

## Common mistakes
- Typing numbers into tables by hand.
- Averaging over runs but hiding the spread.

## Done when
One command regenerates every table and figure from saved outputs.

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
317 main-grid records; analysis in results/analysis (scripts/analyze_main.py) and E48-E58 in evidence_ledger.md.

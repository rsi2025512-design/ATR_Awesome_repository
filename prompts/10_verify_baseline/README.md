# Prompt 10: Verify and reproduce the baseline

| | |
|---|---|
| **Phase** | III - AI coding and baseline validation |
| **Gate** | G2 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Audit the baseline against the original method and report discrepancies honestly. A baseline that merely runs is not verified.

## Before you run it: attach or prepare
- Code, configs, split, real logs and metrics
- The original paper or official code

## Prompt (verbatim from the course Instructions PDF)
```text
I have implemented [BASELINE] based on [PUBLISHED PAPER / OFFICIAL CODE]. Here are the code, dataset partition, configurations, actual logs and measured results: [FILES]. Audit the implementation against the original methodology: preprocessing, architecture, hyperparameters, random seeds, evaluation metric, data split and benchmark protocol. Design unit/sanity tests, inspect any discrepancy with reported results, and distinguish acceptable adaptations from changes that invalidate comparison. Produce a baseline validation report with VERIFIED, UNCERTAIN and NEEDS CORRECTION items, plus the exact additional checks required. Do not state that code is correct simply because it runs, and do not demand exact numerical replication under different conditions. Only after validation should we test extensions or comparisons.
```
**Project values for the brackets:** [BASELINE], [PUBLISHED PAPER / OFFICIAL CODE], [FILES] = your real code, split, configs, logs and metrics.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Run the sanity tests (e.g. shuffled labels give chance-level accuracy; a trivial majority-class baseline is below your method).
- [ ] Compare your number with the original paper and explain any gap.
- [ ] Re-check that no test data entered prompts or training.

## Save the output to
- baseline_validation.md (VERIFIED / UNCERTAIN / NEEDS CORRECTION)
- Measured baseline output in results/

## Common mistakes
- Claiming reproduction without any comparison to the published number.
- Hiding a discrepancy.

## Done when
Validation report written: Gate G2 submission.

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
Baselines validated: shuffled-label control at majority rate, CNN near published values, 5-seed DNABERT-2 and CNN numbers in baseline_validation.md. Leakage audit added (E28-E42, D10).

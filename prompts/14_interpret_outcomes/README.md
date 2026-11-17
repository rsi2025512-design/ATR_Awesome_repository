# Prompt 14: Interpret outcomes, including negative results

| | |
|---|---|
| **Phase** | IV - Contribution and evidence |
| **Gate** | G3 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Separate observations from explanations, report variation, cost and failures, and say which hypotheses held.

## Before you run it: attach or prepare
- results.csv, figures and logs
- Research questions and decision rules from the brief

## Prompt (verbatim from the course Instructions PDF)
```text
My research questions are [QUESTIONS], protocol is [SETUP] and actual results are [TABLES/LOGS/FIGURES]. Analyze each question by separating direct observations, possible mechanisms, alternative explanations and unsupported claims. Discuss relative performance, variation across runs, computational cost, error or failure modes and limitations of the dataset/protocol. Explain which hypotheses are supported, contradicted or still unresolved. Recommend no more than three high-value follow-up experiments ranked by cost and likely information gained. Avoid exaggerating small effects, turning negative findings into positive claims or assuming a metric measures things outside its scope.
```
**Project values for the brackets:** [QUESTIONS], [SETUP], [TABLES/LOGS/FIGURES] = your real results.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Check every sentence in the AI's analysis against a number in results.csv.
- [ ] Run your own error analysis on 20-30 failed examples.
- [ ] Delete any mechanism that you did not test.

## Save the output to
- Results and Discussion outline
- Limitations list

## Common mistakes
- Explaining why a result happened without testing it.
- Hiding a negative result.

## Done when
Each question has a verdict (supported / contradicted / unresolved) tied to a measured number: Gate G3.

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
Interpretation in paper section 4 and Discussion; claims limited to the simulation; untested explanations labelled.

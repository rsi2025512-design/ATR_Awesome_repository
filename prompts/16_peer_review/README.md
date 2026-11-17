# Prompt 16: Conduct a demanding technical peer review

| | |
|---|---|
| **Phase** | V - Write, review and publish |
| **Gate** | G4 |
| **Status** | [ ] not started  [x] in progress  [ ] done |

## Purpose
Use the AI as a tough reviewer, then fix real problems and keep a revision log.

## Before you run it: attach or prepare
- Compiled paper PDF

## Prompt (verbatim from the course Instructions PDF)
```text
Review my draft manuscript [PDF] as a critical technical reviewer. Assess significance, literature coverage, contribution validity, technical correctness, data leakage, fair baselines, experimental design, robustness of conclusions, reproducibility, figure/table accuracy, citation traceability and clarity. Separate MAJOR and MINOR concerns, give section/page locations, explain why each concern matters and propose one concrete remedy or experiment. Identify unsupported novelty and performance claims. Do not default to praise, invent missing literature or treat a fluent manuscript as scientifically sound. Return a prioritized revision checklist and an author-response table.
```
**Project values for the brackets:** [PDF] = your compiled draft.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Check each criticism against the paper; discard those that are wrong and note why.
- [ ] Do not accept suggested literature without finding it yourself.
- [ ] Re-run any experiment you add and update every affected table.

## Save the output to
- peer_review.md
- Revision log with author responses

## Common mistakes
- Treating all AI criticisms as correct.
- Fixing wording but not the experiment problems.

## Done when
Major concerns resolved or honestly listed as limitations.

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
Not yet performed on the final draft.

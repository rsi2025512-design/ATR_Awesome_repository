# Prompt 12: Choose and evaluate a defensible contribution

| | |
|---|---|
| **Phase** | IV - Contribution and evidence |
| **Gate** | G3 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Pick the pathway (A reproduction + extension, B controlled comparison, C targeted modification) that fits your validated baseline and resources.

## Before you run it: attach or prepare
- baseline_validation.md and real baseline results
- Research question and literature evidence

## Prompt (verbatim from the course Instructions PDF)
```text
My baseline [NAME] has been validated, and its actual results are [RESULTS]. My research question is [QUESTION], supported by [LITERATURE EVIDENCE]. Compare three feasible study pathways: A. reproduce an existing approach under a justified new condition; B. conduct a controlled comparative study of performance, generalization, robustness or efficiency; C. make a targeted, theoretically motivated extension or modification. For each, explain the scientific question, expected code changes, compute burden, advantages, failure risks and evidence needed. Recommend the most defensible pathway for my resources. Develop a fair test plan with appropriate comparisons and an ablation or failure analysis. If modification is chosen, guide me in making one isolated change while preserving the baseline implementation. Do not guarantee gains or mistake a routine comparison for novelty.
```
**Project values for the brackets:** [NAME], [RESULTS] = your validated baseline and its real numbers; [QUESTION] from Prompt 05; [LITERATURE EVIDENCE] from your verified sources.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Check that only ONE thing differs between each pair of conditions.
- [ ] Confirm the plan still matches the protocol you froze in Prompt 07 (log any change).
- [ ] Make sure there are two comparators or a written justification.

## Save the output to
- Chosen pathway and comparison plan in research_decisions.md (D-entry)
- Updated configs/

## Common mistakes
- Changing several things at once so no result can be explained.
- Selecting a pathway because it promises gains.

## Done when
Pathway chosen and justified; comparison plan matches the frozen protocol.

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
Contribution: simulated equal-effort comparison of manual vs AI-only vs AI-assisted labelling with four routing policies; protocol v2 frozen at commit 92e1e49 (D10, D11).

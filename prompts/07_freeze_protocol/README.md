# Prompt 07: Freeze an experiment blueprint before viewing results

| | |
|---|---|
| **Phase** | II - Experiment plan |
| **Gate** | G3 (draft before coding) |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Write the full protocol, metrics, seeds and checklist BEFORE running comparisons, so results cannot steer the design.

## Before you run it: attach or prepare
- Dataset sheet from Prompt 06
- one_page_brief.md

## Prompt (verbatim from the course Instructions PDF)
```text
Design a reproducible protocol for [QUESTION] on [DATASET] comparing [BASELINES] with [PROPOSED STUDY]. Include precise input/output definitions, modules, preprocessing, Mermaid architecture diagram, data partitions, controls, training or processing settings, evaluation metrics (with whether higher/lower is better), random seed plan, computational budget and expected table/figure formats. Include at least one deep analysis: ablation, error/failure, robustness, efficiency or sensitivity. Define threats to validity and a pre-experiment checklist to freeze the primary metric, test split and comparison protocol before viewing results. Explain how legitimate protocol changes should be logged later. Never fabricate anticipated outcomes.
```
**Project values for the brackets:** [QUESTION], [DATASET], [BASELINES], [PROPOSED STUDY] from Prompts 05-06.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Check the diagram matches what you will actually code.
- [ ] Commit the frozen config to git BEFORE running the final experiment (the commit is your evidence).
- [ ] Check metric directions (accuracy up is good, cost down is good).

## Save the output to
- protocol.md and a Mermaid diagram
- configs/frozen_protocol.yaml
- Pre-experiment checklist

## Common mistakes
- Editing the split after seeing a bad result without logging it.
- No deeper analysis planned.

## Done when
Protocol committed to git with a date, before the main experiment is run.

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

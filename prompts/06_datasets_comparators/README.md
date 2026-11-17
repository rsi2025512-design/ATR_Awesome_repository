# Prompt 06: Verify datasets and comparators

| | |
|---|---|
| **Phase** | II - Experiment plan |
| **Gate** | G2 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Choose a primary dataset and two comparators, and check access, licence, splits and leakage risks.

## Before you run it: attach or prepare
- one_page_brief.md
- Candidate dataset names (from your review or search)

## Prompt (verbatim from the course Instructions PDF)
```text
My question is [RESEARCH QUESTION] in [TASK/DOMAIN]. Recommend a primary dataset and two meaningful baseline methods or comparable controls, where feasible. For each candidate, identify the official source to verify, file structure, benchmark protocol, licensing/access terms, approximate compute requirement and common pitfalls. Explain an evaluation design appropriate to this domain: train/validation/test partitions when relevant, or a justified alternative for systems/HCI/security studies. Specify likely leakage risks such as patient-, subject-, document-, company- or time-level overlap as applicable. Do not present unverified access claims as facts. End by recommending the simplest credible baseline and a short independent-verification checklist.
```
**Project values for the brackets:** [RESEARCH QUESTION] from Prompt 05; [TASK/DOMAIN] = genomic data labelling.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Visit the official dataset page, not a mirror, and record the licence and citation.
- [ ] Check the dataset has a trustworthy reference label (gold or adjudicated), because accuracy needs ground truth.
- [ ] Check that few-shot examples used in prompts are not drawn from the test split.

## Save the output to
- dataset_baseline_validation_sheet.md
- Entry D6 in research_decisions.md

## Common mistakes
- Using noisy crowd labels as 'ground truth' without saying so.
- Putting prompt examples from the test set (leakage).

## Done when
One dataset and two comparators with verified access and licence recorded.

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

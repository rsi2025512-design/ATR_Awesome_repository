# Prompt 04: Check feasibility, novelty and resource access

| | |
|---|---|
| **Phase** | I - Review to research question |
| **Gate** | G1 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Test whether the idea is already done, whether data and code are accessible, and decide go / no-go.

## Before you run it: attach or prepare
- literature_to_experiment_map.md
- Your chosen idea in 2-3 sentences

## Prompt (verbatim from the course Instructions PDF)
```text
My candidate study is [IDEA]. Develop a feasibility and novelty-verification plan. Provide scholarly search strings and specific categories of neighboring work to inspect, without inventing titles, DOIs or URLs. Create a matrix with columns: published method, VERIFIED contribution (with source), limitation, proposed difference and evidence still missing. Check whether the dataset, code, model weights, license and benchmark protocol are accessible; flag all unresolved availability claims. Estimate computational and time constraints for [HARDWARE] and [WEEKS]. Narrow the study to a viable experimental question and recommend a fallback if the preferred repository, weights or dataset are unavailable.
```
**Project values for the brackets:** [IDEA] = the study chosen in Prompt 03; [HARDWARE] = RTX 4090 24 GB; [WEEKS] = about 1.5 days.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Run the search strings yourself on Google Scholar / Semantic Scholar / ResearchRabbit and record what you actually find.
- [ ] Read the abstracts of the closest neighbouring papers before writing 'proposed difference'.
- [ ] Download or open the dataset page and record the licence text.

## Save the output to
- novelty_feasibility_matrix.md
- Go/no-go decision as D4 in research_decisions.md

## Common mistakes
- Claiming novelty because the AI could not name a similar paper.
- Skipping the fallback plan.

## Done when
A go/no-go decision with a named fallback dataset or method.

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

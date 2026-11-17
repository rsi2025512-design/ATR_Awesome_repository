# Prompt 03: Map the literature to an executable experiment

| | |
|---|---|
| **Phase** | I - Review to research question |
| **Gate** | G1 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Pick three published methods you could reproduce and compare three study types. This is the mandatory bridge from papers to code.

## Before you run it: attach or prepare
- gap_matrix.md from Prompt 02
- The 3-5 original papers you verified

## Prompt (verbatim from the course Instructions PDF)
```text
My literature review [ATTACH REVIEW] identified these candidate gaps: [GAPS]. Identify three published methods from my review that could realistically be implemented or reproduced. For each method, map its original paper to the algorithm, dataset, code or model access, evaluation metric, known limitations and computational requirement. Distinguish verified access to code/weights from unverified suggestions. Compare three possible experimental studies: (A) reproduction plus extension, (B) controlled comparison, and (C) targeted modification. For each study state the smallest working baseline, the testable question, expected resource burden and evidence required. Recommend one minimum viable research experiment for [HARDWARE] and [TIME AVAILABLE]. Provide a literature-to-experiment mapping table and list what I must personally verify before coding. Do not propose an elaborate new architecture without a scientific rationale.
```
**Project values for the brackets:** [ATTACH REVIEW] = rsi2025512_Pratik.pdf; [GAPS] = the gap matrix from Prompt 02; [HARDWARE] = RTX 4090 24 GB; [TIME AVAILABLE] = until Wed 2026-11-18 morning, training under 4-5 hours.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Open each method's repository / model page yourself and note licence and last update.
- [ ] Check that the proposed metric is the one the original paper used.
- [ ] Check that the compute estimate fits the RTX 4090 and the 4-5 hour training cap.

## Save the output to
- literature_to_experiment_map.md
- Entry D3 in research_decisions.md

## Common mistakes
- Choosing an elaborate architecture you cannot run.
- Counting 'code exists' as verified when you have not opened the repo.

## Done when
One minimum viable experiment named, with every access claim marked VERIFIED or UNKNOWN.

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

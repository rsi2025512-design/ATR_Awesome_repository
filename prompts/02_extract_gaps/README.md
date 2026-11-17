# Prompt 02: Extract evidence-based research gaps

| | |
|---|---|
| **Phase** | I - Review to research question |
| **Gate** | G1 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Turn your review into five testable gaps, each tied to a specific passage or reference, and rank three.

## Before you run it: attach or prepare
- Your genomics review PDF (rsi2025512_Pratik.pdf)
- citation_verification sheet (to avoid building on weak references)

## Prompt (verbatim from the course Instructions PDF)
```text
Analyze my attached literature review [ATTACH PAPER]. Identify central methods, datasets, measured findings, author-reported limitations and unresolved questions. Propose five computationally testable research gaps. For each, cite the specific passage or reference in my review; clearly distinguish a limitation reported in the original paper from your own inference; state the experimental question it suggests and what evidence would test it. Flag any claims needing verification against the original publications. Rank three gaps by research significance, available resources and implementation feasibility. Do not claim novelty without a separate literature search.
```
**Project values for the brackets:** [ATTACH PAPER] = rsi2025512_Pratik.pdf. Add your constraints when you run it: one RTX 4090 (24 GB), training under 4-5 hours in total, deadline Wednesday 2026-11-18 morning.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Open your paper at each cited section and confirm the AI quoted it correctly.
- [ ] For each 'reported limitation', open the ORIGINAL paper and confirm the authors said it.
- [ ] Label each gap VERIFIED / INFERRED / UNKNOWN in the matrix.
- [ ] Start from the review's Sec 6 (challenges) and Sec 7 (research gaps) so the gaps are yours.

## Save the output to
- gap_matrix.md: source evidence -> candidate question -> possible experiment
- Entry D2 in research_decisions.md

## Common mistakes
- Accepting gaps that cite passages that are not in your paper.
- Treating the AI's inference as a limitation the authors reported.

## Done when
Five gaps in a matrix, each with a checked source, and three ranked.

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

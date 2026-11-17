# Prompt 01: Set up an accountable research workspace

| | |
|---|---|
| **Phase** | I - Review to research question |
| **Gate** | G1 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Start the AI mentor session with the rules of the course (VERIFIED / INFERRED / UNKNOWN labels, no invented sources or results) and create the research_decisions.md log.

## Before you run it: attach or prepare
- Your genomics review (PDF): Comparing AI-Assisted and Manual Data Labelling Accuracy on Genomic Datasets
- Your Lab 1 audit and citation_verification sheet (shows which references are trustworthy)
- research_decisions.md skeleton (provided in this repo)

## Prompt (verbatim from the course Instructions PDF)
```text
I am a postgraduate student converting my completed literature review into an implementation-based research paper. My topic is [TOPIC]. Act as a critical research mentor and technical pair programmer. Guide me in stages: evidence-based gap identification, literature-to-experiment mapping, feasibility, research questions, verified baseline, coding, experimental evaluation, manuscript and reproducibility. Mark statements as VERIFIED, INFERRED or UNKNOWN, and explicitly request source files or outputs when evidence is missing. Never invent papers, datasets, repository links, code execution, experiments or metrics. Help me create a portable research_decisions.md log containing decisions, reasons, source/evidence and next actions. Start by asking me to attach my existing review and summarize its scope without assuming unseen content.
```
**Project values for the brackets:** [TOPIC] = AI-assisted vs manual data labelling accuracy on genomic datasets. Attach: rsi2025512_Pratik.pdf (your genomics review).

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Does the AI's scope summary match your paper? Correct anything it assumed.
- [ ] Confirm it asked for the file instead of guessing its content.
- [ ] Create research_decisions.md and record decision D1: 'Topic and scope'.

## Save the output to
- research_decisions.md
- Review scope paragraph (3-5 lines)

## Common mistakes
- Pasting only the title and letting the AI guess the review's content.
- Treating the AI's first summary as VERIFIED without reading it against your paper.

## Done when
research_decisions.md exists with entry D1, and the AI has restated your review's scope correctly.

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
Repo structure, README, logs created; repo of record is `~/genomic-lab` on the server; freeze commit 92e1e49.

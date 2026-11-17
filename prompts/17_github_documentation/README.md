# Prompt 17: Prepare reproducible GitHub documentation

| | |
|---|---|
| **Phase** | V - Write, review and publish |
| **Gate** | G4 |
| **Status** | [ ] not started  [x] in progress  [ ] done |

## Purpose
Write the repository README using only commands you have really run; mark the rest [TEST REQUIRED].

## Before you run it: attach or prepare
- Project files, requirements.txt, configs
- The exact commands you ran
- Dataset licence

## Prompt (verbatim from the course Instructions PDF)
```text
Using my actual project files [FILES], environment [ENVIRONMENT], dataset access/license [RULES] and commands I have genuinely executed [COMMANDS], write a clear README with problem statement, setup, dataset preparation, baseline and experimental run commands, evaluation, reproduction of key figures, compute requirements, limitations, credits, license and citation. Mark unexecuted commands as [TEST REQUIRED] rather than pretending they work. Check that configuration files and dependency versions are included, that paths are realistic, and that no secrets, private data or restricted model weights are exposed. Add a minimum reproduction checklist for a second student.
```
**Project values for the brackets:** [FILES], [ENVIRONMENT], [RULES], [COMMANDS] = what you really ran.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Give a friend, or yourself on a clean folder, the README and follow it exactly.
- [ ] Search the repo for keys: `git grep -i -E 'api_key|secret|token'`.
- [ ] Check the dataset licence allows what you shipped.

## Save the output to
- README.md (project root)
- Reproduction checklist

## Common mistakes
- Commands in the README that you never ran.
- A leaked API key in git history.

## Done when
A second person can rerun the central experiment from the README: Gate G4.

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
README updated; GitHub push pending the student's commands.

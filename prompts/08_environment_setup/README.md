# Prompt 08: Configure and test the coding environment

| | |
|---|---|
| **Phase** | III - AI coding and baseline validation |
| **Gate** | G2 |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Build the project folders, pin dependencies and run a small environment test. Stop and share real console output.

## Before you run it: attach or prepare
- Your machine details (chip, RAM, Python version)
- Libraries you expect to use

## Prompt (verbatim from the course Instructions PDF)
```text
Act as my research software engineer. Set up [GOOGLE COLAB/LOCAL/INSTITUTIONAL GPU] for [METHOD] using [LIBRARIES]. Propose dependency versions and show how to check their compatibility instead of claiming untested compatibility. Provide installation commands, GPU/system diagnostics, dataset access procedures, project directories, random-seed controls and a clean repository structure (README, src, notebooks, configs, scripts, results, paper, requirements). Write a small executable environment test, state its expected output type and list failure diagnostics. Stop after this test and ask me to share the actual console output before proceeding.
```
**Project values for the brackets:** [GOOGLE COLAB/LOCAL/INSTITUTIONAL GPU] = LOCAL, RTX 4090 24 GB; [METHOD] and [LIBRARIES] from Prompts 03 and 07.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Run the test yourself and paste the real output back to the AI.
- [ ] Run `pip freeze > requirements.txt` only after the test passes.
- [ ] Store API keys in environment variables or a .env file listed in .gitignore.

## Save the output to
- Environment verification log (paste real console output)
- requirements.txt
- Repository skeleton

## Common mistakes
- Committing an API key.
- Moving on before the environment test passes.

## Done when
Environment test passes and the real output is saved in the log.

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
Conda env `aitr` (torch 2.5.1, CUDA 12.4, transformers 4.29.2, triton removed). Fixes in environment_log.md and D9. Data check, env test and model test passed on the student's server.

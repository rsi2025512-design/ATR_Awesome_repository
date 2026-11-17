# Prompt 11: Debug using actual evidence

| | |
|---|---|
| **Phase** | III - AI coding and baseline validation |
| **Gate** | Any time |
| **Status** | [ ] not started  [ ] in progress  [x] done (draft, needs your verification) |

## Purpose
Fix errors using the real traceback and the smallest safe change, then log the debugging case.

## Before you run it: attach or prepare
- Failing code
- Full real traceback or wrong output
- What you expected

## Prompt (verbatim from the course Instructions PDF)
```text
My code failed or behaved unexpectedly. Relevant code: [CODE]. Actual traceback or observed output: [ACTUAL OUTPUT]. Expected behavior: [EXPECTED BEHAVIOR]. Determine the likely causes, separate confirmed evidence from hypotheses, and suggest the smallest safe correction with an explanation of each change. Provide a verification test and one relevant edge case; state whether earlier results may need to be rerun. Ask for more diagnostic information when needed. Do not claim to have run the code or generate imagined logs. Help me add this case to my AI-assistance/debugging log.
```
**Project values for the brackets:** Use only when something actually fails. Paste the full real traceback.

Prompt text above is copied from the course Instructions PDF. Never paste invented numbers.

## What you must verify yourself
- [ ] Apply only the smallest change, run the test, and confirm the error is gone.
- [ ] Decide whether results generated before the fix must be re-run.
- [ ] Add the case to the debugging log immediately.

## Save the output to
- Corrected code in git (one commit per fix)
- Debugging entry in ai_assistance_log.md

## Common mistakes
- Pasting only the last line of the traceback.
- Forgetting to re-run old results after a data bug.

## Done when
Fix tested, committed and logged.

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
Debug cases (brotli, transformers versions, Triton, src.train import, nohup launch) recorded in environment_log.md with the evidence used.

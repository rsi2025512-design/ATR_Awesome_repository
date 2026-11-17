# AITR Lab 02: AI-assisted vs manual data labelling accuracy on genomic datasets

Student: Pratik Satpathy | Roll No.: RSI2025512 | Course: AI Tools for Research

Implementation study built on my literature review *Comparing AI-Assisted and Manual Data Labelling Accuracy on Genomic Datasets*. Follows the course Instructions PDF (18 prompts, gates G1-G4).

> **Status (2026-11-17):** main experiment complete (317 runs), paper drafted (`paper/paper.pdf`, 8 pages). Prompts 01-15 done as drafts needing the student's verification; Prompt 16 (peer review), 17 (GitHub documentation) and 18 (AI-use log) are in progress. The protocol was frozen at commit 92e1e49 before the main run.

## Constraints
- Compute: one RTX 4090 (24 GB); training under 4-5 hours in total.
- Deadline: Wednesday 2026-11-18 morning.

## Navigation
| File / folder | Purpose |
|---|---|
| [prompts/](prompts/README.md) | One README per prompt (18), verbatim prompt text, status |
| [RESEARCH_PLAN.md](RESEARCH_PLAN.md) | Compressed draft plan; the prompts decide the final study |
| [one_page_brief.md](one_page_brief.md) | Gate G1 brief |
| [research_decisions.md](research_decisions.md) | Decision log |
| [evidence_ledger.md](evidence_ledger.md) | VERIFIED / INFERRED / UNKNOWN ledger |
| [baseline_validation.md](baseline_validation.md) | Gate G2 report |
| [ai_assistance_log.md](ai_assistance_log.md) | AI-use log |
| [earlier_drafts/](earlier_drafts/) | Unverified drafts from the first attempt |
| `configs/`, `src/`, `scripts/`, `notebooks/` | Code |
| `data/README.md` | Dataset access |
| `results/`, `paper/` | Real outputs; LaTeX paper |

## Reproduce
```bash
# Commands as run on the lab server (env `aitr`; arguments per each script's --help).
# End-to-end re-run from a clean clone has NOT been tested.
python scripts/run_baseline.py --dataset human_enhancers_cohn --seed 0
python scripts/run_cnn.py --dataset human_enhancers_cohn
python scripts/leakage_check.py ; python scripts/leakage_analysis.py ; python scripts/leakage_rootcause.py
python scripts/run_main.py --seeds 0 1 3 --tag gpu0     # GPU 0 (seeds 0,1,3)
python scripts/run_main.py --seeds 2 4 --tag gpu1       # GPU 1 (seeds 2,4)
python scripts/analyze_main.py                          # results/analysis/*
python paper/make_tables.py --results results           # paper/generated/*
cd paper && latexmk -pdf paper.tex
```
Exact argument forms: check `--help` of each script; I have not verified them against this text.

## Licence and credits
Code: add a licence of your choice (not chosen yet). Data: Genomic Benchmarks (Gresova et al. 2023). Model: DNABERT-2 (Zhou et al. 2024); its licence has not been read by the student.

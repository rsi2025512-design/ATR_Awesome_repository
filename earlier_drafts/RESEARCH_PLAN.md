> **DRAFT.** Written before the prompts were re-run. Treat the chosen study below as a candidate to be confirmed or replaced by Prompts 02-06.

# Compressed plan: RTX 4090 (24 GB), result by Wednesday morning

Written Mon 2026-11-16, 19:15 IST. Deadline: Wed 2026-11-18 morning (about 36 hours, including sleep).
Labels: **VERIFIED** = seen at an official or primary page. **INFERRED** = my estimate, measure it. **UNKNOWN** = not checked.
This replaces the earlier MacBook/API assumption (decision D3/D4 superseded, see research_decisions.md).

## 1. Chosen study (provisional, freeze after the 1-page brief)

**Title idea:** *Simulating manual, AI-only and AI-assisted labelling of genomic sequences: accuracy against human effort.*

**Why this one**
- No paid API, no GPU wait: fine-tunes a small genome model locally.
- Has trusted gold labels, so "label accuracy" can be measured, which the review says needs a reference.
- Tests the review's three arms (Sec 8), confidence routing (Sec 5.1, gap 4), calibration (Sec 7) and annotator error / reliance (Sec 6.1, 6.4) in one design.
- Training stays far below the 4-5 hour cap (INFERRED, measure in the pilot).

**Verified ingredients**
| Item | Status | Detail |
|---|---|---|
| Genomic Benchmarks (Grešová et al., BMC Genomic Data 24:25, 2023, DOI 10.1186/s12863-023-01123-8) | VERIFIED | Nine datasets (promoters, enhancers, open chromatin; human, mouse, worm). Python package `genomic-benchmarks`; code at github.com/ML-Bioinfo-CEITEC/genomic_benchmarks; includes a simple CNN baseline; open access, data under CC0 |
| DNABERT-2 (Zhou et al., ICLR 2024, arXiv 2306.15006) | VERIFIED | Pretrained weights `zhihan1996/DNABERT-2-117M`; fine-tuning script in MAGICS-LAB/DNABERT_2 (takes train/dev/test CSVs). Licence: one listing says Apache-2.0, another says none stated, so UNKNOWN: read the repo |
| Setup risk | VERIFIED | Repo notes optional Triton/flash-attention install; "dependency conflicts" are a known risk |

## 2. Design (draft, to be frozen before the main run)

**Pool and gold labels.** Use the official train split as an "unlabelled pool" with its gold labels hidden from the arms. Use the official test split only for model accuracy.

**Simulated annotator (assumption, not a finding).** A human labels an item correctly with probability 1 - e. Test e in {0, 0.05, 0.10}. Optional reliance factor a: probability a human accepts a wrong AI suggestion unchecked (a in {0, 0.3}). Say clearly in the paper that humans are simulated.

**Arms**
| Arm | What happens | Human effort |
|---|---|---|
| Manual | Human labels every pool item | N |
| AI-only | DNABERT-2 trained on S human-labelled seed items labels the whole pool, no review | S |
| AI-assisted | Same model proposes labels; human reviews the B items chosen by a routing policy and fixes them | S + B |

**Routing policies (comparators):** random, least-confidence, margin, and a 3-seed ensemble disagreement. Routing is applied after prediction, so it needs no retraining (INFERRED).

**Primary metric:** accuracy of the final pool labels against gold, plotted against human effort as a fraction of N. **Secondary:** macro-F1, MCC, expected calibration error, test-set accuracy.
**Deeper analysis:** sensitivity to e and a; calibration plot; error analysis of items the router missed.

**Decision rule (draft):** confidence routing beats random routing if the paired difference in final-label accuracy at equal effort is at least 1 percentage point and the 95% bootstrap interval over seeds excludes zero. A negative result is reported as is.

**Baselines / validation (Gate G2):**
1. Full-label DNABERT-2 fine-tune and the package's CNN on the official split.
2. Majority-class and shuffled-label sanity checks.
3. Compare with the numbers in the Genomic Benchmarks paper (UNKNOWN until you read the table).

## 3. Compute estimate (INFERRED, measure first)
- Fine-tunes: about 2 datasets x 3 seeds x 3 seed sizes x 3 error rates = 54 small runs, a few minutes each. Plus 2 full-data runs of perhaps 10-30 minutes. Total expected 2-4 hours on a 4090.
- Pilot first: time 1 epoch on 1,000 items, then scale.
- Use bf16, batch size set by a quick memory test.

## 4. Timeline (IST)
| When | Do | Prompt | Output |
|---|---|---|---|
| Mon 19:15-20:15 | Confirm this design; one-page brief; check `nvidia-smi` and a Python environment test | 05, 08 | `one_page_brief.md`, env log |
| Mon 20:15-22:30 | Download data; load, check duplicates and class balance; run CNN and full DNABERT-2 baselines | 09 | baseline numbers |
| Mon 22:30-23:30 | Baseline validation; **freeze protocol and commit config to git** | 10, 07 | `baseline_validation.md`, `configs/frozen_protocol.yaml` |
| Tue 08:00-09:30 | Write experiment script; 2-run pilot; time it | 09, 11 | working script |
| Tue 09:30-15:00 | Main runs (GPU). Meanwhile verify citations and draft Related Work and Method | 15 | `results/` logs |
| Tue 15:00-18:00 | Evaluation script, figures, deeper analysis | 13, 14 | `results.csv`, figures |
| Tue 18:00-23:00 | Write Results, Discussion, Limitations, Abstract last; README | 15, 17 | paper draft |
| Tue night | Sleep |  |  |
| Wed 05:30-08:00 | AI peer-review pass, fixes, compile PDF, push repo, AI-use log | 16, 18 | final paper + repo |

## 5. First hour: run these and paste me the output (Prompt 08)
```bash
nvidia-smi
python3 --version
python3 -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
pip install genomic-benchmarks transformers datasets scikit-learn pandas matplotlib
python3 -c "from genomic_benchmarks.data_check import list_datasets; print(list_datasets())"
```
If the last command fails, tell me the exact error. I will not assume it works.

## 6. Risks and fallbacks
| Risk | Fallback |
|---|---|
| DNABERT-2 will not run (Triton or flash-attention conflicts) | Use the default attention path, or fall back to the package's CNN as the "AI model" and keep the same design |
| Time overrun | Drop to one dataset and two error rates |
| Gold labels are database-derived, not expert-adjudicated | State it as a limitation; this matches the review's point that references are not ground truth |
| Simulated annotators reviewers will question | Present as a controlled simulation, not evidence about real people |
| Results look too good | Re-check leakage (duplicate sequences across train/test) before trusting them |

## 7. What this study cannot show
Real human behaviour, ontology/metadata annotation (the review's main genomic tasks), or LLM labelling. These go in Limitations and Future Work.

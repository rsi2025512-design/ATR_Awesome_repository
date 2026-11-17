# Baseline validation (Prompt 10)

Single seed (0), 3 epochs, lr 3e-5 (INFERRED default, not from the DNABERT-2 repo), batch 32, bf16, standard attention (triton removed). 10% of training held out for monitoring; test used only for final metrics. All numbers below are from the student's run output on 2026-11-17.

| Run | Dataset | Test acc | Macro-F1 | ECE (15 bins) | Majority acc | Train time |
|---|---|---|---|---|---|---|
| Pilot (2,700 seqs, 1 epoch) | promoters | 0.836 | 0.836 | 0.038 | 0.544 | 5.0 s |
| Real labels, full | promoters | **0.910** | 0.910 | 0.075 | 0.544 | 100.7 s |
| Shuffled-label control | promoters | 0.544 | 0.354 | 0.006 | 0.544 | 99.4 s |
| Real labels, full | enhancers (cohn) | **0.751** | 0.751 | 0.124 | 0.500 | 97.6 s |

| Package CNN (10 ep, bs 64, emb 100: INFERRED) | promoters | 0.838 | 0.838 | 0.153 | 0.544 | 13.6 s |
| Package CNN (same) | enhancers (cohn) | 0.689 | 0.682 | 0.282 | 0.500 | 12.9 s |

Published package CNN accuracy (recorded in dataset_baseline_validation_sheet.md): promoters 84.6 (PyTorch) / 86.5 (TF).

## Checks
- [x] Shuffled-label control at chance (0.5443 vs majority 0.5441; model collapsed to one class) - VERIFIED
- [x] Beats majority baseline on both datasets - VERIFIED (single seed)
- [x] Package CNN reproduced within a reasonable band (promoters 0.838 vs 84.6/86.5; enhancers 0.689 vs 69.5/68.9) - VERIFIED, single seed; epochs/batch/embedding are INFERRED choices
- [ ] Multiple seeds / variance - NOT DONE (single seed)
- [ ] Near-duplicate / overlapping-locus leakage check - NOT DONE
- [ ] DNABERT-2 licence and default hyperparameters read - NOT DONE

## Observations (not conclusions)
- Enhancers: val accuracy fell from 0.755 (epochs 1-2) to 0.737 (epoch 3) while training loss kept falling; test ECE 0.124 is higher than promoters (0.075). Consistent with overfitting/overconfidence; one seed only.

## Update 2026-11-17: 5-seed baselines (results/analysis/baselines.csv)
| Dataset | Model | Seeds | Accuracy (%) | Macro-F1 (%) | ECE | Majority (%) |
|---|---|---|---|---|---|---|
| Promoters | DNABERT-2 | 5 | 92.4 ± 1.0 | 92.4 | 0.061 | 54.4 |
| Promoters | package CNN | 5 | 83.5 ± 0.6 | 83.4 | 0.157 | 54.4 |
| Enhancers | DNABERT-2 | 5 | 74.4 ± 0.8 | 74.3 | 0.136 | 50.0 |
| Enhancers | package CNN | 5 | 66.9 ± 1.4 | 65.5 | 0.303 | 50.0 |

- [x] Multiple seeds / variance: DONE (5 seeds). The single-seed table above is superseded.
- [x] Leakage check: DONE (E28-E42). Promoters test is 45.6% >80% overlapping with train, almost all negative; accuracy there is not generalisation. Enhancers chosen as primary (D10).
- [ ] DNABERT-2 licence and default hyperparameters read: NOT DONE (student to do; stated as a limitation in the paper).
- CNN is 1.1 pp (promoters) and 2.6 pp (enhancers) below the lower published figures; the package applies BCE-with-logits to a sigmoided output (kept as shipped).

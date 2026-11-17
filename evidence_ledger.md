# Evidence ledger

| # | Claim | Label | Source / run | Date |
|---|---|---|---|---|
| E1 | Genomic Benchmarks has 9 datasets; sizes and CNN baselines as in the paper table | VERIFIED (article text; confirm numbers in the paper) | PMC10150520, DOI 10.1186/s12863-023-01123-8 | 2026-11-16 |
| E2 | Article CC BY 4.0; CC0 waiver stated for its data; repo licence not stated | VERIFIED (statement); repo licence UNKNOWN | same | 2026-11-16 |
| E3 | Train/test counts per dataset | UNKNOWN | not in article | |
| E4 | No deduplication described for these datasets | VERIFIED (absence in article text) | same | 2026-11-16 |
| E5 | DNABERT-2 weights and fine-tune script exist | VERIFIED | HF `zhihan1996/DNABERT-2-117M`; GitHub MAGICS-LAB/DNABERT_2 | 2026-11-16 |
| E6 | DNABERT-2 licence | UNKNOWN (listings conflict) | | |
| E7 | CoAnnotating: entropy-guided allocation; up to 21% over random | VERIFIED (abstract) | arXiv 2310.15638 | 2026-11-16 |
| E8 | Rogic et al. 77% / 59% / over 200 reference errors | VERIFIED (abstract) | PubMed 42483875 | 2026-11-16 |
| E9 | HILTS exists (Barbosa et al., Information Systems 138) | VERIFIED | ScienceDirect, ACM DL listings | 2026-11-16 |
| E10 | Routing and active learning already studied in other domains | INFERRED | search snippets | |
| E11 | Training under 4-5 h on a 4090 | INFERRED | needs pilot timing | |
| E12 | Server has RTX 4090 24 GB (GPU 0) and RTX 4070 Ti 12 GB (GPU 1), driver 575.64.03 CUDA 12.9 | VERIFIED | student's nvidia-smi output | 2026-11-16 |
| E13 | torch not installed on server (system Python 3.10.12) | VERIFIED | student's console output | 2026-11-16 |
| E14 | genomic-benchmarks lists the 9 datasets | VERIFIED | student's console output | 2026-11-16 |
| E15 | Env test passed: torch 2.5.1 (CUDA 12.4), RTX 4090 23.5 GiB, bf16 ok, transformers 5.20.2 | VERIFIED | student's notebook output | 2026-11-16 |
| E16 | Both datasets have 0 exact duplicates within/between splits; constant sequence length (251 / 500 bp) in both classes | VERIFIED | data_check.py output | 2026-11-16 |
| E17 | Promoters test majority-class accuracy = 4915/9034 = 54.4%; enhancers is balanced (50%) | VERIFIED (arithmetic on E16 counts) | counts above | 2026-11-16 |
| E18 | DNABERT-2-117M loads (117.1M params) under transformers 4.x + torch 2.5.1 | VERIFIED | student's model_test output | 2026-11-16 |
| E19 | DNABERT-2 forward pass fails in its Triton flash-attn kernel on triton 3.1.0 | VERIFIED | traceback | 2026-11-16 |
| E20 | DNABERT-2 forward pass works with triton removed (standard attention); output (1,17,768) | VERIFIED | student's model_test output | 2026-11-16 |
| E21 | Promoters pilot (2,700 seqs, 1 epoch): test acc 0.836, 5.0 s | VERIFIED | student's run output | 2026-11-17 |
| E22 | Promoters full real-label run: test acc 0.9100, macro-F1 0.9100, ECE 0.0749, 100.7 s | VERIFIED | student's run output | 2026-11-17 |
| E23 | Promoters shuffled-label control: test acc 0.5443 (majority 0.5441), macro-F1 0.354 | VERIFIED | student's run output | 2026-11-17 |
| E24 | Enhancers full real-label run: test acc 0.7510, macro-F1 0.7507, ECE 0.1236, 97.6 s | VERIFIED | student's run output | 2026-11-17 |
| E25 | One fine-tune of ~100 s means a full 5-seed study is compute-feasible | INFERRED | E22, E24 timings | 2026-11-17 |
| E26 | Package CNN promoters: test acc 0.8383, F1 0.8381, ECE 0.1534; enhancers: acc 0.6891, F1 0.6824, ECE 0.2822 | VERIFIED | student's run output | 2026-11-17 |
| E27 | CNN loss stays ~0.55 at 85% acc and ECE is high; cause suspected: sigmoid output fed to BCE-with-logits in package code | INFERRED | package source + run output | 2026-11-17 |
| E28 | Promoters: 45.6% of test seqs share >80% of 16-mers with train (both strands), 42.8% share >95%; enhancers: 0.86% and 0.07% | VERIFIED | student's leakage_check output | 2026-11-17 |
| E29 | Cause of promoter overlap (overlapping windows / repeated loci) | UNKNOWN | not yet analysed | 2026-11-17 |
| E30 | Promoter accuracy (DNABERT-2 0.910, CNN 0.838) may be inflated by train/test overlap | INFERRED (E28); to be tested by stratified accuracy | | 2026-11-17 |
| E31 | Promoters, overlap bins (<=5/5-50/50-80/>80%): n = 2694/1995/225/4120; neighbour-label agreement 0.742/0.951/0.929/1.000 | VERIFIED | student's leakage_analysis output | 2026-11-17 |
| E32 | Promoters DNABERT-2 accuracy (seeds 0-3): <=5% bin 0.751/0.813/0.831/0.822; >80% bin 0.993/0.989/0.987/0.987. CNN: <=5% 0.599/0.568/0.631/0.584; >80% 0.953/0.964/0.942/0.950 | VERIFIED | same output | 2026-11-17 |
| E33 | Direct class balance by overlap bin on promoters test: positive share 0.995 / 0.992 / 0.653 / 0.026 (bins <=5, 5-50, 50-80, >80%) | VERIFIED | student's terminal output 2026-11-17 | 2026-11-17 |
| E34 | Overlap with train is almost a class marker on promoters: 97.4% of >80%-overlap test seqs are negative, 99.5% of <=5%-overlap are positive | VERIFIED (from E33) | | 2026-11-17 |
| E35 | Enhancers: accuracy nearly flat across overlap bins (<=5%: DNABERT-2 0.743, CNN 0.682 vs overall 0.751 / 0.689); only 61 seqs >80% | VERIFIED | same output | 2026-11-17 |
| E36 | Promoters seeds 0-3: DNABERT-2 acc 0.910/0.929/0.934/0.930 (mean 0.926, sd 0.011); CNN 0.838/0.827/0.843/0.831 (mean 0.835, sd 0.007) | VERIFIED (seeds 0-3 only; batch still running) | same output | 2026-11-17 |
| E37 | Promoters train, inside-train redundancy: negatives share on average 98.2% of 16-mers with other train seqs (99.3% have >50% shared); positives 9.9% (4.9% have >50%) | VERIFIED | student's leakage_rootcause output | 2026-11-17 |
| E38 | Distinct-16-mer fraction per sequence is 0.998 (neg) and 0.996 (pos), so the redundancy is not low-complexity repeats inside a sequence | VERIFIED | same output | 2026-11-17 |
| E39 | Test negatives sharing >80% with train: only 6% (117/1947) are explained by one train sequence at one shift (>=90% of shared 16-mers); those have |shift| 1-10 (39) or 11-50 (78) | VERIFIED | same output | 2026-11-17 |
| E40 | Cause: promoter negatives are densely overlapping windows of shared regions (each covered by several training windows) | INFERRED (E37-E39); benchmark construction not checked against source | | 2026-11-17 |
| E41 | Promoters test contains only about 30 negatives with <=50% overlap (14 + 16, from E31/E33), so generalisation to unseen negatives cannot be measured on this split | INFERRED (arithmetic on E31, E33) | | 2026-11-17 |
| E42 | Enhancers train, inside-train redundancy: negatives share 15.2% of 16-mers with other train seqs on average (8.0% have >50%), positives 7.8% (2.3% >50%); only 60 test seqs share >80% with train | VERIFIED | student's leakage_rootcause output | 2026-11-17 |
| E43 | Planned main study: 60 main + 180 sensitivity AI-assisted fine-tunes, about 40 s each, about 2.7 h on one RTX 4090 | INFERRED (E22/E24 timings scaled to 5,000 + labelled items) | | 2026-11-17 |
| E44 | Pilot (seed 0, e=0.05, a=0, s=300, s'=1000): manual(300) 0.6678, manual(1000) 0.7329, AI-only 0.6595, AI-assisted random/least-conf/margin/ensemble 0.6632/0.6703/0.6703/0.6631; about 32.5 s per AI-assisted run | VERIFIED | student's records_a.jsonl | 2026-11-17 |
| E45 | AI-assisted underperforms manual at equal human labels because pseudo-labels dominate the fit | INFERRED; diagnostic columns (pseudo_label_acc etc.) not yet inspected | | 2026-11-17 |
| E46 | Main run launched 2026-11-17 on both GPUs (seeds 0,1,3 on RTX 4090; seeds 2,4 on RTX 4070 Ti), started 14:10 server time; 4070 Ti about 1.8x slower per run (20 s vs 11 s for a manual run) | VERIFIED | student's ps and log output | 2026-11-17 |
| E47 | Main grid complete: 317 records (240 AI-assisted + 44 manual + 33 AI-only); both processes ended with exit 0; exploratory routed_only arm not run | VERIFIED | student's record count and job status | 2026-11-17 |
| E48 | 5-seed baselines (test acc): promoters DNABERT-2 92.4 ± 1.0, CNN 83.5 ± 0.6; enhancers DNABERT-2 74.4 ± 0.8, CNN 66.9 ± 1.4; ECE 0.061/0.157/0.136/0.303 | VERIFIED | results/analysis/baselines.csv | 2026-11-17 |
| E49 | Main cell (e=0.05, a=0), 1000→3000: ensemble disagreement beats random by +2.8 pp (95% CI 1.3 to 4.5), positive in 5/5 seeds | VERIFIED | results/analysis/main_comparisons.csv | 2026-11-17 |
| E50 | Least-confidence/margin vs random at 1000→3000: +0.6 pp (−0.4 to 1.5), 4/5 seeds positive; no clear gain at smaller budgets for any policy | VERIFIED | main_comparisons.csv | 2026-11-17 |
| E51 | Of 24 main-cell comparisons: 1 clear gain, 3 clearly worse, 20 no clear difference (frozen rule: ≥1.0 pp and lower 95% bound >0) | VERIFIED | main_comparisons.csv | 2026-11-17 |
| E52 | At 3,000 labels AI-assisted vs Manual(3000)=73.0%: random −3.5 (−5.5, −1.6), least-conf −2.9 (−5.4, −0.7), ensemble −0.7 (−1.5, 0.1) | VERIFIED | main_comparisons.csv | 2026-11-17 |
| E53 | AI-only vs manual at s=300: +3.1 pp (−0.8, 7.4), no clear difference | VERIFIED | main_comparisons.csv | 2026-11-17 |
| E54 | Proposer test accuracy 63.6/68.1/70.5% for s=100/300/1000; proposer correct on 70.5% of random, 51.9% of least-conf and 50.2% of ensemble-selected items at 1000→3000 | VERIFIED | records, diagnostics | 2026-11-17 |
| E55 | ECE at 3,000 labels: manual 0.095; AI-assisted random 0.231, least-conf 0.248, ensemble 0.210; AI-only(1000) 0.265 vs manual(1000) 0.176 | VERIFIED | main_cell_accuracy.csv | 2026-11-17 |
| E56 | Sensitivity (seeds 0–2, point estimates): ensemble gain over random 0.5 to 3.1 pp in all six cells; least-conf −0.3 to 1.3 pp | VERIFIED | sensitivity_accuracy.csv | 2026-11-17 |
| E57 | Pseudo-label noise (~30% wrong) is why AI-assisted trails manual | INFERRED; untested because the routed_only arm was not run | | 2026-11-17 |
| E58 | Margin and least-confidence select identical items for two classes (design redundancy found after the run) | VERIFIED (identical results in all cells) | main_cell_accuracy.csv | 2026-11-17 |

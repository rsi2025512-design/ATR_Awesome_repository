# Dataset and baseline validation sheet (Prompt 06)

Question: at equal total human labels, does confidence routing beat random routing for AI-assisted labelling of genomic sequences? Domain: genomic sequence classification (regulatory elements).

## Candidate datasets (from the Genomic Benchmarks paper table; fetched 2026-11-16)
| Dataset | Organism | Classes | Total seqs | Class ratio | Median length | CNN acc (PyTorch / TF) | Use |
|---|---|---|---|---|---|---|---|
| human_nontata_promoters | Human | 2 | 36,131 | 1.2 | 251 | 84.6 / 86.5 | **Primary** (short, fast, moderate difficulty) |
| human_enhancers_cohn | Human | 2 | 27,791 | 1.0 | 500 | 69.5 / 68.9 | **Secondary** (harder; more room for routing) |
| human_ocr_ensembl, human_enhancers_ensembl | Human | 2 | 174,756; 154,842 | 1.0 | 315; 269 | 68.0 / 68.8; 68.9 / 81.1 | Not used (large) |
Official source: github.com/ML-Bioinfo-CEITEC/genomic_benchmarks and PyPI `genomic-benchmarks`; paper DOI 10.1186/s12863-023-01123-8.
Licence: article is CC BY 4.0; it states the CC0 waiver applies to the data it makes available; repository licence UNKNOWN (check).
File structure / train-test counts: UNKNOWN until loaded (the article does not give them).
Protocol (from paper): train/test subsets, negatives sampled from the same genome with non-overlapping intervals, fixed seed. No deduplication described.

## Baselines and controls
| Role | Method | Source | Status |
|---|---|---|---|
| Baseline 1 | Package CNN | Genomic Benchmarks paper/repo | Published numbers above; reproduce |
| Baseline 2 | DNABERT-2 full-label fine-tune | MAGICS-LAB/DNABERT_2 | No published number for these datasets known to me (UNKNOWN); licence UNKNOWN |
| Control | Majority class | n/a | Compute |
| Control | Shuffled labels | n/a | Should be near chance |
| Comparator | Random routing; "more training labels" | Design | Defined in protocol |

## Evaluation design
- Pool = official train split. Gold labels of the pool are used **only to score and to simulate humans**, never to train a model except through the S+B items the simulated human reviews.
- Test = official test split, only for model accuracy reporting.
- Seed set S is split 80/20 for training and early stopping (no extra gold labels used for tuning).
- Hyperparameters fixed in advance from the DNABERT-2 script defaults (to be read from the repo).

## Leakage risks
1. Identical or near-identical sequences in train and test (no dedup described).
2. Overlapping genomic windows around the same locus for positives; negatives from the same genome.
3. Using test or pool gold labels for tuning or early stopping.
4. Selecting the seed set after looking at pool labels.
5. Class-length artefacts (e.g., one class systematically different length) letting a model score well without biology.

## Simplest credible baseline
CNN from the package on primary dataset, compared with its published accuracy.

## Independent-verification checklist
- [ ] Load both datasets; record train/test counts and class counts.
- [ ] Count exact duplicate sequences within and across splits (and report).
- [ ] Compare class length distributions.
- [ ] Reproduce CNN accuracy within a reasonable band; explain any gap (do not demand exact replication).
- [ ] Majority-class and shuffled-label controls behave as expected.
- [ ] Read the DNABERT-2 licence and script defaults.

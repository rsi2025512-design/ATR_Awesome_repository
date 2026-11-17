# Literature-to-experiment map (Prompt 03)

Labels as before. "Checked" = seen at an official or primary page in this session. No code was run.
Compute: RTX 4090 24 GB. Time: until Wed 2026-11-18 morning; training under 4-5 h.

## Three methods

| | M1: DNABERT-2 fine-tuning | M2: Genomic Benchmarks CNN baseline | M3: Uncertainty routing (CoAnnotating idea) |
|---|---|---|---|
| Original paper | Zhou et al., arXiv 2306.15006 (ICLR 2024). VERIFIED exists | Grešová et al., BMC Genomic Data 24:25 (2023), DOI 10.1186/s12863-023-01123-8. VERIFIED | Li et al., EMNLP 2023, arXiv 2310.15638 (review ref [14]). VERIFIED |
| Algorithm | 117M-parameter transformer pretrained on multi-species genomes, BPE tokenisation | Simple CNN supplied in the package | Sort items by LLM-response entropy; send least certain to humans; compare with random allocation |
| Dataset | Own GUE benchmark; fine-tune script takes train/dev/test CSVs. Used here on Genomic Benchmarks (my choice) | Genomic Benchmarks: 9 datasets, regulatory elements; data stated CC0 | NLP text tasks (not genomic) |
| Code / model access | HF `zhihan1996/DNABERT-2-117M`; repo MAGICS-LAB/DNABERT_2. VERIFIED existence. Licence conflicting between listings (Apache-2.0 vs none stated): UNKNOWN | PyPI `genomic-benchmarks`; GitHub ML-Bioinfo-CEITEC/genomic_benchmarks. VERIFIED existence. Repository licence UNKNOWN | GitHub SALT-NLP/CoAnnotating. VERIFIED existence; licence UNKNOWN |
| Metric | Accuracy, MCC (to choose) | Accuracy and F1 (PyTorch and TensorFlow versions) | Quality vs random allocation; cost-performance |
| Known limitations | Optional Triton/flash-attention install; possible dependency conflicts (listing text) | Simple model; datasets have no described deduplication | NLP; relies on repeated LLM prompting (not used here) |
| Compute | Fine-tune a 117M model: minutes for small seed sets, longer for full data (INFERRED, measure) | Small | Post-hoc on model probabilities: negligible |

Published CNN baseline numbers (from the fetched article text; confirm against the paper's table): human_nontata_promoters 84.6 / 83.7 (PyTorch acc / F1), 86.5 / 84.4 (TensorFlow); human_enhancers_cohn 69.5 / 67.1 (PyTorch), 68.9 / 71.3 (TensorFlow).

## Three study designs

| | A. Reproduction + extension | B. Controlled comparison | C. Targeted modification |
|---|---|---|---|
| Smallest working baseline | Reproduce CNN numbers above | Same trained seed models; arms and routing compared post hoc | DNABERT-2 plus one added component |
| Testable question | Do I reproduce the published CNN accuracy? | At equal human labels, does confidence routing beat random routing and the "spend it on more training labels" option? | Does a single change improve accuracy? |
| Resource burden | Low | Medium (5 seeds x 4 seed sizes x 2 datasets of fine-tunes) | Medium |
| Evidence needed | Gap analysis vs published numbers | Accuracy vs effort curves, calibration, noise sensitivity | Isolated change, ablation |

## Recommended minimum viable experiment (INFERRED)
Pathway **B**, preceded by baseline validation (A-style): reproduce the CNN accuracy on two datasets, fine-tune DNABERT-2 on full labels, then run the simulated three-arm and routing comparison.

## What you must personally verify before coding
- [ ] Open the Genomic Benchmarks paper's table and confirm the CNN numbers and dataset sizes.
- [ ] Load both datasets with the package and record train/test counts (the article did not give them).
- [ ] Check duplicate sequences within and across train/test.
- [ ] Read the DNABERT-2 repo licence file and the fine-tune script defaults (learning rate, epochs, batch size).
- [ ] Read CoAnnotating Methods for how routing is evaluated.

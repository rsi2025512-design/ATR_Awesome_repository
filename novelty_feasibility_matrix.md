# Novelty and feasibility matrix (Prompt 04)

Date 2026-11-16. Search depth: shallow. One search this session returned result titles only; earlier searches covered the review's own papers. **Not finding a paper is not evidence that none exists.** No novelty claimed.

## Search strings to run yourself (Google Scholar, Semantic Scholar, ResearchRabbit)
- `active learning DNA sequence classification foundation model label efficiency`
- `human-in-the-loop genomic annotation simulated annotator noise`
- `confidence routing human review calibration genomic sequence classifier`
- `selective labelling OR "learning to defer" regulatory element classification`
- `Genomic Benchmarks active learning OR label noise`
Categories of neighbouring work: active-learning surveys; human-LLM allocation methods; calibration of neural classifiers; DNA-model benchmarks; label-noise methods.

## Matrix
| Published method | VERIFIED contribution (source) | Limitation | Proposed difference | Evidence still missing |
|---|---|---|---|---|
| CoAnnotating | Entropy-guided allocation of items between humans and an LLM; up to 21% over random (arXiv abstract, project page, repo README) | NLP, not genomic | Same routing idea on genomic sequence classification with a fine-tuned DNA model | Read results tables |
| Genomic Benchmarks | Nine regulatory-element datasets, CNN baseline, public-domain data statement (paper text) | No dedup described | Used as the dataset, not a method | Train/test counts |
| DNABERT-2 | Genome foundation model with fine-tune script (repo, arXiv) | Install fragility | Used as the "AI labeller" | Licence; hyperparameter defaults |
| DNA-model benchmark papers (titles only seen) | Compare DNA foundation models on genomic tasks | Not read | Different question: labelling effort, not model ranking | Open and read |
| Confidence-routing studies in other domains (snippets seen in earlier searches) | Routing human review by model confidence is studied elsewhere | Other domains | Genomic sequence setting; calibration; noise sensitivity | Open and read |

**Verdict (INFERRED):** routing, active learning and calibration are established. A defensible contribution is a controlled, reproducible simulation of the three labelling arms on public genomic benchmarks with noise sensitivity. Frame it as a controlled comparison.

## Access checks
| Item | Status |
|---|---|
| Datasets | VERIFIED in paper: 9 datasets, sizes listed; data stated CC0 (the article states the CC0 waiver applies to its data; repository licence UNKNOWN) |
| DNABERT-2 weights | VERIFIED existence on Hugging Face; licence UNKNOWN |
| Benchmark protocol | Splits regenerated with a fixed seed (paper text); train/test counts UNKNOWN; no dedup described |
| Code | Repos exist (VERIFIED); nothing run yet |

## Compute and time (INFERRED, measure first)
RTX 4090. Seed-model fine-tunes: 5 seeds x 4 seed sizes x 2 datasets = 40 small runs. Full-label baselines: 2 datasets x up to 3 seeds. Routing and arm simulation is post hoc (negligible). Expected total training 2-4 h; reduce seeds or dataset if the pilot is slow.

## Narrowed question
At equal total human labels, does routing the model's least-confident pool items to a (simulated) human beat random routing, and beat spending the same labels on extra training data, across annotator error rates?

## Go / no-go
**GO**, conditional on: environment test passes (Prompt 08, running on your server), datasets load, DNABERT-2 licence checked.
## Fallbacks
1. DNABERT-2 will not run: use the package CNN as the AI model; same design.
2. Too slow: one dataset, 3 seeds, fewer seed sizes.
3. Weights unavailable: smaller Nucleotide Transformer model (not yet checked, UNKNOWN).

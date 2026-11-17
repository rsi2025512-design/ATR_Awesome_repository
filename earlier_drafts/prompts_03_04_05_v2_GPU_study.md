# Prompts 03, 04, 05 redone for the GPU study (2026-11-16)

Labels: VERIFIED = seen at an official/primary page. INFERRED = my reasoning. UNKNOWN = not checked.
This supersedes the API-based mapping in literature_to_experiment_map.md and novelty_feasibility_matrix.md for the chosen study. Those files stay as the record of the first plan.

## Prompt 03: literature-to-experiment map

| Review reference / source | Role in the new study | Access | Status |
|---|---|---|---|
| Grešová et al. 2023, BMC Genomic Data 24:25 (not in your review's reference list: add after verifying) | Dataset and baseline CNN | Python package `genomic-benchmarks`; GitHub ML-Bioinfo-CEITEC/genomic_benchmarks; data CC0 | VERIFIED existence, access, licence statement. Which of the nine datasets to use, sizes, and published baseline numbers: UNKNOWN |
| Zhou et al., DNABERT-2 (arXiv 2306.15006; ICLR 2024) (not in your review) | The "AI labeller" | HF `zhihan1996/DNABERT-2-117M`; repo MAGICS-LAB/DNABERT_2 | VERIFIED existence and fine-tune script; licence conflicting (Apache-2.0 vs none stated): UNKNOWN; install conflicts possible |
| Li et al. 2023, CoAnnotating (review [14]) | Motivates uncertainty-guided allocation between AI and human; comparator idea (random vs uncertainty routing) | arXiv 2310.15638; code SALT-NLP/CoAnnotating | VERIFIED abstract: up to 21% over random baseline (NLP tasks) |
| Ren et al. 2021; Cacciarelli & Kulahci 2024 (review [1],[2]) | Uncertainty / margin / committee query strategies for routing | Papers | Existence VERIFIED earlier; strategy details UNKNOWN until read |
| Sheng et al. 2008 (review [26]) | Justifies simulated noisy labellers and repeated labelling | Paper | Existence VERIFIED earlier |
| Buçinca et al. 2021 (review [3]) | Justifies the reliance parameter a | Paper | Existence VERIFIED earlier |
| Northcutt et al. 2021 (review [20]) | Optional: flag mislabelled items | Paper | Existence VERIFIED earlier |

Pathway: **B, controlled comparison**, preceded by baseline validation (full-label DNABERT-2 and CNN on the official split).
Smallest working baseline: fine-tune on the full training split and report test accuracy and MCC.
Evidence needed: validated baseline, equal-effort comparison across arms and policies, calibration, sensitivity, error analysis.

**What you must personally verify before coding**
- [ ] Open the Genomic Benchmarks paper table: dataset sizes, class balance, published baseline accuracy.
- [ ] Open the DNABERT-2 repo: licence file, requirements, fine-tune arguments.
- [ ] Check train/test overlap (duplicate sequences) in your chosen dataset.
- [ ] Confirm the review's CoAnnotating DOI (10.18653/v1/2023.emnlp-main.92) resolves.

## Prompt 04: novelty and feasibility

**Search strings to run yourself** (Google Scholar, Semantic Scholar, ResearchRabbit):
- `active learning DNA sequence classification label efficiency foundation model`
- `human-in-the-loop genomic annotation simulated annotator noise confidence routing`
- `selective labelling OR "learning to defer" regulatory element classification`
- `uncertainty routing human review calibration genomic sequence model`
- `Genomic Benchmarks active learning`

**What I found:** one search returned only result titles, no abstracts. Titles included DNA foundation model benchmarks, DNABERT-2, BEND, and the Genomic Benchmarks paper. I saw nothing titled as a study of simulated human-AI labelling with routing, but this is a title-level check only, so it is **not** evidence of novelty.

| Close neighbours to inspect | Why | Status |
|---|---|---|
| Benchmarking DNA foundation models (PMC12663285) | Shows how DNA models are compared on genomic tasks | Title only; read before citing |
| BEND (arXiv 2311.12570) | DNA language-model benchmark | Title only |
| CoAnnotating | Same routing idea in NLP | VERIFIED abstract |
| Confidence-routing studies in other domains (seen earlier: arXiv 2507.00543, 2603.16002) | Routing is already studied elsewhere | Snippets only |

**Novelty verdict (INFERRED):** routing and active learning are established ideas. A defensible contribution is a controlled, reproducible comparison of the three labelling arms on genomic sequence classification with calibration and annotator-error sensitivity. Present it as a controlled comparison, not a new method.

**Feasibility:** data and weights are public (VERIFIED). Compute fits a 4090 (INFERRED, measure pilot). Risk: install problems, simulated humans.
**Go / no-go:** **GO**, conditional on the four checks above and an environment test.
**Fallbacks:** CNN instead of DNABERT-2; one dataset; two error rates.

## Prompt 05: research problem, questions, success rules

**Problem.** Reviews argue that AI assistance can cut human labelling effort in genomics, but controlled three-arm comparisons with an independent reference are missing (review Sec 6.7, 7). This study tests a simulated version on a public genomic benchmark.

| | RQ1 | RQ2 | RQ3 |
|---|---|---|---|
| Question | At equal human-review budget, does confidence-based routing give higher final-label accuracy than random routing? | How do manual, AI-only and AI-assisted labelling compare in final-label accuracy per unit of human effort, across simulated annotator error rates? | Is model confidence calibrated, and does calibration relate to routing benefit? |
| Input | Pool of sequences, seed labels, trained model | Same | Model probabilities on pool |
| Comparator | Random routing | Manual, AI-only | Reliability diagram, ECE |
| Independent variables | Routing policy; review budget B | Arm; annotator error e; reliance a | Dataset; seed size S |
| Dependent variables | Final pool accuracy vs gold | Final accuracy; effort fraction | ECE; accuracy gain over random |
| Decision rule (set now) | Supported if mean gain at matched budget is at least 1 percentage point with a 95% bootstrap interval over seeds excluding 0 | Descriptive; AI-assisted "wins" at an effort level only if it exceeds both others there by the same rule | Descriptive; report correlation, no causal claim |
| What would contradict me | Gain under 1 point or interval includes 0 | AI-assisted not above AI-only when e is high | ECE high yet routing still helps (or reverse) |

**Intended vs demonstrated.** Intended: the simulated comparison above. Not demonstrated: any claim about real annotators or metadata/ontology annotation.
**Overbroad risks flagged:** "improve labelling" (too vague, removed); any claim about human behaviour (out of scope).
**Success threshold for the project:** baseline validated, all arms run under identical conditions with at least 3 seeds, results reproducible from one command.

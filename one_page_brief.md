# One-page research brief (Gate G1)

Student: Pratik Satpathy, RSI2025512 | 2026-11-16 | DRAFT, pending your verification checklist

| Field | Entry |
|---|---|
| Review topic and key papers | AI-assisted vs manual labelling of genomic data. Re-verify at source: Li et al. 2023 CoAnnotating [14]; Sheng et al. 2008 [26]; Buçinca et al. 2021 [3]; Northcutt et al. 2021 [20]; Ren et al. 2021 / Cacciarelli & Kulahci 2024 [2],[1]. New sources to verify and add: Grešová et al. 2023 (Genomic Benchmarks); Zhou et al. 2023/24 (DNABERT-2) |
| Research gap | Review Sec 6.7 and 7: no controlled three-arm genomic comparison; accuracy and effort rarely reported together; uncertainty routing under-evaluated. Original authors' statements UNKNOWN; novelty not claimed |
| Research question | Primary: at equal total human labels, does confidence-based routing beat random routing for AI-assisted labelling of genomic sequences? Sub-questions: arms vs effort across annotator error (RQ2); calibration (RQ3) |
| Study pathway | B, controlled comparison, after baseline validation |
| Dataset or measurement setup | Genomic Benchmarks: human_nontata_promoters (36,131 seqs) and human_enhancers_cohn (27,791 seqs). Official train/test; pool = train; gold labels used only for scoring. Licence: data stated CC0 in the paper; repo licence UNKNOWN |
| Baseline / comparators | Baselines: package CNN, full-label DNABERT-2. Comparators: AI-only, random routing, "more training labels" with the same budget. Controls: majority class, shuffled labels |
| Primary metric and control | Final pool-label accuracy vs gold at equal human labels (higher better). Held constant: split, seeds, model, hyperparameters |
| Computing and risks | RTX 4090 24 GB, under 4-5 h training (INFERRED). Risks: install conflicts, duplicate-sequence leakage, simulated annotators, DNABERT-2 licence |
| First executable milestone | Environment test (Prompt 08, running on server); load both datasets; print class counts, train/test sizes and duplicate counts |

## Research problem
Reviews argue that AI assistance can lower human labelling effort in genomics, but controlled three-arm comparisons with an independent reference are missing. This study tests a simulated version on two public genomic benchmarks.

## Questions and decision rules (set before results)
| | RQ1 | RQ2 | RQ3 |
|---|---|---|---|
| Question | Does confidence routing beat random routing at equal human labels? | How do manual, AI-only and AI-assisted labelling compare in accuracy per human label across annotator error rates? | Is model confidence calibrated, and does calibration relate to routing benefit? |
| Comparator | Random routing; "more training labels" | Manual (all labelled by human), AI-only | Reliability diagram, ECE |
| Variables | Policy; budget B | Arm; error rate e; reliance a | Dataset; seed size S |
| Metric | Final pool accuracy | Final accuracy; labels per item | ECE; gain over random |
| Decision rule | Supported if mean gain is at least 1 percentage point and the 95% bootstrap interval (items and seeds) excludes 0 | Descriptive; an arm "wins" only by the same rule | Descriptive correlation; no causal claim |
| Contradicts me | Gain under 1 pp or interval includes 0 | AI-assisted not above AI-only when e is high | High ECE but routing helps anyway, or reverse |

Intended to investigate: the simulated comparison above. Not demonstrated: effects on real annotators, or ontology/metadata annotation (the review's main genomic tasks). Over-broad wording removed: "improve labelling".

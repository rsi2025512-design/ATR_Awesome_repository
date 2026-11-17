# Novelty and feasibility matrix (Prompt 04)

Date: 2026-11-16. Based on a limited web search (about 12 queries). **Absence of a paper in my search is not evidence that none exists.** No novelty is claimed.

## 1. Search strings to run yourself
Run each in Google Scholar and Semantic Scholar, then in ResearchRabbit, and record what you find.
- `"confidence" "human review" LLM annotation ontology mapping biomedical metadata`
- `LLM annotation GEO metadata ontology curation human-in-the-loop routing`
- `selective prediction OR "learning to defer" biomedical annotation LLM`
- `LLM uncertainty entropy prompt variants annotation allocation human`
- `Gemma curation LLM mouse strain cell line annotation`
- `expected calibration error LLM labelling genomic metadata`
- `reference label errors LLM disagreement curator adjudication transcriptomics`

**Neighbouring work to inspect:** human-LLM allocation methods; calibration of verbalised LLM confidence; ontology-mapping benchmarks; LLM curation in genomics repositories (GEO, Gemma and similar); label-noise detection.

## 2. Matrix

| Published work | What I VERIFIED it contributes | Source seen | Limitation | Proposed difference | Evidence still missing |
|---|---|---|---|---|---|
| CoAnnotating (Li et al. 2023) | Entropy-guided allocation of items between humans and an LLM; up to 21% better than random allocation | arXiv abstract, project page, GitHub README | NLP tasks, not genomics | Apply the same policy to a genomic ontology-annotation task | Read results tables; which datasets |
| Rogic et al. 2026 | GPT-4o annotates mouse strains (77%) and cell lines (59%) against Gemma; over 200 reference errors found | PubMed abstract, bioRxiv text | No routing or confidence analysis seen in the abstract | Add routing policies and calibration on the same task | Read full text: does it discuss confidence or human review? |
| Hou & Ji 2024 | GPT-4 cell-type annotation with strong agreement with manual annotation; R package | Duke record, press coverage | Single-arm LLM vs manual agreement | Not the planned task | Dataset access |
| arXiv 2507.00543, "Reliable Annotations with Less Effort: Evaluating LLM-Human..." (title cut off in search) | Reports 24-45% less human effort using confidence thresholds across tasks | Search snippet only | Domain unknown | Closest neighbour to my routing question: must be read before claiming any difference | Open the paper; authors, domain, datasets |
| RadAnnotate (arXiv 2603.16002) | Confidence-based automation in radiology report annotation, with calibration check | Search snippet | Radiology, not genomics | Domain differs | Confirm details |
| "Agreement Is Not Quality" (arXiv 2607.28890) | Confidence calibration differs by model | Search snippet | Qualitative coding | Domain differs | Confirm details |
| Frontiers neuroimaging metadata study (authors UNKNOWN from snippet) | LLM metadata annotation compared with human annotators, LLM at 95.6% vs humans 94.2% and 93.9% on one task | Search snippet | Neuroimaging | Domain differs | Open the paper |
| HILTS (Barbosa et al. 2026) | LLM pseudo-labelling with active learning and human review | ScienceDirect and author preprint pages | Not genomic | Not the planned task | None for now |

**Novelty verdict (INFERRED):** confidence-based routing between LLMs and humans is already studied in several domains, so the *method* is not novel. A defensible contribution is a controlled, reproducible evaluation of routing and calibration on a genomic ontology-annotation task, with the reference's own errors analysed. Say this in the paper; do not call it new.

## 3. Access checks

| Item | Status | Detail |
|---|---|---|
| Rogic code | Partly VERIFIED | GPT_annotate repo exists; README describes scripts and released tables; licence UNKNOWN |
| Gemma evaluation data | UNKNOWN | Paper says spreadsheets are provided; location, size and terms not seen |
| Released GPT-4o annotations and curator evaluations | Partly VERIFIED | README says these tables are included; their columns UNKNOWN |
| CoAnnotating code | Partly VERIFIED | Repo exists; licence UNKNOWN |
| Model access | UNKNOWN | GPT-4o used by Rogic via OpenAI API (paid); current availability and price not checked |
| Benchmark protocol | Partly VERIFIED | Accuracy against Gemma curation; exact matching rule UNKNOWN |

## 4. Compute and time (INFERRED)
- Hardware: no GPU needed; the work is API calls and light R/Python analysis on a laptop.
- Call count: items x prompt repeats. For example, 300 items x 5 prompt variants = 1,500 calls. Price UNKNOWN: run a 20-item pilot and extrapolate.
- Rough effort: environment and data check 1-2 days; baseline reproduction 3-4 days; routing experiment 3-4 days; deeper analysis 3 days; paper and repository 5 days. About 3 weeks in total. Adjust to your real deadline.

## 5. Narrowed question (draft for Prompt 05)
On a genomic ontology-annotation task (mouse strain from GEO metadata), at equal human-labelling budgets, does routing the least-confident LLM annotations to a human beat random routing, and how often is the reference label itself wrong where the model disagrees?

## 6. Go / no-go
**Conditional GO.** It becomes GO when these four checks pass: (1) the code and tables open and the licence permits reuse, (2) the Gemma evaluation data can be downloaded, (3) the released tables hold enough to recompute the published accuracy, (4) a 20-item API pilot costs an amount you can afford.

## 7. Fallbacks
1. **No API budget:** use only the released GPT-4o outputs and curator evaluations. Reproduce the accuracy figures, then do the reference-error analysis (G5). No new model calls.
2. **Gemma data unavailable:** switch to a task from Hou & Ji or Riquelme-García once their datasets are verified.
3. **Model withdrawn or too costly:** use a smaller hosted or local open model and report the change as a deviation from the original protocol.

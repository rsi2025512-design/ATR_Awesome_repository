# Literature-to-experiment map (Prompt 03)

Checked 2026-11-16 by web search of the pages named. "Opened" means I saw the page text in search results; I have NOT run any code or downloaded any data.
Labels: **VERIFIED** = seen at a primary or official page. **UNKNOWN** = not seen. **INFERRED** = my reasoning.
Assumed constraints (unconfirmed, please correct): MacBook Air, no GPU; no human annotators; weeks and API budget not stated.

## A. Three methods from the review that could be reproduced

| | M1: Rogic et al. (review ref [25]) | M2: CoAnnotating (ref [14]) | M3: Hou & Ji GPTCelltype (ref [9]) |
|---|---|---|---|
| Original paper | Database 2026, baag041; DOI 10.1093/database/baag041; PMID 42483875 (VERIFIED on PubMed) | EMNLP 2023; arXiv 2310.15638 (VERIFIED). Review's DOI 10.18653/v1/2023.emnlp-main.92 not yet resolved (UNKNOWN) | Nature Methods 21(8):1462-1465, 2024; DOI 10.1038/s41592-024-02235-4 (VERIFIED) |
| Task / algorithm | Zero-shot GPT-4o plus RAG: identify mouse strains and cell lines in GEO metadata, map to ontology terms (EFO, TGEMO, CLO) (VERIFIED, abstract and methods text) | Prompt an LLM several times, compute response entropy, give the least-uncertain items to the LLM, send the rest to humans (VERIFIED, repo README) | Query GPT-4 with marker genes to name cell types (VERIFIED in press coverage and abstract) |
| Dataset | Over 9,000 manually curated Gemma experiments, 5,000+ articles (VERIFIED). Authors say evaluation spreadsheets are provided; exact location and licence UNKNOWN | NLP text-classification datasets, not genomics (VERIFIED from abstract; names UNKNOWN) | Ten datasets, five species (VERIFIED). Which ones, and where to download: UNKNOWN |
| Code / model access | GitHub PavlidisLab/GPT_annotate exists, R scripts in `cell_lines` and `strains`, released tables of GPT-4o annotations and curator evaluations, needs `download.R` first (VERIFIED from README text). Licence UNKNOWN. Needs OpenAI API (GPT-4o, text-embedding-3-large) | GitHub SALT-NLP/CoAnnotating exists with `LLM_Inferencing.py`, `Expertise_Estimation.py`, `Work_Allocation.ipynb` (VERIFIED). Licence UNKNOWN. Original used ChatGPT API | Authors state an R package GPTCelltype exists (VERIFIED). Repository URL and licence not seen (UNKNOWN). Needs GPT-4 API |
| Metric | Accuracy of correctly annotated experiments: 77% mouse strain, 59% cell line; over 200 reference errors found (VERIFIED, abstract) | Annotation quality against a random-allocation baseline, cost-performance (Pareto) curves; up to 21% over random (VERIFIED, abstract) | Agreement with manual annotation (matched in over 75% of cell types in most studies, per press release; get the exact definition from the paper) |
| Known limitations | Retrieval failures can look like model failures; reference curation itself has errors (VERIFIED in review text; confirm in the paper) | NLP data, no genomics; relies on repeated API calls | Authors note GPT-4's training data is undisclosed so quality is hard to verify (VERIFIED, press coverage) |
| Compute | API calls plus embedding store; no GPU needed (INFERRED). Cost UNKNOWN until a 20-item pilot | API calls: items x number of prompt variants (INFERRED). Cost UNKNOWN | API calls only (INFERRED) |

**Considered but not chosen:** Riquelme-García et al. (ref [23], CSBJ 27:2155-2167, open access CC BY 4.0 per repository record): needs model fine-tuning, so cost and effort are higher; code and data access UNKNOWN. HILTS (ref [2]): exists (Barbosa et al., Information Systems 138, DOI 10.1016/j.is.2025.102660, VERIFIED), but it trains small classifiers on NLP/wildlife-advertisement data, so it does not fit a genomic labelling baseline.

## B. Three study designs compared

| | A. Reproduction + extension | B. Controlled comparison | C. Targeted modification |
|---|---|---|---|
| Smallest working baseline | Rerun Rogic's mouse-strain task on a small subset, or recompute the 77% from the released tables | Same items labelled by the LLM once, then four allocation policies scored on the same items | Rogic pipeline with ONE added component (e.g. a confidence output) |
| Testable question | Do I reproduce roughly 77% under my conditions? | At equal human-label budgets, does entropy-based or self-reported-confidence routing beat random routing and AI-only? | Does adding confidence change accuracy at equal cost? |
| Resource burden | Low to medium | Medium (repeated prompts) | Medium |
| Evidence needed | Documented gap vs the published number | Accuracy vs fraction-to-human curves, calibration, repeated runs | Baseline preserved, isolated change |
| Risk | Data or code not downloadable | Reference treated as the "human" (limitation) | Small effect, hard to interpret |

## C. Recommended minimum viable experiment (INFERRED, provisional)

1. **Validate the baseline first (pathway A-style, low cost):** from the released GPT_annotate tables, recompute the mouse-strain accuracy and compare with the published 77%. This is your baseline validation for Gate G2.
2. **Main study (pathway B):** on a stratified subset of mouse-strain experiments, compare AI-only, random routing and entropy-guided routing (CoAnnotating-style, repeated prompts), with the Gemma curation as the stand-in "human".
3. **Deeper analysis (one of):** adjudicate a sample of LLM-vs-reference disagreements yourself (gap G5), or vary prompt and temperature (gap G4).

Whether this fits depends on three facts I do not have: your API budget, your time, and what columns the released tables contain.

## D. What you must personally verify before coding
- [ ] Open the GPT_annotate repository: licence, last-commit date, what `download.R` fetches, and what columns the annotation tables contain (do they hold any confidence or repeated-run information?).
- [ ] Find where the Gemma evaluation spreadsheets are hosted and read the terms.
- [ ] Read Rogic et al. Methods: the exact accuracy definition, the prompt, and which model version was used.
- [ ] Open the CoAnnotating repository: licence, requirements, and whether it runs without the original paid API.
- [ ] Check that GPT-4o (or the model you use) is still available and price a 20-item pilot.
- [ ] Resolve CoAnnotating's DOI from the review (10.18653/v1/2023.emnlp-main.92).

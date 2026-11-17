# Gap matrix (Prompt 02)

Source: rsi2025512_Pratik.pdf (genomics review). "Sec" = section of that review.
Labels: **VERIFIED** = the review says it (I read the passage). Whether the ORIGINAL paper says it is **UNKNOWN** until you check. **INFERRED** = my reasoning, to be tested.
Assumed constraints (please correct): MacBook Air, no GPU; API or small local model; no human annotators; weeks not yet stated.
No novelty is claimed. Novelty needs the separate search in Prompt 04.

## Five candidate gaps

| ID | Gap (source in review) | What the review reports | Who said it | Experimental question | Evidence that would test it | Feasibility |
|---|---|---|---|---|---|---|
| G1 | No controlled three-arm genomic study (Sec 6.7, Sec 7 gap 1, Sec 8) | Studies compare AI vs a reference, or show an interface, but not manual vs AI-only vs AI-assisted on one dataset | The review's own synthesis (VERIFIED that it says so; novelty UNKNOWN) | Do AI-assisted labels beat manual and AI-only labels in accuracy and time on the same records? | Accuracy, macro-F1, kappa, median time per item across arms | **Low** without human annotators; only a simulated version is possible (INFERRED) |
| G2 | Uncertainty and routing are under-evaluated (Sec 7 gap 4, Sec 5.1, Sec 3.3) | CoAnnotating [14] uses uncertainty to split work; HILTS [2] uses LLM pseudo-labels plus active learning | Original papers [14], [2] (UNKNOWN until checked; [2] existence unconfirmed) | Is LLM confidence calibrated on genomic labels, and does routing the least-confident items to a "human" cut human labels at small accuracy loss versus random routing? | Calibration error; accuracy against fraction sent to human; comparison with random routing and AI-only | **High**: API or small model, a few thousand items |
| G3 | Accuracy, error severity and effort are not reported together (Sec 7 gap 2, Sec 2, Sec 8) | Exact match is not enough for ontology labels; parent/child errors are milder than unrelated ones | The review (VERIFIED); no cited original | Do exact-match accuracy and hierarchical/semantic similarity rank methods differently, and what does each cost per correct item? | Exact vs hierarchical scores, error-severity breakdown, cost per correct item | **Medium-high**; needs an ontology file (UNKNOWN which) |
| G4 | Model, prompt and retrieval dependence (Sec 6.3, Sec 6.2, Sec 7 gap 3) | Retrieval failures can look like model failures [25]; base and fine-tuned models differ by ontology [23] | Originals [25], [23] (UNKNOWN until checked) | How much does accuracy move across prompts, temperature, repeated runs and retrieval on/off on one fixed task? | Mean and spread over repeated runs; prompt and retrieval ablation table | **High**; cheap if responses are cached |
| G5 | Reference labels are imperfect (Sec 6.1, Sec 3.1, Sec 6.6) | Rogic et al. found reference-curation errors [25]; Confident Learning [20] finds label errors | Originals [25], [20] (UNKNOWN until checked) | Where the model disagrees with the reference, how often is the reference wrong, and can confident learning flag those items? | You adjudicate a sample of disagreements; precision of the flagging method | **Medium**: needs your adjudication time, single adjudicator is a limitation |

**Not testable here (INFERRED):** automation bias and expert judgement shift (Sec 6.4, Sec 7 gap 5), and downstream scientific usefulness (Sec 7 gap 6). Both need human participants or downstream pipelines. Record them as limitations or future work.

## Ranking of three (INFERRED, scored on significance / resources / feasibility)

| Rank | Gap | Why |
|---|---|---|
| 1 | **G2** routing and calibration | Matches the review's central trend ("which items go to humans", Sec 5.1); runs on a laptop; has clear comparators (AI-only, random routing) |
| 2 | **G4** sensitivity and reproducibility | Cheap, directly supports Sec 6.3, and works as the deeper analysis |
| 3 | **G5** reference-label noise | Addresses the review's strongest methodological point (Sec 6.1); needs your time for adjudication |

Note a tension: G2 treats the reference label as the "human". The review itself says references are not ground truth, so G5 or G4 should supply the deeper analysis, and the paper must state this limitation.

## Claims to verify against the original publications before use
1. CoAnnotating [14] allocates items between humans and an LLM using uncertainty.
2. HILTS [2] exists and combines LLM pseudo-labels with active learning (DOI 10.1016/j.is.2025.102660).
3. Rogic et al. [25]: 77% mouse-strain, 59% cell-line accuracy, over 9,000 experiments, over 200 reference errors.
4. Riquelme-García et al. [23]: results vary by ontology; fine-tuned models still need curation.
5. Hou & Ji [9]: "very high agreement" with manual cell-type annotation (get the actual numbers).
6. Desmond et al. [4]: 54 users, 21 labels, about 6% accuracy gain.
7. Lu & Cosgun [17] and Rister Portinari Maranca et al. [24] findings as paraphrased in Sec 3.2 and 3.4.

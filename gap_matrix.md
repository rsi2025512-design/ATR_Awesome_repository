# Gap matrix (Prompt 02)

Source review: `rsi2025512_Pratik.pdf` (genomics review). "Sec" = section of that review.
Labels: VERIFIED = the review says it (I read the passage). Whether the ORIGINAL paper says it is UNKNOWN until you check. INFERRED = my reasoning.
Constraints: one RTX 4090 (24 GB), training under 4-5 h in total, deadline Wed 2026-11-18 morning, simulated annotators.
No novelty is claimed here. Novelty needs the separate search in Prompt 04.

| ID | Gap (source in review) | Reported by | Experimental question | Evidence that would test it | Feasibility on this setup |
|---|---|---|---|---|---|
| G1 | No controlled three-arm study of manual vs AI-only vs AI-assisted on one genomic task (Sec 6.7, Sec 7 gap 1, Sec 8) | The review's own synthesis (VERIFIED that it says so) | How do the three arms compare in final-label accuracy per unit of human effort? | Accuracy vs human labels spent, same data and gold labels | Medium: only with simulated annotators (INFERRED) |
| G2 | Uncertainty and routing under-evaluated (Sec 7 gap 4, Sec 5.1, Sec 3.3) | Review cites CoAnnotating [14] and HILTS [2]; originals UNKNOWN until read | Does sending the model's least-confident items to a human beat random routing at equal budget? Is confidence calibrated? | Accuracy gain over random at matched budget; ECE | High |
| G3 | Accuracy and effort rarely reported together (Sec 7 gap 2, Sec 2, Sec 8) | Review (VERIFIED) | What is the accuracy-vs-effort frontier of each arm? | Accuracy against human labels per item | High |
| G4 | Results depend on model/setup details (Sec 6.3) | Review cites Rogic [25], Riquelme-García [23]; originals UNKNOWN | How much do results move across seeds and seed-set sizes? | Mean and spread over 5 seeds | High |
| G5 | Reference labels are imperfect (Sec 6.1, 6.6, Sec 3.1) | Review cites Rogic [25], Northcutt [20], Sheng [26]; originals UNKNOWN | How sensitive are the conclusions to annotator error rate? | Sensitivity over error rates 0, 5, 10% | High (as simulation) |

**Not testable here (INFERRED):** real automation bias and expert judgement shift (Sec 6.4, Sec 7 gap 5) and downstream scientific usefulness (Sec 7 gap 6). Both need human participants or downstream pipelines. Report as limitations / future work. The reliance parameter in the simulation is an assumption, not a measurement.

## Ranking of three (INFERRED)
| Rank | Gap | Why |
|---|---|---|
| 1 | G2 (+G3 as the accuracy-effort curves) | Matches the review's central trend (Sec 5.1); cheap; clear comparators |
| 2 | G1 (simulated) | Directly operationalises the review's three-arm design (Sec 8) |
| 3 | G5 | Addresses the review's strongest methodological point; supplies the deeper analysis |

## Claims to verify against original publications
1. CoAnnotating [14]: uncertainty-guided allocation; "up to 21% over random" (VERIFIED in abstract; read the tables).
2. HILTS [2] content (existence VERIFIED earlier at ScienceDirect/ACM listings).
3. Rogic et al. [25]: 77% / 59% / over 200 reference errors (VERIFIED in PubMed abstract).
4. Riquelme-García et al. [23] results by ontology.
5. Hou & Ji [9]: the review says "very high agreement"; get actual figures.
6. Desmond et al. [4]: 54 users, 21 labels, about 6% gain.
7. Sheng et al. [26] and Buçinca et al. [3] findings as paraphrased in Sec 3.1 and 3.4.

## Problems found in the review itself (INFERRED, fix before reusing)
- Ref [8] (Harrer et al.) appears in the list but I found no in-text citation.
- Intro cites [25] for GPT-4 cell-type work (that is Hou & Ji, [9]) and [9] for mouse-strain/cell-line work (that is Rogic, [25]); Gemma curation agent is cited as [15] instead of [21].
- Sec 7 gap numbering reads "First, Second, Second, Fourth".

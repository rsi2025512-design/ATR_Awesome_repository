# Research decisions log

| ID | Date | Decision | Reason | Source / evidence | Next action |
|---|---|---|---|---|---|
| D1 | 2026-11-16 | Restart Lab 02 from scratch in a new repository; base review = genomics review (rsi2025512_Pratik.pdf); hardware RTX 4090 24 GB; deadline Wed 2026-11-18 morning | User instruction; earlier plan wrongly assumed a MacBook | Conversation; course Instructions PDF | Run Prompt 01 |
| D2 | 2026-11-16 | Gaps G1-G5; top three G2(+G3), G1 simulated, G5 | Fit review Sec 5-8; feasible on 4090 | gap_matrix.md | Verify the 7 flagged claims |
| D3 | 2026-11-16 | Pathway B after baseline validation; methods DNABERT-2, package CNN, routing | Cheap and testable | literature_to_experiment_map.md | Complete verify checklist |
| D4 | 2026-11-16 | Conditional GO; fallback CNN as AI model | Access partly verified; licences UNKNOWN | novelty_feasibility_matrix.md | Run Prompt 08 on server |
| D5 | 2026-11-16 | RQ1-RQ3 and decision rule (1 pp, 95% bootstrap CI) set before results | Rules fixed in advance | one_page_brief.md | Review brief |
| D6 | 2026-11-16 | Datasets: human_nontata_promoters (primary), human_enhancers_cohn (secondary) | Sizes and published CNN baselines from paper table | dataset_baseline_validation_sheet.md | Load data; duplicate check |
| D7 | 2026-11-16 | Protocol drafted; freeze after Prompt 10 | Pre-registration before results | protocol.md; configs/frozen_protocol.yaml | Commit frozen config before main run |
| D8 | 2026-11-16 | Use the RTX 4090 (GPU 0) only; work in a fresh virtualenv, not the mixed user/system site-packages | Server has two GPUs; torch missing; NumPy 2 conflicts with system compiled modules | environment_log.md | Install torch in venv; run env_test, model_test, data_check |
| D9 | 2026-11-16 | Run DNABERT-2 with standard (non-flash) attention by removing triton from the `aitr` env; env pinned to transformers 4.x | Triton kernel in model repo incompatible with triton 3.1.0; transformers 5.x incompatible with torch 2.5.1 | environment_log.md | Re-run model_test; record final versions in protocol |
| D10 (APPROVED by the student 2026-11-17 13:31 IST) | 2026-11-17 | Make human_enhancers_cohn the primary dataset; keep human_nontata_promoters as a secondary, leakage-flagged dataset with stratified reporting | Promoters test: 45.6% of items share >80% of 16-mers with train, almost all negative; enhancers: 0.86% | E28, E31-E35 | Update frozen_protocol.yaml before freeze; report full official test and low-overlap subset |
| D11 | 2026-11-17 | Protocol v2 frozen by git commit 92e1e49 (configs/frozen_protocol.yaml, 13:31 IST, student's terminal output) | Required before the main run | configs/frozen_protocol.yaml | Run pilot, then main |
| D12 | 2026-11-17 | Exploratory routed_only arm not run; main grid stays at 317 records | Student declined extra ~60 runs; not part of frozen RQs | protocol.md | Explanation of the AI-assisted deficit labelled INFERRED in the paper |
| D13 | 2026-11-17 | Report least-confidence and margin as one policy in the paper | Identical for two classes (E58) | paper section 3 | None |
| D14 | 2026-11-17 | Report the decision rule outcome as 1 clear gain among 24 without multiplicity correction | Frozen rule had no correction; stated as a limitation | paper section 4.2 | None |

"""Generate every table and number used in paper.tex from the saved results (no hand-typed results).
  python paper/make_tables.py --results <results dir>   -> paper/generated/*.tex
Hard-coded inputs are limited to the leakage audit numbers, transcribed from the student's terminal output of
scripts/leakage_check.py, leakage_analysis.py and leakage_rootcause.py (2026-11-17); they are marked below.
"""
import argparse, glob, json
from pathlib import Path
import numpy as np
import pandas as pd

ap = argparse.ArgumentParser(); ap.add_argument("--results", required=True); a = ap.parse_args()
R = Path(a.results); AN = R / "analysis"; OUT = Path(__file__).resolve().parent / "generated"; OUT.mkdir(exist_ok=True)
pct = lambda x, d=1: f"{100 * x:.{d}f}"
M = {}                                              # macro name -> value
def mac(k, v): M[k] = v

base = pd.read_csv(AN / "baselines.csv")
def b(ds, model): return base[(base.dataset == ds) & (base.model == model)].iloc[0]
for ds, tag in [("human_nontata_promoters", "Prom"), ("human_enhancers_cohn", "Enh")]:
    for model, mt in [("DNABERT-2", "Dna"), ("package CNN", "Cnn")]:
        r = b(ds, model)
        mac(f"{mt}{tag}", pct(r.acc_mean)); mac(f"{mt}{tag}Sd", pct(r.acc_sd)); mac(f"{mt}{tag}F", pct(r.f1_mean)); mac(f"{mt}{tag}Ece", f"{r.ece_mean:.3f}")
mac("MajProm", pct(b("human_nontata_promoters", "DNABERT-2").majority)); mac("MajEnh", pct(b("human_enhancers_cohn", "DNABERT-2").majority))

# T1 baselines
rows = []
for ds, nm in [("human_nontata_promoters", "Promoters (non-TATA)"), ("human_enhancers_cohn", "Enhancers (Cohn)")]:
    for model in ["DNABERT-2", "package CNN"]:
        r = b(ds, model); rows.append(f"{nm} & {model} & {int(r.n_seeds)} & {pct(r.acc_mean)} $\\pm$ {pct(r.acc_sd)} & {pct(r.f1_mean)} & {r.ece_mean:.3f} & {pct(r.majority)} \\\\")
(OUT / "t_baselines.tex").write_text("\\begin{tabular}{llrcccc}\n\\toprule\nDataset & Model & Seeds & Accuracy (\\%) & Macro-F1 (\\%) & ECE & Majority (\\%) \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# T3 stratified accuracy on promoters: transcribed from leakage_analysis.py output (seeds 0-3), see header
strat = {  # bin: (n, positive share, [dna s0..s3], [cnn s0..s3])
    "$\\leq$5\\%": (2694, 0.995, [.751, .813, .831, .822], [.599, .568, .631, .584]),
    "5--50\\%":   (1995, 0.992, [.955, .965, .965, .961], [.924, .894, .927, .918]),
    "50--80\\%":  (225, 0.653, [.893, .898, .902, .889], [.844, .827, .836, .831]),
    "$>$80\\%":   (4120, 0.026, [.993, .989, .987, .987], [.953, .964, .942, .950])}
rows = [f"{k} & {v[0]:,} & {pct(v[1])} & {pct(np.mean(v[2]))} & {pct(np.mean(v[3]))} \\\\" for k, v in strat.items()]
(OUT / "t_strat.tex").write_text("\\begin{tabular}{lrrcc}\n\\toprule\nShared 16-mers with train & Test seqs & Positive (\\%) & DNABERT-2 acc (\\%) & CNN acc (\\%) \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")
mac("StratLowDna", pct(np.mean(strat['$\\leq$5\\%'][2]))); mac("StratLowCnn", pct(np.mean(strat['$\\leq$5\\%'][3])))
mac("StratHighDna", pct(np.mean(strat['$>$80\\%'][2]))); mac("StratHighCnn", pct(np.mean(strat['$>$80\\%'][3])))

# main cell accuracy
acc = pd.read_csv(AN / "main_cell_accuracy.csv")
def A(arm, pol, s, sp, col="test_accuracy_mean"): return acc[(acc.arm == arm) & (acc.policy == pol) & (acc.s == s) & (acc.sp == sp)].iloc[0][col]
def cell(arm, pol, s, sp):
    return f"{pct(A(arm, pol, s, sp))} $\\pm$ {pct(A(arm, pol, s, sp, 'test_accuracy_std'))}"
rows = []
rows.append("Manual (all labels human) & " + " & ".join(cell("manual", "-", n, n) for n in (100, 300, 1000, 3000)) + " \\\\")
rows.append("AI-only (human labels = seed set) & " + " & ".join([cell("ai_only", "-", 100, 100), cell("ai_only", "-", 300, 300), cell("ai_only", "-", 1000, 1000), "--"]) + " \\\\")
for pol, nm in [("random", "AI-assisted, random"), ("least_confidence", "AI-assisted, least-confidence"), ("margin", "AI-assisted, margin"), ("ensemble_disagreement", "AI-assisted, ensemble disagreement")]:
    rows.append(f"{nm} & -- & " + " & ".join(cell("ai_assisted", pol, s, sp) for s, sp in [(100, 300), (300, 1000), (1000, 3000)]) + " \\\\")
(OUT / "t_main_acc.tex").write_text("\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{4}{c}{Total human labels} \\\\\n\\cmidrule(lr){2-5}\n & 100 & 300 & 1000 & 3000 \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")
for n, w in [(100, "OneH"), (300, "ThreeH"), (1000, "OneK"), (3000, "ThreeK")]: mac(f"Man{w}", pct(A("manual", "-", n, n)))
for pol, t in [("random", "Rand"), ("least_confidence", "Lc"), ("ensemble_disagreement", "Ens")]:
    mac(f"Ai{t}Three", pct(A("ai_assisted", pol, 1000, 3000))); mac(f"Ece{t}Three", f"{A('ai_assisted', pol, 1000, 3000, 'test_ece_mean'):.3f}")
mac("EceManThree", f"{A('manual', '-', 3000, 3000, 'test_ece_mean'):.3f}"); mac("EceManOne", f"{A('manual', '-', 1000, 1000, 'test_ece_mean'):.3f}")
mac("EceAiOnlyOne", f"{A('ai_only', '-', 1000, 1000, 'test_ece_mean'):.3f}")

# ECE table
rows = ["Manual & " + " & ".join(f"{A('manual','-',n,n,'test_ece_mean'):.3f}" for n in (100, 300, 1000, 3000)) + " \\\\",
        "AI-only & " + " & ".join([f"{A('ai_only','-',s,s,'test_ece_mean'):.3f}" for s in (100, 300, 1000)] + ["--"]) + " \\\\"]
for pol, nm in [("random", "AI-assisted, random"), ("least_confidence", "AI-assisted, least-confidence"), ("ensemble_disagreement", "AI-assisted, ensemble disagreement")]:
    rows.append(f"{nm} & -- & " + " & ".join(f"{A('ai_assisted', pol, s, sp, 'test_ece_mean'):.3f}" for s, sp in [(100, 300), (300, 1000), (1000, 3000)]) + " \\\\")
(OUT / "t_ece.tex").write_text("\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{4}{c}{Total human labels} \\\\\n\\cmidrule(lr){2-5}\n & 100 & 300 & 1000 & 3000 \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")

# comparisons
c = pd.read_csv(AN / "main_comparisons.csv"); cf = c[c["subset"] == "full_test"]; cl = c[c["subset"] == "low_overlap"]
vc = cf.verdict.value_counts().to_dict(); vl = cl.verdict.value_counts().to_dict()
for k, n in [("Beats", "beats"), ("Worse", "worse"), ("NoClear", "no clear difference")]:
    mac(f"nFull{k}", str(vc.get(n, 0))); mac(f"nLow{k}", str(vl.get(n, 0)))
mac("nComp", str(len(cf)))
def C(name, s, sp):
    r = cf[(cf.comparison == name) & (cf.s == s) & (cf.sp == sp)].iloc[0]; return r
def put(tag, name, s, sp):
    r = C(name, s, sp); mac(f"{tag}Mean", f"{r.mean_pp:.1f}"); mac(f"{tag}Lo", f"{r.ci_low_pp:.1f}"); mac(f"{tag}Hi", f"{r.ci_high_pp:.1f}")
put("EnsVsRand", "ai_assisted:ensemble_disagreement vs random", 1000, 3000); put("LcVsRand", "ai_assisted:least_confidence vs random", 1000, 3000)
put("RandVsMan", "ai_assisted:random vs manual(3000)", 1000, 3000); put("LcVsMan", "ai_assisted:least_confidence vs manual(3000)", 1000, 3000)
put("EnsVsMan", "ai_assisted:ensemble_disagreement vs manual(3000)", 1000, 3000); put("OnlyVsMan", "ai_only(300) vs manual(300)", 300, 1000)
name_map = {"least_confidence": "least-conf.", "margin": "margin", "ensemble_disagreement": "ens. disagr.", "random": "random"}
def nice(r):
    cmp_ = r.comparison.replace("ai_assisted:", "")
    for k, v in name_map.items(): cmp_ = cmp_.replace(k, v)
    return cmp_.replace("ai_only", "AI-only").replace(" vs ", " vs. ").replace("manual", "manual")
rows = []
for s, sp in [(100, 300), (300, 1000), (1000, 3000)]:
    sub = cf[(cf.s == s) & (cf.sp == sp)]
    rows.append(f"\\multicolumn{{5}}{{l}}{{\\emph{{Budget pair {s}$\\to${sp}}}}} \\\\")
    for r in sub.itertuples():
        rows.append(f"{nice(r)} & {r.mean_pp:+.2f} & [{r.ci_low_pp:+.2f}, {r.ci_high_pp:+.2f}] & {r.verdict} \\\\".replace("  ", " ") .replace(" & ", " & ", 1))
rows = [r.replace("\\\\", "\\\\") for r in rows]
tab = "\\begin{tabular}{lccl}\n\\toprule\nComparison (accuracy, pp) & Mean & 95\\% CI & Verdict \\\\\n\\midrule\n"
tab += "\n".join(r.replace("\\multicolumn{5}", "\\multicolumn{4}") for r in rows) + "\n\\bottomrule\n\\end{tabular}\n"
(OUT / "t_comparisons.tex").write_text(tab)

# records-based numbers
recs = pd.DataFrame([json.loads(l) for f in glob.glob(str(R / "human_enhancers_cohn" / "main" / "records_*.jsonl")) for l in open(f)]).drop_duplicates("key")
mac("nRecords", str(len(recs))); mac("RunHours", f"{recs.seconds.sum() / 3600:.1f}")
mc = recs[(recs.e == 0.05) & (recs.a == 0.0)]
pv = mc[(mc.arm == "ai_assisted") & (mc.s == 1000)].pivot(index="seed", columns="policy", values="test_accuracy")
g = (pv.ensemble_disagreement - pv.random) * 100; g2 = (pv.least_confidence - pv.random) * 100
mac("EnsSeedMin", f"{g.min():.1f}"); mac("EnsSeedMax", f"{g.max():.1f}"); mac("EnsSeedPos", str(int((g > 0).sum())))
mac("LcSeedMin", f"{g2.min():.1f}"); mac("LcSeedMax", f"{g2.max():.1f}"); mac("LcSeedPos", str(int((g2 > 0).sum())))
pq = mc[(mc.arm == "ai_assisted") & (mc.policy == "random")].groupby("s")[["proposer_test_acc", "pseudo_label_acc"]].mean()
rows = [f"{s} & {pct(r.proposer_test_acc)} & {pct(r.pseudo_label_acc)} \\\\" for s, r in pq.iterrows()]
(OUT / "t_proposer.tex").write_text("\\begin{tabular}{rcc}\n\\toprule\nSeed labels $s$ & Proposer test accuracy (\\%) & Pseudo-label accuracy (\\%) \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")
for s, r in pq.iterrows():
    w = {100: "OneH", 300: "ThreeH", 1000: "OneK"}[s]; mac(f"ProposerAcc{w}", pct(r.proposer_test_acc)); mac(f"PseudoAcc{w}", pct(r.pseudo_label_acc))
rv = mc[(mc.arm == "ai_assisted") & (mc.s == 1000)].groupby("policy")[["proposer_acc_on_reviewed", "reviewed_label_acc"]].mean()
for pol, t in [("random", "Rand"), ("least_confidence", "Lc"), ("ensemble_disagreement", "Ens")]:
    mac(f"RevProp{t}", pct(rv.loc[pol, "proposer_acc_on_reviewed"])); mac(f"RevLab{t}", pct(rv.loc[pol, "reviewed_label_acc"]))

# sensitivity (seeds 0-2): ensemble-random and lc-random gains, pair 1000->3000
sens = recs[(recs.arm == "ai_assisted") & (recs.seed <= 2) & (recs.s == 1000)].groupby(["e", "a", "policy"]).test_accuracy.mean().unstack()
sens["ens"] = (sens.ensemble_disagreement - sens.random) * 100; sens["lc"] = (sens.least_confidence - sens.random) * 100
rows = [f"{e:.2f} & {a_:.1f} & {pct(r.random)} & {r.lc:+.2f} & {r.ens:+.2f} \\\\" for (e, a_), r in sens.iterrows()]
(OUT / "t_sens.tex").write_text("\\begin{tabular}{ccccc}\n\\toprule\nError $e$ & Reliance $a$ & Random acc (\\%) & Least-conf. gain (pp) & Ens. disagr. gain (pp) \\\\\n\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}\n")
mac("SensEnsMin", f"{sens.ens.min():.1f}"); mac("SensEnsMax", f"{sens.ens.max():.1f}"); mac("SensLcMin", f"{sens.lc.min():.1f}"); mac("SensLcMax", f"{sens.lc.max():.1f}")
mac("SensEnsAllPos", "all six" if (sens.ens > 0).all() else str(int((sens.ens > 0).sum())))
low = np.load(R / "human_enhancers_cohn" / "low_overlap_mask.npy"); mac("nLowOverlap", f"{int(low.sum()):,}"); mac("pctLowOverlap", pct(low.mean()))
names = {"Prom": "Prom"}
txt = "% generated by paper/make_tables.py; do not edit\n" + "\n".join(f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in M.items()) + "\n"
(OUT / "numbers.tex").write_text(txt)
print(len(M), "macros;", ", ".join(sorted(p.name for p in OUT.glob("*.tex"))))

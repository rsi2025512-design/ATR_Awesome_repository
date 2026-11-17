"""Downloads and inspects the two chosen Genomic Benchmarks datasets (Prompt 06 checklist).
    python scripts/data_check.py
Prints: directory layout, train/test sizes, class counts, length stats, exact duplicate counts within and across splits.
[TEST REQUIRED] not yet run. If the folder layout differs from the assumed
<root>/<dataset>/{train,test}/<class>/*.txt the script prints what it found instead of guessing.
"""
import os, sys
from pathlib import Path
from collections import Counter
from genomic_benchmarks.loc2seq import download_dataset
DATASETS = ["human_nontata_promoters", "human_enhancers_cohn"]
ROOT = Path.home() / ".genomic_benchmarks"
def read_split(d, split):
    seqs = []
    sd = d / split
    if not sd.is_dir():
        return None
    for cls_dir in sorted(p for p in sd.iterdir() if p.is_dir()):
        for f in cls_dir.glob("*.txt"):
            seqs.append((cls_dir.name, f.read_text().strip().upper()))
    return seqs
for name in DATASETS:
    print("=" * 70, "\n", name)
    try:
        download_dataset(name, version=0)
    except Exception as e:
        print("download_dataset failed:", repr(e)); continue
    d = ROOT / name
    print("path:", d, "| top level:", sorted(os.listdir(d)))
    tr, te = read_split(d, "train"), read_split(d, "test")
    if tr is None or te is None:
        print("Unexpected layout; inspect manually."); continue
    for tag, s in [("train", tr), ("test", te)]:
        lens = [len(x) for _, x in s]
        print(f"{tag}: n={len(s)} classes={dict(Counter(c for c, _ in s))} "
              f"len min/median/max={min(lens)}/{sorted(lens)[len(lens)//2]}/{max(lens)}")
        for c in sorted(set(c for c, _ in s)):
            l = [len(x) for cc, x in s if cc == c]
            print(f"   class {c}: mean length {sum(l)/len(l):.1f}")
    trs, tes = [x for _, x in tr], [x for _, x in te]
    print("exact duplicate sequences within train:", len(trs) - len(set(trs)))
    print("exact duplicate sequences within test :", len(tes) - len(set(tes)))
    print("train/test exact overlap (unique seqs):", len(set(trs) & set(tes)))
    both = {}
    for c, x in tr: both.setdefault(x, set()).add(c)
    print("train sequences appearing under >1 class:", sum(1 for v in both.values() if len(v) > 1))

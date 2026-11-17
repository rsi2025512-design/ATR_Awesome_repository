"""Module 1: data loading and validation for Genomic Benchmarks datasets.

Inputs : dataset name; folder layout ~/.genomic_benchmarks/<name>/{train,test}/<class>/*.txt
Outputs: (sequences: list[str], labels: np.ndarray[int64], shape (N,)); 0 = 'negative', 1 = 'positive'
Order  : classes sorted by name, files sorted by file name -> deterministic.
"""
from pathlib import Path
import numpy as np

ROOT = Path.home() / ".genomic_benchmarks"
CLASS_TO_ID = {"negative": 0, "positive": 1}

# Counts VERIFIED from the student's data_check.py output (2026-11-16): (train, test), per-class counts.
EXPECTED = {
    "human_nontata_promoters": {"train": {0: 12355, 1: 14742}, "test": {0: 4119, 1: 4915}, "length": 251},
    "human_enhancers_cohn":    {"train": {0: 10422, 1: 10421}, "test": {0: 3474, 1: 3474}, "length": 500},
}


def ensure_downloaded(name, root=ROOT):
    """Download via genomic_benchmarks if the folder is missing."""
    if not (Path(root) / name).is_dir():
        from genomic_benchmarks.loc2seq import download_dataset
        download_dataset(name, version=0)


def load_split(name, split, root=ROOT):
    """Return (seqs, labels) for split in {'train','test'}."""
    d = Path(root) / name / split
    if not d.is_dir():
        raise FileNotFoundError(f"{d} not found; call ensure_downloaded('{name}') first")
    seqs, labels = [], []
    for cls in sorted(p.name for p in d.iterdir() if p.is_dir()):
        if cls not in CLASS_TO_ID:
            raise ValueError(f"unexpected class folder '{cls}' in {d}")
        for f in sorted((d / cls).glob("*.txt")):
            seqs.append(f.read_text().strip().upper())
            labels.append(CLASS_TO_ID[cls])
    return seqs, np.asarray(labels, dtype=np.int64)


def validate(name, split, seqs, labels, expected=EXPECTED):
    """Raise AssertionError if counts, length or alphabet differ from what was verified."""
    exp = expected[name]
    assert len(seqs) == len(labels), "seqs/labels length mismatch"
    counts = {c: int((labels == c).sum()) for c in (0, 1)}
    assert counts == exp[split], f"{name}/{split}: class counts {counts} != expected {exp[split]}"
    lens = {len(s) for s in seqs}
    assert lens == {exp["length"]}, f"{name}/{split}: sequence lengths {sorted(lens)[:5]} != {exp['length']}"
    bad = [s for s in seqs if set(s) - set("ACGTN")]
    assert not bad, f"{name}/{split}: {len(bad)} sequences contain characters outside ACGTN"
    assert len(set(seqs)) == len(seqs), f"{name}/{split}: exact duplicate sequences present"
    return counts


def load_dataset(name, root=ROOT, check=True):
    """Return dict with 'train' and 'test' -> (seqs, labels); validated unless check=False."""
    ensure_downloaded(name, root)
    out = {}
    for split in ("train", "test"):
        seqs, labels = load_split(name, split, root)
        if check:
            validate(name, split, seqs, labels)
        out[split] = (seqs, labels)
    # train/test leakage check (exact only)
    overlap = set(out["train"][0]) & set(out["test"][0])
    assert not overlap, f"{name}: {len(overlap)} sequences appear in both train and test"
    return out

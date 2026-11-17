"""Near-duplicate / shared-region check between train and test (both strands).
For each test sequence: fraction of its 16-mers that also occur anywhere in train (forward or reverse complement).
  python scripts/leakage_check.py
Reports the distribution. High fractions mean test sequences overlap train regions (possible leakage).
Limitation: exact 16-mer sharing only; sequences with N are treated as A at that position.
[TEST REQUIRED] not yet run on the real data.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
K = 16
LUT = np.zeros(256, dtype=np.uint64)
for i, c in enumerate("ACGT"):
    LUT[ord(c)] = i


def to_arr(seqs):
    return LUT[np.frombuffer("".join(seqs).encode(), dtype=np.uint8)].reshape(len(seqs), -1)


def kmer_codes(arr, k=K, rc=False):
    n_pos = arr.shape[1] - k + 1
    codes = np.zeros((arr.shape[0], n_pos), dtype=np.uint64)
    for i in range(k):
        col = arr[:, i:i + n_pos]
        if rc:
            codes += (np.uint64(3) - col) << np.uint64(2 * i)
        else:
            codes += col << np.uint64(2 * (k - 1 - i))
    return codes


def shared_fraction(train_seqs, test_seqs, k=K):
    tr = to_arr(train_seqs)
    train_set = np.unique(np.concatenate([kmer_codes(tr, k).ravel(), kmer_codes(tr, k, rc=True).ravel()]))
    te = to_arr(test_seqs)
    f_fwd = np.isin(kmer_codes(te, k), train_set).mean(1)
    f_rc = np.isin(kmer_codes(te, k, rc=True), train_set).mean(1)
    return np.maximum(f_fwd, f_rc)


if __name__ == "__main__":
    from src.data import load_dataset, EXPECTED
    for name in EXPECTED:
        d = load_dataset(name)
        frac = shared_fraction(d["train"][0], d["test"][0])
        print(name, f"| test seqs {len(frac)}")
        for t in (0.05, 0.25, 0.5, 0.8, 0.95):
            print(f"  share >{int(t*100)}% of 16-mers with train: {int((frac > t).sum())} ({(frac > t).mean()*100:.2f}%)")
        print(f"  mean shared fraction {frac.mean():.4f}, max {frac.max():.4f}")

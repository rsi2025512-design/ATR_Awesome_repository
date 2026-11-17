"""Stratify test accuracy by train/test overlap (16-mer sharing, both strands).
  python scripts/leakage_analysis.py
For each dataset and overlap bin: n, share of test, neighbour-label agreement (label of the training sequences
sharing 16-mers vs the test label), and test accuracy of every saved run in results/<dataset>/*/test_predictions.npz.
[TEST REQUIRED] not yet run on the real data.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from leakage_check import to_arr, kmer_codes, K

BINS = [0.0, 0.05, 0.5, 0.8, 1.0001]
NAMES = ["<=5%", "5-50%", "50-80%", ">80%"]


def neighbour_info(train_seqs, train_labels, test_seqs, k=K):
    """Return per-test-seq: shared fraction, and mean label of the train sequences owning the shared 16-mers."""
    f, r = kmer_codes(to_arr(train_seqs), k), kmer_codes(to_arr(train_seqs), k, rc=True)
    n, n_pos = f.shape
    codes = np.concatenate([f.ravel(), r.ravel()])
    seq_id = np.concatenate([np.repeat(np.arange(n), n_pos)] * 2)
    uniq, first = np.unique(codes, return_index=True)
    uniq_label = np.asarray(train_labels)[seq_id[first]]     # label of one train seq containing each k-mer

    def stats(c):
        pos = np.minimum(np.searchsorted(uniq, c), len(uniq) - 1)
        hit = uniq[pos] == c
        nh = hit.sum(1)
        vote = np.where(nh > 0, np.where(hit, uniq_label[pos], 0).sum(1) / np.maximum(nh, 1), np.nan)
        return hit.mean(1), vote

    te = to_arr(test_seqs)
    ff, fv = stats(kmer_codes(te, k))
    rf, rv = stats(kmer_codes(te, k, rc=True))
    use_f = ff >= rf
    return np.where(use_f, ff, rf), np.where(use_f, fv, rv)


if __name__ == "__main__":
    from src.data import load_dataset, EXPECTED
    for name in EXPECTED:
        d = load_dataset(name)
        trs, trl = d["train"]; tes, tel = d["test"]
        frac, vote = neighbour_info(trs, trl, tes)
        b = np.digitize(frac, BINS) - 1
        runs = {}
        for f in sorted(Path("results", name).glob("*/test_predictions.npz")):
            z = np.load(f)
            assert (z["labels"] == tel).all(), f"label order mismatch in {f}"
            runs[f.parent.name] = (z["probs"].argmax(1) == tel)
        print("=" * 78, "\n", name, "| runs found:", list(runs))
        print(f"{'bin':8s}{'n':>7s}{'share':>8s}{'nbr-label agree':>17s}" + "".join(f"{r[:14]:>16s}" for r in runs))
        for i, nm in enumerate(NAMES):
            m = b == i
            if not m.any():
                continue
            agree = ((vote[m] > 0.5).astype(int) == tel[m]).mean() if (~np.isnan(vote[m])).any() else float("nan")
            print(f"{nm:8s}{int(m.sum()):7d}{m.mean():8.3f}{agree:17.3f}" + "".join(f"{runs[r][m].mean():16.3f}" for r in runs))
        print(f"{'ALL':8s}{len(tel):7d}{1.0:8.3f}{'':17s}" + "".join(f"{runs[r].mean():16.3f}" for r in runs))

"""Why do promoter negatives overlap train? Three diagnostics (CPU only, ~1 min):
  python scripts/leakage_rootcause.py [dataset]
A) redundancy INSIDE train, by class: fraction of each sequence's 16-mers also found in another train sequence
   (canonical k-mers, both strands) and fraction of distinct 16-mers per sequence (low value = repeats).
B) shifted-copy test: for test sequences sharing >80% with train, does one train sequence at one fixed shift
   explain >=90% of the shared 16-mers (forward strand only)? Histogram of |shift| by class.
Prints counts only; interpretation is done afterwards.
[TEST REQUIRED] not yet run on the real data.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from leakage_check import to_arr, kmer_codes, K
from leakage_analysis import neighbour_info


def within_train(train_seqs, k=K):
    a = to_arr(train_seqs)
    canon = np.minimum(kmer_codes(a, k), kmer_codes(a, k, rc=True))          # (n, n_pos)
    n, n_pos = canon.shape
    keys = np.unique((canon.astype(np.uint64) << np.uint64(20)) | np.arange(n, dtype=np.uint64)[:, None])
    codes, seqs = keys >> np.uint64(20), (keys & np.uint64((1 << 20) - 1)).astype(np.int64)
    _, inv, cnt = np.unique(codes, return_inverse=True, return_counts=True)
    shared = cnt[inv] >= 2
    per_seq_kmers = np.bincount(seqs, minlength=n)
    shared_frac = np.bincount(seqs, weights=shared, minlength=n) / per_seq_kmers
    return shared_frac, per_seq_kmers / n_pos


def shifted_copy(train_seqs, test_seqs, frac, k=K, sample=2000, seed=0):
    tr = to_arr(train_seqs); f = kmer_codes(tr, k); n, n_pos = f.shape
    uniq, first = np.unique(f.ravel(), return_index=True)
    tid, tpos = first // n_pos, first % n_pos
    tc = kmer_codes(to_arr(test_seqs), k)
    idx = np.where(frac > 0.8)[0]
    idx = np.random.RandomState(seed).choice(idx, min(sample, len(idx)), replace=False)
    out = {}
    for i in idx:
        pos = np.minimum(np.searchsorted(uniq, tc[i]), len(uniq) - 1)
        hit = uniq[pos] == tc[i]
        if hit.sum() == 0:
            continue
        off = np.arange(n_pos)[hit] - tpos[pos[hit]]
        key = tid[pos[hit]].astype(np.int64) * 100000 + (off + 50000)
        u, c = np.unique(key, return_counts=True)
        j = c.argmax()
        out[i] = (c[j] / hit.sum(), abs(int(u[j] % 100000) - 50000))
    return out


if __name__ == "__main__":
    from src.data import load_dataset
    name = sys.argv[1] if len(sys.argv) > 1 else "human_nontata_promoters"
    d = load_dataset(name); trs, trl = d["train"]; tes, tel = d["test"]
    sf, uf = within_train(trs)
    print(name, "\nA) inside train")
    for c, nm in [(0, "negative"), (1, "positive")]:
        m = trl == c
        print(f"  {nm}: n={int(m.sum())} mean shared-with-other-train {sf[m].mean():.3f} | "
              f">50% shared {(sf[m] > .5).mean():.3f} | >80% shared {(sf[m] > .8).mean():.3f} | "
              f"distinct 16-mer fraction mean {uf[m].mean():.3f}")
    frac, _ = neighbour_info(trs, trl, tes)
    res = shifted_copy(trs, tes, frac)
    print("B) shifted-copy test on test seqs sharing >80% with train (forward strand hits only)")
    for c, nm in [(0, "negative"), (1, "positive")]:
        r = [v for i, v in res.items() if tel[i] == c]
        if not r:
            print(f"  {nm}: none"); continue
        single = [s for s, o in r if s >= 0.9]
        offs = np.array([o for s, o in r if s >= 0.9])
        h = lambda lo, hi: int(((offs >= lo) & (offs <= hi)).sum())
        print(f"  {nm}: analysed {len(r)} | one train seq at one shift explains >=90%: {len(single)} ({len(single)/len(r):.2f}) | "
              f"|shift| 0: {h(0,0)}, 1-10: {h(1,10)}, 11-50: {h(11,50)}, >50: {h(51,10**6)}")

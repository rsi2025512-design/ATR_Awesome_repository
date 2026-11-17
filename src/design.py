"""Experiment design logic (numpy only, no torch): seeds, noise, routing, and training-set construction.
Implements protocol v2 (configs/frozen_protocol.yaml). All randomness is derived from the run seed, so a given
item has the same simulated human error / reliance draw in every arm (common random numbers, paired comparisons).
"""
import math
import numpy as np

SIZES = [100, 300, 1000, 3000]
PAIRS = [(100, 300), (300, 1000), (1000, 3000)]            # (s, s'); budget B = s' - s
POLICIES = ["random", "least_confidence", "margin", "ensemble_disagreement"]
E_VALUES = [0.0, 0.05, 0.10]
MAIN_E, MAIN_A = 0.05, 0.0
MAX_PSEUDO = 5000
BS, EPOCHS, MIN_STEPS = 32, 3, 150


def n_epochs(n, bs=BS, epochs=EPOCHS, min_steps=MIN_STEPS):
    return max(epochs, math.ceil(min_steps / math.ceil(n / bs)))


def perm_for(seed, n_pool):
    return np.random.RandomState(seed).permutation(n_pool)


def flips_for(seed, n_pool, e):
    return (np.random.RandomState(seed + 1000).rand(n_pool) < e).astype(np.int64)


def accept_ai_for(seed, n_pool, a):
    return np.random.RandomState(seed + 4000).rand(n_pool) < a


def route(policy, pool_probs, cand, B, seed, s, sp):
    """Pick B candidate pool indices for human review. pool_probs: (n_models, N, 2); model 0 is the proposer."""
    if B > len(cand):
        raise ValueError("budget larger than candidate set")
    if policy == "random":
        return np.random.RandomState(seed * 1000 + s * 7 + sp).choice(cand, B, replace=False)
    p0 = pool_probs[0][cand]
    if policy == "least_confidence":
        score = 1.0 - p0.max(1)
    elif policy == "margin":
        score = -np.abs(p0[:, 1] - p0[:, 0])
    elif policy == "ensemble_disagreement":
        score = pool_probs[:, cand, 1].std(0)
    else:
        raise ValueError(policy)
    return cand[np.argsort(-score, kind="stable")[:B]]


def build_manual(gold, flips, perm, n):
    idx = perm[:n]
    return idx, (gold ^ flips)[idx]


def build_ai_only(gold, flips, proposed, perm, s, max_pseudo=MAX_PSEUDO):
    S0, rest = perm[:s], perm[s:][:max_pseudo]
    idx = np.concatenate([S0, rest])
    lab = np.concatenate([(gold ^ flips)[S0], proposed[rest]])
    return idx, lab, {"n_human_labels": s, "pseudo_label_acc": float((proposed[rest] == gold[rest]).mean())}


def build_ai_assisted(gold, flips, accept_ai, proposed, pool_probs, perm, s, sp, policy, seed, max_pseudo=MAX_PSEUDO):
    n = len(gold); y_h = gold ^ flips
    S0, cand, B = perm[:s], perm[s:], sp - s
    rev = route(policy, pool_probs, cand, B, seed, s, sp)
    rev_labels = np.where(accept_ai[rev], proposed[rev], y_h[rev])
    is_rev = np.zeros(n, bool); is_rev[rev] = True
    rest = cand[~is_rev[cand]][:max_pseudo]
    idx = np.concatenate([S0, rev, rest])
    lab = np.concatenate([y_h[S0], rev_labels, proposed[rest]])
    diag = {"n_human_labels": s + B,
            "proposer_acc_on_reviewed": float((proposed[rev] == gold[rev]).mean()),
            "reviewed_label_acc": float((rev_labels == gold[rev]).mean()),
            "pseudo_label_acc": float((proposed[rest] == gold[rest]).mean())}
    return idx, lab, diag


def cells():
    """Yield (e, seed, a_values) exactly as in the protocol: main cell 5 seeds; all other cells seeds 0-2."""
    for e in E_VALUES:
        for seed in ([0, 1, 2, 3, 4] if e == MAIN_E else [0, 1, 2]):
            yield e, seed, ([0.0, 0.3] if seed < 3 else [0.0])


def count_ai_assisted():
    return sum(len(PAIRS) * len(POLICIES) * len(a) for _, _, a in cells())

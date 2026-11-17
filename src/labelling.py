"""Main experiment, GPU part (protocol v2). Design logic lives in src/design.py (tested without GPU).
Per (e, seed): an ensemble of 5 DNABERT-2 models is trained on the s seed labels (cached); model 0 is the proposer.
Arms per budget pair (s, s'): manual(n) for n in {s, s'}, ai_only(s), ai_assisted(s, s', policy, a).
Every run: fine-tune a fresh DNABERT-2 on the constructed training set, evaluate on the official test set,
append one JSON line to records_<tag>.jsonl and save test predictions (uint8) for paired bootstrap analysis.
Resumable: finished keys are skipped. [TEST REQUIRED] not yet run.
"""
import copy, json, sys, time
from pathlib import Path
import numpy as np
import torch
from torch.utils.data import TensorDataset
from src import design as D
from src.data import load_dataset
from src.encode import get_tokenizer, encode
from src.train import DNAClassifier, train, predict, set_seed
from src.metrics import all_metrics


class Env:
    def __init__(self, dataset="human_enhancers_cohn", results="results"):
        self.dataset = dataset
        d = load_dataset(dataset)
        (trs, self.trl), (tes, self.tel) = d["train"], d["test"]
        tok = get_tokenizer()
        self.pool_pred, _ = encode(trs, self.trl, tok)               # whole pool, used for prediction
        self.pool_ids, self.pool_mask = self.pool_pred.tensors[0], self.pool_pred.tensors[1]
        self.test_ds, _ = encode(tes, self.tel, tok)
        self.base = DNAClassifier()                                  # stays on CPU; clones are trained
        self.root = Path(results) / dataset
        self.root.mkdir(parents=True, exist_ok=True)
        mf = self.root / "low_overlap_mask.npy"
        if mf.exists():
            self.low = np.load(mf)
        else:
            sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
            from leakage_analysis import neighbour_info
            frac, _ = neighbour_info(trs, self.trl, tes)
            self.low = frac <= 0.25                                  # test seqs sharing <=25% of 16-mers with train
            np.save(mf, self.low)
        print(f"pool {len(self.trl)} test {len(self.tel)} low-overlap test {int(self.low.sum())}")


def fit(env, idx, labels, seed):
    idx_t = torch.as_tensor(np.asarray(idx))
    ds = TensorDataset(env.pool_ids[idx_t], env.pool_mask[idx_t], torch.as_tensor(labels, dtype=torch.long))
    m = copy.deepcopy(env.base)
    set_seed(seed)
    m.head.reset_parameters()
    train(m, ds, epochs=D.n_epochs(len(idx)), lr=3e-5, batch_size=D.BS, seed=seed, log=lambda r: None)
    return m


def evaluate(env, m):
    probs = predict(m, env.test_ds)
    met = all_metrics(probs, env.tel)
    pred = probs.argmax(1)
    met["acc_low_overlap"] = float((pred == env.tel)[env.low].mean())
    return met, pred.astype(np.uint8)


def get_ensemble(env, seed, s, e, perm, flips):
    f = env.root / "cache" / f"ens_s{s}_e{e}_seed{seed}.npz"
    f.parent.mkdir(exist_ok=True)
    if not f.exists():
        idx = perm[:s]; lab = (env.trl ^ flips)[idx]
        probs, prop = [], None
        for j in range(5):
            m = fit(env, idx, lab, seed * 100 + j)
            probs.append(predict(m, env.pool_pred))
            if j == 0:
                met, _ = evaluate(env, m)
                prop = {"proposer_test_acc": met["accuracy"], "proposer_test_ece": met["ece"],
                        "proposer_pool_acc": float((probs[0].argmax(1) == env.trl).mean())}
            del m; torch.cuda.empty_cache()
        np.savez(f, pool_probs=np.stack(probs).astype(np.float32), prop=json.dumps(prop))
    z = np.load(f)
    return z["pool_probs"], json.loads(str(z["prop"]))


def run(env, out_name="main", tag="a", seeds=None, pilot=False):
    out = env.root / out_name
    (out / "preds").mkdir(parents=True, exist_ok=True)
    done = set()
    for f in out.glob("records*.jsonl"):
        done |= {json.loads(l)["key"] for l in open(f)}
    rec_file = out / f"records_{tag}.jsonl"
    N, gold = len(env.trl), env.trl
    t_start = time.time()

    def emit(arm, policy, s, sp, e, a, seed, idx, lab, diag, extra):
        key = f"{arm}|{policy}|s{s}|sp{sp}|e{e}|a{a}|seed{seed}"
        if key in done:
            return
        t0 = time.time()
        m = fit(env, idx, lab, seed)
        met, pred = evaluate(env, m)
        del m; torch.cuda.empty_cache()
        row = dict(key=key, arm=arm, policy=policy, s=s, sp=sp, e=e, a=a, seed=seed, n_train=int(len(idx)),
                   seconds=round(time.time() - t0, 1), **{f"test_{k}": v for k, v in met.items()}, **diag, **extra)
        np.save(out / "preds" / (key.replace("|", "_") + ".npy"), pred)
        with open(rec_file, "a") as fh:
            fh.write(json.dumps(row) + "\n")
        done.add(key)
        print(f"[{(time.time() - t_start) / 60:6.1f} min] {key}  acc {met['accuracy']:.4f}  {row['seconds']}s", flush=True)

    cell_list = [(D.MAIN_E, 0, [0.0])] if pilot else list(D.cells())
    pairs = [(300, 1000)] if pilot else D.PAIRS
    for e, seed, a_list in cell_list:
        if seeds is not None and seed not in seeds:
            continue
        perm, flips = D.perm_for(seed, N), D.flips_for(seed, N, e)
        for s, sp in pairs:
            pp, prop = get_ensemble(env, seed, s, e, perm, flips)
            proposed = pp[0].argmax(1)
            for n in (s, sp):
                idx, lab = D.build_manual(gold, flips, perm, n)
                emit("manual", "-", n, n, e, 0.0, seed, idx, lab, {}, {})
            idx, lab, dg = D.build_ai_only(gold, flips, proposed, perm, s)
            emit("ai_only", "-", s, s, e, 0.0, seed, idx, lab, dg, prop)
            for a in a_list:
                acc = D.accept_ai_for(seed, N, a)
                for pol in D.POLICIES:
                    idx, lab, dg = D.build_ai_assisted(gold, flips, acc, proposed, pp, perm, s, sp, pol, seed)
                    emit("ai_assisted", pol, s, sp, e, a, seed, idx, lab, dg, prop)
    print("finished", out_name, tag)

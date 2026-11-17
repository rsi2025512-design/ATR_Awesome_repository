"""Module 3c: baseline runner (real labels, or shuffled-label control).
Examples (from repo root, `aitr` env):
  pilot timing : python scripts/run_baseline.py --dataset human_nontata_promoters --max_train 3000 --epochs 1 --tag pilot
  full baseline: python scripts/run_baseline.py --dataset human_nontata_promoters --epochs 3
  control      : python scripts/run_baseline.py --dataset human_nontata_promoters --epochs 3 --shuffle_labels
Test data is used ONLY for the final metrics; 10% of the (sub)sampled training data is held out for monitoring.
Writes results/<dataset>/<tag>/{metrics.json, test_predictions.npz}.
[TEST REQUIRED] not yet run.
"""
import argparse, json, sys, time
from pathlib import Path
import numpy as np, torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import load_dataset
from src.encode import get_tokenizer, encode
from src.metrics import all_metrics, majority_baseline
from src.train import DNAClassifier, train, predict, set_seed

p = argparse.ArgumentParser()
p.add_argument("--dataset", required=True)
p.add_argument("--epochs", type=int, default=3)
p.add_argument("--lr", type=float, default=3e-5)
p.add_argument("--batch_size", type=int, default=32)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--max_train", type=int, default=None, help="subsample the training set (pilot)")
p.add_argument("--shuffle_labels", action="store_true", help="control: permute training labels")
p.add_argument("--tag", default=None)
a = p.parse_args()

tag = a.tag or f"{'shuffled' if a.shuffle_labels else 'real'}_e{a.epochs}_s{a.seed}"
out = Path("results") / a.dataset / tag
out.mkdir(parents=True, exist_ok=True)

data = load_dataset(a.dataset)
(trs, trl), (tes, tel) = data["train"], data["test"]
rng = np.random.RandomState(a.seed)
idx = rng.permutation(len(trs))
if a.max_train:
    idx = idx[: a.max_train]
n_val = max(1, int(0.1 * len(idx)))
val_idx, fit_idx = idx[:n_val], idx[n_val:]
fit_labels = trl[fit_idx].copy()
if a.shuffle_labels:
    fit_labels = np.random.RandomState(a.seed + 999).permutation(fit_labels)   # val/test labels stay real

tok = get_tokenizer()
fit_ds, _ = encode([trs[i] for i in fit_idx], fit_labels, tok)
val_ds, _ = encode([trs[i] for i in val_idx], trl[val_idx], tok)
te_ds, _ = encode(tes, tel, tok)
print(f"fit {len(fit_idx)}  val {len(val_idx)}  test {len(tes)}  shuffled={a.shuffle_labels}")

set_seed(a.seed)
model = DNAClassifier()
t0 = time.time()
hist = train(model, fit_ds, a.epochs, a.lr, a.batch_size, a.seed, val_ds=val_ds)
train_seconds = time.time() - t0
probs = predict(model, te_ds)
m = all_metrics(probs, tel)
maj_acc, maj_cls = majority_baseline(trl, tel)
res = {"args": vars(a), "n_fit": len(fit_idx), "n_val": len(val_idx), "n_test": len(tes),
       "history": hist, "train_seconds": round(train_seconds, 1), "test": m,
       "majority_class": maj_cls, "majority_test_accuracy": maj_acc,
       "torch": torch.__version__, "gpu": torch.cuda.get_device_name(0)}
(out / "metrics.json").write_text(json.dumps(res, indent=2))
np.savez(out / "test_predictions.npz", probs=probs, labels=tel)
print(json.dumps({k: res[k] for k in ["train_seconds", "test", "majority_test_accuracy"]}, indent=2))
print("saved to", out)

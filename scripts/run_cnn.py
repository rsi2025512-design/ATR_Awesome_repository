"""Package-CNN baseline runner, same data split and metrics as run_baseline.py.
  python scripts/run_cnn.py --dataset human_nontata_promoters --epochs 10 --seed 0
Writes results/<dataset>/<tag>/{metrics.json, test_predictions.npz}.
[TEST REQUIRED] not yet run.
"""
import argparse, json, sys, time
from pathlib import Path
import numpy as np, torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import load_dataset
from src.metrics import all_metrics, majority_baseline
from src.train import set_seed
from src.cnn import encode_chars, make_cnn_loader, build_cnn, predict_cnn

p = argparse.ArgumentParser()
p.add_argument("--dataset", required=True)
p.add_argument("--epochs", type=int, default=10)
p.add_argument("--batch_size", type=int, default=64)
p.add_argument("--embedding_dim", type=int, default=100)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--tag", default=None)
a = p.parse_args()

tag = a.tag or f"cnn_e{a.epochs}_s{a.seed}"
out = Path("results") / a.dataset / tag
out.mkdir(parents=True, exist_ok=True)

data = load_dataset(a.dataset)
(trs, trl), (tes, tel) = data["train"], data["test"]
idx = np.random.RandomState(a.seed).permutation(len(trs))      # same split rule as run_baseline.py
n_val = max(1, int(0.1 * len(idx)))
val_idx, fit_idx = idx[:n_val], idx[n_val:]
x_fit, x_val, x_te = encode_chars([trs[i] for i in fit_idx]), encode_chars([trs[i] for i in val_idx]), encode_chars(tes)
print(f"fit {len(fit_idx)}  val {len(val_idx)}  test {len(tes)}  input_len {x_fit.shape[1]}")

set_seed(a.seed)
model = build_cnn(x_fit.shape[1], "cuda", a.embedding_dim)
loader = make_cnn_loader(x_fit, trl[fit_idx], a.batch_size, True, a.seed)
t0 = time.time()
model.fit(loader, a.epochs)                                     # package's own training loop
train_seconds = time.time() - t0
val_m = all_metrics(predict_cnn(model, x_val), trl[val_idx])
probs = predict_cnn(model, x_te)
m = all_metrics(probs, tel)
maj_acc, maj_cls = majority_baseline(trl, tel)
res = {"args": vars(a), "n_fit": len(fit_idx), "n_val": len(val_idx), "n_test": len(tes),
       "train_seconds": round(train_seconds, 1), "val": val_m, "test": m,
       "majority_class": maj_cls, "majority_test_accuracy": maj_acc,
       "torch": torch.__version__, "gpu": torch.cuda.get_device_name(0)}
(out / "metrics.json").write_text(json.dumps(res, indent=2))
np.savez(out / "test_predictions.npz", probs=probs, labels=tel)
print(json.dumps({k: res[k] for k in ["train_seconds", "val", "test", "majority_test_accuracy"]}, indent=2))
print("saved to", out)

"""Module 3b: DNABERT-2 classifier, training loop, prediction.

Model : DNABERT-2-117M backbone -> masked mean pooling of last hidden state -> dropout -> Linear(768, 2).
        (Mean pooling is used instead of the backbone's pooler, whose weights were newly initialised on load.)
Train : AdamW, linear warmup/decay, bf16 autocast, grad clip 1.0, fixed epochs, NO selection on test data.
Hyperparameter defaults are INFERRED common values, NOT taken from the DNABERT-2 repo; change in the config.
"""
import random, time
import numpy as np
import torch
import torch.nn as nn
from transformers import AutoModel, get_linear_schedule_with_warmup
from src.encode import make_loader, MODEL_NAME
from src.metrics import accuracy


def set_seed(seed):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)


class DNAClassifier(nn.Module):
    def __init__(self, name=MODEL_NAME, n_classes=2, dropout=0.1):
        super().__init__()
        self.backbone = AutoModel.from_pretrained(name, trust_remote_code=True)
        self.drop = nn.Dropout(dropout)
        self.head = nn.Linear(self.backbone.config.hidden_size, n_classes)

    def forward(self, ids, mask):
        h = self.backbone(input_ids=ids, attention_mask=mask)[0]          # (B, L, 768)
        m = mask.unsqueeze(-1).to(h.dtype)
        pooled = (h * m).sum(1) / m.sum(1).clamp(min=1)                     # (B, 768)
        return self.head(self.drop(pooled))                                 # (B, 2)


@torch.no_grad()
def predict(model, dataset, batch_size=128, device="cuda"):
    """Return softmax probabilities, np.ndarray (N, 2), in dataset order."""
    model.eval()
    out = []
    for ids, mask, _ in make_loader(dataset, batch_size, shuffle=False):
        with torch.autocast("cuda", dtype=torch.bfloat16):
            logits = model(ids.to(device), mask.to(device))
        out.append(torch.softmax(logits.float(), -1).cpu().numpy())
    return np.concatenate(out)


def train(model, train_ds, epochs=3, lr=3e-5, batch_size=32, seed=0, device="cuda",
          val_ds=None, weight_decay=0.01, warmup=0.1, log=print):
    set_seed(seed)
    model.to(device)
    loader = make_loader(train_ds, batch_size, True, seed)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    total = epochs * len(loader)
    sched = get_linear_schedule_with_warmup(opt, int(warmup * total), total)
    history = []
    for ep in range(epochs):
        model.train(); t0 = time.time(); run, n = 0.0, 0
        for ids, mask, y in loader:
            ids, mask, y = ids.to(device), mask.to(device), y.to(device)
            with torch.autocast("cuda", dtype=torch.bfloat16):
                logits = model(ids, mask)
            loss = nn.functional.cross_entropy(logits.float(), y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step(); sched.step(); opt.zero_grad(set_to_none=True)
            run += loss.item() * len(y); n += len(y)
        rec = {"epoch": ep + 1, "train_loss": run / n, "seconds": round(time.time() - t0, 1)}
        if val_ds is not None:
            rec["val_acc"] = accuracy(predict(model, val_ds, device=device), val_ds.tensors[2].numpy())
        history.append(rec); log(rec)
    return history

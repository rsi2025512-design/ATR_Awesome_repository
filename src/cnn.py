"""Module 5: package CNN baseline (genomic_benchmarks.models.torch.CNN), used as shipped.

Inputs : DNA strings (fixed length), labels (N,) int
Encoding: A,C,G,T,N -> 0..4 (character level, no padding needed: all sequences have equal length)
Training: the package's own CNN.fit() (Adam, default lr). Package quirk kept on purpose: forward() applies a
          sigmoid and the loss (BCE-with-logits) is then applied to that output. Epochs, embedding_dim, batch size
          are NOT specified by the package source -> our values are INFERRED defaults.
Outputs: predict_cnn -> np.ndarray (N, 2) = [1-p, p] so the same metrics code works.
"""
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
from genomic_benchmarks.models.torch import CNN

VOCAB = {c: i for i, c in enumerate("ACGTN")}


def encode_chars(seqs):
    return torch.from_numpy(np.array([[VOCAB[c] for c in s] for s in seqs], dtype=np.int64))   # (N, L)


def make_cnn_loader(x, y, batch_size, shuffle, seed=0):
    ds = TensorDataset(x, torch.as_tensor(y, dtype=torch.float32).unsqueeze(1))                # y: (N, 1) float
    g = torch.Generator(); g.manual_seed(seed)
    return DataLoader(ds, batch_size=batch_size, shuffle=shuffle, generator=g)


def build_cnn(input_len, device="cuda", embedding_dim=100):
    return CNN(number_of_classes=2, vocab_size=len(VOCAB), embedding_dim=embedding_dim,
               input_len=input_len, device=device).to(device)


@torch.no_grad()
def predict_cnn(model, x, batch_size=512, device="cuda"):
    model.eval()
    p = np.concatenate([model(x[i:i + batch_size].to(device)).squeeze(1).float().cpu().numpy()
                        for i in range(0, len(x), batch_size)])
    return np.stack([1 - p, p], axis=1)

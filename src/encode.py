"""Module 2: tokenisation and batching for DNABERT-2.

Inputs : list[str] DNA sequences, np.ndarray[int64] labels (N,), a HF tokenizer
Outputs: TensorDataset of (input_ids [N,L] int64, attention_mask [N,L] int64, labels [N] int64)
         L = longest tokenised sequence in the set (<= max_length); shorter ones are padded.
Truncation is allowed only above max_length and is COUNTED and reported, never silent.
"""
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader

MODEL_NAME = "zhihan1996/DNABERT-2-117M"


def get_tokenizer(name=MODEL_NAME):
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(name, trust_remote_code=True)


def encode(seqs, labels, tokenizer, max_length=512):
    """Tokenise all sequences once. Returns (TensorDataset, info dict)."""
    enc = tokenizer(list(seqs), return_tensors="pt", padding=True,
                    truncation=True, max_length=max_length)
    ids, mask = enc["input_ids"].long(), enc["attention_mask"].long()
    # count truncation: sequences whose unpadded length hits max_length
    n_trunc = int((mask.sum(1) >= max_length).sum())
    lens = mask.sum(1)
    info = {"n": len(seqs), "padded_length": int(ids.shape[1]),
            "token_len_min": int(lens.min()), "token_len_mean": float(lens.float().mean()),
            "token_len_max": int(lens.max()), "n_at_max_length": n_trunc,
            "pad_token_id": tokenizer.pad_token_id}
    return TensorDataset(ids, mask, torch.as_tensor(labels, dtype=torch.long)), info


def make_loader(dataset, batch_size, shuffle, seed=0):
    """Deterministic loader: shuffling uses its own seeded generator."""
    g = torch.Generator()
    g.manual_seed(seed)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, generator=g)

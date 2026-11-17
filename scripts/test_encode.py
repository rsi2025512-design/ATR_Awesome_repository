"""Sanity test for Module 2. Run from the repo root in the `aitr` env (GPU not needed):
    %run scripts/test_encode.py
Expected: token-length stats for both datasets, batch shapes, round-trip match rate, 'MODULE 2 TEST OK'.
[TEST REQUIRED] not yet run on the real tokenizer.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import load_dataset, EXPECTED
from src.encode import get_tokenizer, encode, make_loader
tok = get_tokenizer()
for name in EXPECTED:
    seqs, labels = load_dataset(name)["train"]
    ds, info = encode(seqs, labels, tok)
    print(name, info)
    assert info["n_at_max_length"] == 0, "sequences hit max_length: truncation possible"
    ids, mask, y = next(iter(make_loader(ds, 32, shuffle=False)))
    print("  batch shapes:", tuple(ids.shape), tuple(mask.shape), tuple(y.shape), "| dtypes", ids.dtype, y.dtype)
    assert ids.shape == mask.shape and y.shape[0] == ids.shape[0]
    # determinism: two shuffled loaders with the same seed give the same first batch
    a = next(iter(make_loader(ds, 32, True, seed=1)))[2]; b = next(iter(make_loader(ds, 32, True, seed=1)))[2]
    assert (a == b).all(), "seeded shuffle not deterministic"
    # round trip on 200 sequences (decode, drop special tokens and spaces, compare to original)
    ok = 0
    for i in range(200):
        dec = tok.decode(ds[i][0][ds[i][1].bool()], skip_special_tokens=True).replace(" ", "")
        ok += dec == seqs[i]
    print(f"  decode round-trip match: {ok}/200")
print("MODULE 2 TEST OK")

"""Sanity test for Module 1 (run in the `aitr` kernel or terminal, from the repo root):
    python scripts/test_data.py
Expected: for both datasets prints sizes and 'OK', ends with 'MODULE 1 TEST OK'.
[TEST REQUIRED] not yet run on the real data.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import load_dataset, EXPECTED
for name in EXPECTED:
    d = load_dataset(name)
    (trs, trl), (tes, tel) = d["train"], d["test"]
    print(f"{name}: train {len(trs)} (pos {int(trl.sum())}), test {len(tes)} (pos {int(tel.sum())}), "
          f"seq len {len(trs[0])}, label dtype {trl.dtype}, first label {trl[0]}")
    assert trl.shape == (len(trs),) and tel.shape == (len(tes),)
    print("  OK")
print("MODULE 1 TEST OK")

"""Loads DNABERT-2 and runs one forward pass (Prompt 08, second test).
    CUDA_VISIBLE_DEVICES=0 python scripts/model_test.py
Expected output type: parameter count and an output tensor shape. On failure it prints the traceback.
[TEST REQUIRED] not yet run.
"""
import traceback, torch
from transformers import AutoTokenizer, AutoModel
NAME = "zhihan1996/DNABERT-2-117M"
try:
    tok = AutoTokenizer.from_pretrained(NAME, trust_remote_code=True)
    model = AutoModel.from_pretrained(NAME, trust_remote_code=True).to("cuda").eval()
    print("params (M):", round(sum(p.numel() for p in model.parameters())/1e6, 1))
    seq = "ACGTAGCATCGGATCTATCTATCGACACTTGGTTATCGATCTACGAGCATCTCGTTAGC"
    ids = tok(seq, return_tensors="pt")["input_ids"].to("cuda")
    with torch.no_grad():
        out = model(ids)
    h = out[0] if isinstance(out, (tuple, list)) else out.last_hidden_state
    print("input ids shape:", tuple(ids.shape), "| hidden state shape:", tuple(h.shape))
    print("MODEL TEST OK")
except Exception:
    traceback.print_exc()
    print("MODEL TEST FAILED: paste the full traceback above back to the AI (Prompt 11).")

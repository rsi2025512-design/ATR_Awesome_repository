"""Environment test (Prompt 08). Run inside the project venv:
    CUDA_VISIBLE_DEVICES=0 python scripts/env_test.py
Expected output type: versions, CUDA availability, GPU name and memory, a small GPU matmul result, bf16 support.
[TEST REQUIRED] not yet run.
"""
import sys, random, platform
import numpy as np
print("python", sys.version.split()[0], platform.platform())
print("numpy", np.__version__)
for name in ["pandas", "sklearn", "transformers", "genomic_benchmarks", "matplotlib"]:
    try:
        m = __import__(name)
        print(name, getattr(m, "__version__", "installed (no __version__)"))
    except Exception as e:
        print(name, "IMPORT FAILED:", repr(e))
try:
    import torch
except Exception as e:
    print("torch IMPORT FAILED:", repr(e)); sys.exit(1)
print("torch", torch.__version__, "| built for CUDA", torch.version.cuda)
print("cuda available:", torch.cuda.is_available(), "| visible devices:", torch.cuda.device_count())
if not torch.cuda.is_available():
    print("No CUDA device visible. See failure diagnostics in the README of prompts/08."); sys.exit(2)
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    print(f"device {i}: {p.name}, {p.total_memory/2**30:.1f} GiB")
random.seed(0); np.random.seed(0); torch.manual_seed(0); torch.cuda.manual_seed_all(0)
a = torch.randn(2048, 2048, device="cuda"); b = torch.randn(2048, 2048, device="cuda")
c = (a @ b).float().mean().item(); torch.cuda.synchronize()
print("gpu matmul ok, mean =", round(c, 4))
print("bf16 supported:", torch.cuda.is_bf16_supported())
print("peak memory MiB:", round(torch.cuda.max_memory_allocated()/2**20, 1))

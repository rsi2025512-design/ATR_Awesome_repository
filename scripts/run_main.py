"""Main experiment runner (protocol v2).
  pilot (one grid cell, for timing and sanity): python scripts/run_main.py --pilot
  main on GPU 0, seeds 0,1,3:  CUDA_VISIBLE_DEVICES=0 python scripts/run_main.py --seeds 0,1,3 --tag gpu0
  main on GPU 1, seeds 2,4  :  CUDA_VISIBLE_DEVICES=1 python scripts/run_main.py --seeds 2,4 --tag gpu1
Results: results/human_enhancers_cohn/<main|pilot_main>/records_<tag>.jsonl and preds/*.npy
Only run the main experiment after the protocol freeze commit.
"""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.labelling import Env, run

p = argparse.ArgumentParser()
p.add_argument("--dataset", default="human_enhancers_cohn")
p.add_argument("--pilot", action="store_true")
p.add_argument("--seeds", default=None, help="comma-separated subset, e.g. 0,1,3")
p.add_argument("--tag", default="a")
a = p.parse_args()
seeds = [int(x) for x in a.seeds.split(",")] if a.seeds else None
env = Env(a.dataset)
run(env, "pilot_main" if a.pilot else "main", a.tag, seeds, a.pilot)

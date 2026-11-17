"""Module 3a: metrics. probs: np.ndarray (N, C) float, labels: np.ndarray (N,) int."""
import numpy as np
from sklearn.metrics import f1_score


def accuracy(probs, labels):
    return float((probs.argmax(1) == labels).mean())


def macro_f1(probs, labels):
    return float(f1_score(labels, probs.argmax(1), average="macro"))


def ece(probs, labels, n_bins=15):
    """Expected calibration error on top-label confidence, equal-width bins (15 per the protocol)."""
    conf = probs.max(1)
    correct = (probs.argmax(1) == labels).astype(float)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    total = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (conf > lo) & (conf <= hi)
        if m.any():
            total += m.mean() * abs(correct[m].mean() - conf[m].mean())
    return float(total)


def majority_baseline(train_labels, test_labels):
    """Always predict the training majority class; returns test accuracy."""
    maj = int(np.bincount(train_labels).argmax())
    return float((test_labels == maj).mean()), maj


def all_metrics(probs, labels, n_bins=15):
    return {"accuracy": accuracy(probs, labels), "macro_f1": macro_f1(probs, labels), "ece": ece(probs, labels, n_bins)}

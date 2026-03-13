import numpy as np


def detect_drift(old_scores, new_scores):

    diff = abs(np.mean(old_scores) - np.mean(new_scores))

    if diff > 0.3:
        return "Drift Detected"

    return "Model Stable"
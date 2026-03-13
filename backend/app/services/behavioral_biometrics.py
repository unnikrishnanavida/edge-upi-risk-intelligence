import numpy as np


def behavior_score(velocity, device_score):

    score = np.mean([velocity, device_score])

    if score > 0.8:
        return "High Risk"

    if score > 0.5:
        return "Medium Risk"

    return "Normal"
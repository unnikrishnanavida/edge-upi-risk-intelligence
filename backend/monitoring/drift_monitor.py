risk_scores = []


def monitor_drift(score):

    risk_scores.append(score)

    if len(risk_scores) > 200:

        avg = sum(risk_scores) / len(risk_scores)

        if avg > 0.5:

            print("⚠ Model drift detected")
import random

# --------------------------------------------------
# Dummy ML Model (for demo purposes)
# --------------------------------------------------

def predict_ml(tx):

    amount = tx.get("amount", 0)

    # Simple ML-like scoring logic
    if amount > 50000:
        score = 0.9
    elif amount > 10000:
        score = 0.6
    elif amount > 2000:
        score = 0.3
    else:
        score = 0.1

    # Add slight randomness to simulate ML behaviour
    score = score + random.uniform(-0.05, 0.05)

    # Clamp score
    score = max(0, min(1, score))

    return score
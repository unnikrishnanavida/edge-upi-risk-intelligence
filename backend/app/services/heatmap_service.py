from app.core.database import get_connection
from app.services.transaction_store import get_all_transactions


def generate_fraud_heatmap():

    df = get_all_transactions()

    if len(df) < 2:
        return {
            "error": "Not enough transactions for heatmap"
        }

    return {
        "amount": df["amount"].tolist(),
        "risk": df["risk"].tolist()
    }
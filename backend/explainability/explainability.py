import pandas as pd

def explain_transaction(tx_id):

    try:
        df = pd.read_csv("data/transactions.csv")

        transaction = df[df["transaction_id"] == tx_id]

        if transaction.empty:
            return {"error": "Transaction not found"}

        transaction = transaction.iloc[0]

        explanation = {
            "transaction_id": tx_id,
            "amount": transaction["amount"],
            "device_score": transaction["device_score"],
            "location_risk": transaction["location_risk"],
            "velocity": transaction["velocity"]
        }

        return explanation

    except Exception as e:
        return {"error": str(e)}
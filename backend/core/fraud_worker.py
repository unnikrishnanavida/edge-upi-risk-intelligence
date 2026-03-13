from backend.core.risk_engine import evaluate_risk

def analyze_transaction(tx):

    risk = evaluate_risk(tx)

    if risk == "HIGH":

        print("🚨 FRAUD ALERT")

        print(tx)
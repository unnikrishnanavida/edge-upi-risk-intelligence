from backend.core.risk_engine import evaluate_risk


class TransactionProcessor:

    def process_transaction(self, transaction):

        # Example feature extraction
        ml_score = transaction.get("ml_score", 0.4)

        behavior_score = transaction.get("behavior_score", 0.2)

        graph_score = transaction.get("graph_score", 0.2)

        velocity_score = transaction.get("velocity_score", 0.2)

        result = evaluate_risk(
            ml_score,
            behavior_score,
            graph_score,
            velocity_score
        )

        return {
            "transaction": transaction,
            "risk_score": result["risk_score"],
            "risk_level": result["risk_level"]
        }
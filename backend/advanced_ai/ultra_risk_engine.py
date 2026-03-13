class UltraRiskEngine:

    def compute(self, ml_score, rule_score, velocity_score):

        # -----------------------------
        # FIX: ML score may return dict
        # -----------------------------
        if isinstance(ml_score, dict):
            ml_score = ml_score.get("score", 0)

        if isinstance(rule_score, dict):
            rule_score = rule_score.get("score", 0)

        if isinstance(velocity_score, dict):
            velocity_score = velocity_score.get("score", 0)

        # -----------------------------
        # Risk Weights
        # -----------------------------
        weights = {
            "ml": 0.5,
            "rules": 0.3,
            "velocity": 0.2
        }

        # -----------------------------
        # Compute risk
        # -----------------------------
        risk_score = (
            weights["ml"] * ml_score +
            weights["rules"] * rule_score +
            weights["velocity"] * velocity_score
        )

        # -----------------------------
        # Clamp score between -1 and 1
        # -----------------------------
        risk_score = max(-1, min(1, risk_score))

        return risk_score


ultra_engine = UltraRiskEngine()
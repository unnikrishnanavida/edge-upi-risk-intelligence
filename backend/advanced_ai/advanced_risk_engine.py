class AdvancedRiskEngine:

    def compute_risk(self, ml_score, behavior_risk, graph_risk):

        risk = (
            0.5 * ml_score +
            0.3 * behavior_risk +
            0.2 * graph_risk
        )

        return min(risk, 1.0)
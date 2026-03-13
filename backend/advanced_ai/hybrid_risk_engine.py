import numpy as np


class HybridRiskEngine:

    def __init__(self):

        self.weights = {
            "ml": 0.4,
            "behaviour": 0.25,
            "graph": 0.2,
            "rule": 0.15
        }

    def compute(self, ml_score, behaviour_score, graph_score, rule_score):

        ml_component = ml_score * self.weights["ml"]
        behaviour_component = behaviour_score * self.weights["behaviour"]
        graph_component = graph_score * self.weights["graph"]
        rule_component = rule_score * self.weights["rule"]

        risk = ml_component + behaviour_component + graph_component + rule_component

        risk = float(np.clip(risk, -1, 1))

        return risk


engine = HybridRiskEngine()


def hybrid_risk(ml_score, behaviour_score, graph_score, rule_score):

    return engine.compute(
        ml_score,
        behaviour_score,
        graph_score,
        rule_score
    )
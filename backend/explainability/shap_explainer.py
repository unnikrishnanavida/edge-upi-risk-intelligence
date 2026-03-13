import shap
import numpy as np


class FraudExplainer:

    def __init__(self, model):

        self.model = model

        # Use KernelExplainer for sklearn models
        self.explainer = shap.KernelExplainer(
            model.predict_proba,
            np.zeros((1, model.n_features_in_))
        )


    def explain(self, X):

        shap_values = self.explainer.shap_values(X)

        return shap_values
import shap
import pandas as pd
import numpy as np

def generate_shap_values(model, features_df):
    explainer = shap.Explainer(model)
    shap_values = explainer(features_df)

    return {
        "base_value": float(shap_values.base_values[0]),
        "shap_values": {
            features_df.columns[i]: float(shap_values.values[0][i])
            for i in range(len(features_df.columns))
        }
    }
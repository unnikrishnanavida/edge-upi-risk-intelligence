import joblib
import numpy as np
import os

MODEL_PATH = "backend/models/isolation_forest.pkl"

training_buffer = []

RETRAIN_THRESHOLD = 200


def add_training_sample(features):

    training_buffer.append(features)

    if len(training_buffer) >= RETRAIN_THRESHOLD:
        retrain_model()


def retrain_model():

    if not os.path.exists(MODEL_PATH):
        return

    model = joblib.load(MODEL_PATH)

    X = np.array(training_buffer)

    try:
        model.fit(X)

        joblib.dump(model, MODEL_PATH)

        print("Model retrained with", len(X), "samples")

        training_buffer.clear()

    except Exception as e:
        print("Retraining failed:", e)
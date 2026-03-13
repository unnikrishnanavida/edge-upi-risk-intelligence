import numpy as np
from sklearn.ensemble import IsolationForest


class BehavioralBiometricsEngine:

    def __init__(self):

        self.model = IsolationForest(contamination=0.05)

        self.training_data = []

    def collect_behavior(self, behavior):

        features = [
            behavior["typing_speed"],
            behavior["touch_pressure"],
            behavior["session_time"],
            behavior["swipe_velocity"]
        ]

        self.training_data.append(features)

    def train(self):

        if len(self.training_data) > 10:
            self.model.fit(self.training_data)

    def detect_anomaly(self, behavior):

        features = np.array([[
            behavior["typing_speed"],
            behavior["touch_pressure"],
            behavior["session_time"],
            behavior["swipe_velocity"]
        ]])

        result = self.model.predict(features)

        if result[0] == -1:
            return True

        return False
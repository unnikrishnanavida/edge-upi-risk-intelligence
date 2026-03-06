from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:

    def __init__(self):
        self.model = IsolationForest(contamination=0.05)
        self.model.fit(np.random.rand(1000, 5))

    def detect(self, features):
        prediction = self.model.predict([features])
        return "ANOMALY" if prediction[0] == -1 else "NORMAL"
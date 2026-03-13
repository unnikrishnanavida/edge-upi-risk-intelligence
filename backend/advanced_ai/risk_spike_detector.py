import time


class RiskSpikeDetector:

    def __init__(self):

        self.history = []

    def add_score(self, score):

        now = time.time()

        self.history.append((now, score))

        self.history = [

            (t, s) for (t, s) in self.history

            if now - t < 300
        ]

    def detect_spike(self):

        if len(self.history) < 10:

            return False

        avg = sum(s for _, s in self.history) / len(self.history)

        if avg > 0.75:

            return True

        return False
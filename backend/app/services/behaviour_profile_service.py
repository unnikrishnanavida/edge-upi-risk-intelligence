from collections import defaultdict
import numpy as np

class BehaviourProfileEngine:

    def __init__(self):
        self.user_profiles = defaultdict(list)

    def update_profile(self, user_id, amount):

        self.user_profiles[user_id].append(amount)

        if len(self.user_profiles[user_id]) > 50:
            self.user_profiles[user_id].pop(0)

    def get_profile_stats(self, user_id):

        history = self.user_profiles[user_id]

        if len(history) < 5:
            return None

        return {
            "avg": np.mean(history),
            "std": np.std(history)
        }

    def deviation_score(self, user_id, amount):

        stats = self.get_profile_stats(user_id)

        if stats is None:
            return 0

        deviation = abs(amount - stats["avg"]) / (stats["std"] + 1)

        return deviation * 50
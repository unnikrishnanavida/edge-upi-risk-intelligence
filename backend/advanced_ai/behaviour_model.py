import numpy as np
from collections import defaultdict


class BehaviourRiskModel:

    def __init__(self):

        self.user_history = defaultdict(list)

    def update(self, user, amount):

        history = self.user_history[user]

        history.append(amount)

        if len(history) > 20:
            history.pop(0)

    def score(self, user, amount):

        history = self.user_history[user]

        if len(history) < 3:
            return 0

        avg = np.mean(history)

        std = np.std(history)

        if std == 0:
            std = 1

        z = (amount - avg) / std

        if z > 3:
            return 0.9
        elif z > 2:
            return 0.7
        elif z > 1:
            return 0.4
        else:
            return 0.1


model = BehaviourRiskModel()


def behaviour_risk(user, amount):

    model.update(user, amount)

    return model.score(user, amount)
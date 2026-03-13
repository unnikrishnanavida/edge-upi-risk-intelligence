import json
import os
import random

NETWORK_FILE = "data/fraud_network.json"


def record_transaction(user_id, amount):

    os.makedirs("data", exist_ok=True)

    receiver = random.randint(1, 20)

    edge = {
        "from": user_id,
        "to": receiver,
        "amount": amount
    }

    with open(NETWORK_FILE, "a") as f:
        f.write(json.dumps(edge) + "\n")


class FraudNetworkDetector:

    def __init__(self):
        self.file = NETWORK_FILE


    def load_transactions(self):

        if not os.path.exists(self.file):
            return []

        transactions = []

        with open(self.file, "r") as f:
            for line in f:
                try:
                    transactions.append(json.loads(line.strip()))
                except:
                    continue

        return transactions


    def check_network_risk(self, sender, receiver):

        txns = self.load_transactions()

        score = 0

        for t in txns:

            if t["from"] == sender or t["to"] == sender:
                score += 1

        if score > 10:
            return 0.9
        elif score > 5:
            return 0.5
        else:
            return 0.1
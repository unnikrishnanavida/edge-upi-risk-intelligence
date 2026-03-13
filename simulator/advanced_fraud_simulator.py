import random
import time


class AdvancedFraudSimulator:

    def generate_account_takeover(self):

        return {
            "sender": "victim_user",
            "receiver": "fraud_account",
            "amount": random.randint(30000, 80000),
            "timestamp": time.time(),
            "new_device": True,
            "location_change": True,
            "rapid_transactions": True
        }

    def generate_money_mule_chain(self):

        users = ["A", "B", "C", "D"]

        txs = []

        for i in range(len(users)-1):

            txs.append({
                "sender": users[i],
                "receiver": users[i+1],
                "amount": random.randint(10000, 30000),
                "timestamp": time.time()
            })

        return txs
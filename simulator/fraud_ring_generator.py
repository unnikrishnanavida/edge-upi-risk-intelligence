import random
import time


class FraudRingGenerator:

    def generate_ring(self, size=5):

        users = [f"user_{i}" for i in range(size)]

        transactions = []

        for i in range(size):

            sender = users[i]
            receiver = users[(i + 1) % size]

            tx = {

                "sender": sender,
                "receiver": receiver,
                "amount": random.randint(10000, 50000),
                "timestamp": time.time()

            }

            transactions.append(tx)

        return transactions
import numpy as np
import pandas as pd
import random
import uuid
from datetime import datetime, timedelta


class LargeScaleFraudSimulator:

    def __init__(self, users=50000):

        self.users = users
        self.user_ids = [f"user_{i}" for i in range(users)]

    def generate_transaction(self):

        sender = random.choice(self.user_ids)
        receiver = random.choice(self.user_ids)

        amount = np.random.exponential(200)

        timestamp = datetime.now() - timedelta(
            minutes=random.randint(0, 500000)
        )

        fraud_probability = np.random.rand()

        is_fraud = 1 if fraud_probability > 0.97 else 0

        return {
            "txn_id": str(uuid.uuid4()),
            "sender": sender,
            "receiver": receiver,
            "amount": float(amount),
            "timestamp": timestamp,
            "is_fraud": is_fraud
        }

    def generate_dataset(self, n_transactions=1000000):

        transactions = []

        for _ in range(n_transactions):
            transactions.append(self.generate_transaction())

        return pd.DataFrame(transactions)
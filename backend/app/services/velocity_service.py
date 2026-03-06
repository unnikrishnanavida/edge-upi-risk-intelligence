import time

user_transactions = {}

def check_velocity(user_id):

    now = time.time()

    if user_id not in user_transactions:
        user_transactions[user_id] = []

    user_transactions[user_id].append(now)

    user_transactions[user_id] = [
        t for t in user_transactions[user_id]
        if now - t <= 30
    ]

    txn_count = len(user_transactions[user_id])

    velocity_attack = txn_count > 5

    return {
        "velocity_attack": velocity_attack,
        "transactions_last_30s": txn_count
    }
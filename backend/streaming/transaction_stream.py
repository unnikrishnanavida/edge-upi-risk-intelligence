import time
import random

def generate_transactions():

    users = [1,2,3,4,5]

    while True:

        tx = {
            "user_id": random.choice(users),
            "amount": random.randint(100,20000)
        }

        yield tx

        time.sleep(1)
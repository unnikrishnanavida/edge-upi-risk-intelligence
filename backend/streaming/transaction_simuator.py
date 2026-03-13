import random
import time

users = ["U100", "U200", "U300", "U400"]
merchants = ["M10", "M20", "M30", "M40"]

def generate_transaction():

    return {
        "user_id": random.choice(users),
        "amount": random.randint(10, 20000),
        "device_id": "device_" + str(random.randint(1,5)),
        "location": random.choice(["Chennai","Delhi","Mumbai","Hyderabad"]),
        "merchant": random.choice(merchants)
    }


def simulate_stream(callback):

    while True:

        tx = generate_transaction()

        callback(tx)

        time.sleep(1)
import requests
import random
import time

API = "http://127.0.0.1:8000/predict"

users = ["user1", "user2", "user3", "user4", "user5"]

devices = ["phoneA", "phoneB", "phoneC"]

locations = ["mumbai", "delhi", "hyderabad", "vpn"]

merchants = ["amazon", "flipkart", "merchantX", "merchantY"]


def generate_transaction():

    return {
        "user_id": random.choice(users),
        "amount": random.randint(100, 20000),
        "device_id": random.choice(devices),
        "location": random.choice(locations),
        "merchant": random.choice(merchants)
    }


def simulate():

    print("Starting transaction simulator...\n")

    while True:

        tx = generate_transaction()

        try:

            response = requests.post(API, json=tx)

            print("Transaction:", tx)
            print("Response:", response.json())
            print("-" * 40)

        except Exception as e:

            print("Error:", e)

        time.sleep(2)


if __name__ == "__main__":
    simulate()
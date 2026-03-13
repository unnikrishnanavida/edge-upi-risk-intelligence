import requests
import random


URL = "http://localhost:8000/analyze"


def run_test(n=1000):

    for i in range(n):

        payload = {

            "amount": random.randint(10, 20000),
            "sender": "user_1",
            "receiver": "user_2"

        }

        r = requests.post(URL, json=payload)

        print(r.status_code)
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "upi_transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

def consume_transactions():

    for message in consumer:
        tx = message.value
        print("Streaming transaction:", tx)
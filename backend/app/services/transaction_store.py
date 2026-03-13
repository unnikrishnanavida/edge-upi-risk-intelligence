import pandas as pd
import os

DB_FILE = "transactions.csv"


def save_transaction(tx):

    df = pd.DataFrame([tx])

    if os.path.exists(DB_FILE):

        df_existing = pd.read_csv(DB_FILE)

        df = pd.concat([df_existing, df], ignore_index=True)

    df.to_csv(DB_FILE, index=False)


def get_all_transactions():

    if not os.path.exists(DB_FILE):
        return pd.DataFrame()

    return pd.read_csv(DB_FILE)


def get_transaction(tx_id):

    df = get_all_transactions()

    tx = df[df["transaction_id"] == tx_id]

    if len(tx) == 0:
        return None

    return tx.iloc[0].to_dict()
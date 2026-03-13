import pandas as pd


def temporal_patterns(df):

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["hour"] = df["timestamp"].dt.hour

    fraud_by_hour = df.groupby("hour")["risk"].sum()

    return fraud_by_hour.to_dict()
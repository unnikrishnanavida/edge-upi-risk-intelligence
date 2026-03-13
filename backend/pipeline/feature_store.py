import os
import pandas as pd


class FeatureStore:

    def __init__(self):

        self.path = "data/feature_store"

        os.makedirs(self.path, exist_ok=True)

    def save(self, df, name):

        file_path = f"{self.path}/{name}.parquet"

        df.to_parquet(file_path)

    def load(self, name):

        file_path = f"{self.path}/{name}.parquet"

        return pd.read_parquet(file_path)
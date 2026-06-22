import pandas as pd


class LogLoader:

    def __init__(self, filepath):
        self.filepath = filepath

    def load_logs(self, nrows=100000):

        df = pd.read_csv(
            self.filepath,
            nrows=nrows
        )

        print(f"Loaded {len(df)} security events")

        return df
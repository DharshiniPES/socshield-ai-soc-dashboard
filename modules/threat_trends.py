import pandas as pd


class ThreatTrends:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

        self.df["timestamp"] = pd.to_datetime(
            self.df["timestamp"]
        )



    def daily_threats(self):

        data = self.df[
            self.df["threat_label"] != "benign"
        ]

        return (
            data
            .groupby(
                data["timestamp"].dt.date
            )
            .size()
        )
    def monthly_threats(self):

        data = self.df[
            self.df["threat_label"] != "benign"
        ]

        return (
            data
            .groupby(
                data["timestamp"].dt.month
            )
            .size()
        )
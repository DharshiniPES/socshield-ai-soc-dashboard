from sklearn.ensemble import IsolationForest


class AnomalyDetection:

    def __init__(self, dataframe):
        self.df = dataframe

    def detect_anomalies(self):

        features = self.df[
            [
                "bytes_transferred"
            ]
        ]

        model = IsolationForest(
            contamination=0.02,
            random_state=42
        )

        predictions = model.fit_predict(
            features
        )

        self.df["anomaly"] = predictions

        anomalies = self.df[
            self.df["anomaly"] == -1
        ]

        return anomalies.head(20)
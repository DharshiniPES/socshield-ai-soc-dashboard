class AlertEngine:

    def __init__(self, dataframe):
        self.df = dataframe

    def generate_alerts(self):

        alerts = []

        malicious = self.df[
            self.df["threat_label"] == "malicious"
        ]

        for _, row in malicious.head(20).iterrows():

            alerts.append(
                f"🚨 HIGH RISK | {row['source_ip']} | {row['protocol']} | {row['action']}"
            )

        return alerts
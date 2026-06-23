class AlertEngine:

    def __init__(self, dataframe):
        self.df = dataframe

    def generate_alerts(self):

        alerts = []

        malicious = self.df[
            self.df["threat_label"] == "malicious"
        ]

        for _, row in malicious.head(20).iterrows():

            if row["threat_label"] == "malicious" and row["action"] == "allowed":
                severity = "CRITICAL"

            elif row["threat_label"] == "malicious":
                severity = "HIGH"

            elif row["threat_label"] == "suspicious":
                severity = "MEDIUM"

            else:
                severity = "LOW"

            alerts.append(
                {
                    "severity": severity,
                    "ip": row["source_ip"],
                    "protocol": row["protocol"],
                    "action": row["action"]
                }
            )

        return alerts
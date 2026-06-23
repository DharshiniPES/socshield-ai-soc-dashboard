class AlertEngine:

    def __init__(self, dataframe):
        self.df = dataframe

    def determine_severity(self, row):

        if (
            row["threat_label"] == "malicious"
            and row["action"] == "allowed"
        ):
            return "CRITICAL"

        elif row["threat_label"] == "malicious":
            return "HIGH"

        elif row["threat_label"] == "suspicious":
            return "MEDIUM"

        else:
            return "LOW"

    def generate_alerts(self):

        alerts = []

        for _, row in self.df.head(100).iterrows():

            severity = self.determine_severity(row)

            # Skip benign alerts
            if severity == "LOW":
                continue

            alerts.append(
                {
                    "severity": severity,
                    "ip": row["source_ip"],
                    "protocol": row["protocol"],
                    "action": row["action"]
                }
            )

        return alerts
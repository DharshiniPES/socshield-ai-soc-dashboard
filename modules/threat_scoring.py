class ThreatScoring:

    def __init__(self, dataframe):
        self.df = dataframe

    def calculate_ip_risk(self):

        malicious = self.df[
            self.df["threat_label"] == "malicious"
        ]

        counts = malicious["source_ip"].value_counts()

        max_count = counts.max()

        risk_scores = []

        for ip, count in counts.items():

            score = round(
                (count / max_count) * 100,
                2
            )

            risk_scores.append(
                (ip, score)
            )

        return sorted(
            risk_scores,
            key=lambda x: x[1],
            reverse=True
        )[:10]
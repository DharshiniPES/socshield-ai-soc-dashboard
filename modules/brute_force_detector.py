class BruteForceDetector:

    def __init__(self, dataframe):
        self.df = dataframe

    def detect_bruteforce(self):

        failed_attempts = self.df[
            self.df["action"] == "blocked"
        ]

        counts = (
            failed_attempts["source_ip"]
            .value_counts()
        )

        suspicious_ips = counts[
            counts > 50
        ]

        return suspicious_ips
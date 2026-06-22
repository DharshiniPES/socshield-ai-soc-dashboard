class Investigation:

    def __init__(self, dataframe):
        self.df = dataframe

    def investigate_ip(self, ip):

        results = self.df[
            self.df["source_ip"] == ip
        ]

        return results

    def get_protocols(self, ip):

        results = self.df[
            self.df["source_ip"] == ip
        ]

        return results["protocol"].value_counts()

    def get_destinations(self, ip):

        results = self.df[
            self.df["source_ip"] == ip
        ]

        return (
            results["dest_ip"]
            .value_counts()
            .head(5)
        )
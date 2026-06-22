class IPAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe

    def top_source_ips(self, top_n=10):

        return (
            self.df["source_ip"]
            .value_counts()
            .head(top_n)
        )

    def top_destination_ips(self, top_n=10):

        return (
            self.df["dest_ip"]
            .value_counts()
            .head(top_n)
        )
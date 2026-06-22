class Investigation:

    def __init__(self, dataframe):
        self.df = dataframe

    def investigate_ip(self, ip):

        return self.df[
            self.df["source_ip"] == ip
        ]

    def get_protocols(self, ip):

        records = self.investigate_ip(ip)

        return records["protocol"].value_counts()

    def get_destinations(self, ip):

        records = self.investigate_ip(ip)

        return (
            records["dest_ip"]
            .value_counts()
            .head(5)
        )
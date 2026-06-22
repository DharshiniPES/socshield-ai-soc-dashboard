class ProtocolAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe

    def protocol_distribution(self):

        return (
            self.df["protocol"]
            .value_counts()
        )
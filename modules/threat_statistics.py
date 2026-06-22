class ThreatStatistics:

    def __init__(self, dataframe):
        self.df = dataframe

    def threat_distribution(self):
        return self.df["threat_label"].value_counts()

    def protocol_distribution(self):
        return self.df["protocol"].value_counts()

    def action_distribution(self):
        return self.df["action"].value_counts()

    def log_type_distribution(self):
        return self.df["log_type"].value_counts()
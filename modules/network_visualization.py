import networkx as nx
import matplotlib.pyplot as plt


class NetworkVisualization:

    def __init__(self, dataframe):
        self.df = dataframe

    def draw_graph(self, limit=100):

        G = nx.Graph()

        sample = self.df[
            self.df["threat_label"] != "benign"
        ].head(50)

        for _, row in sample.iterrows():

            G.add_edge(
                row["source_ip"],
                row["dest_ip"]
            )

        fig, ax = plt.subplots(
            figsize=(10, 8)
        )

        pos = nx.spring_layout(
            G,
            seed=42
        )

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=500,
            font_size=7,
            ax=ax
        )

        return fig
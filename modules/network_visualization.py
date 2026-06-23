import networkx as nx
import matplotlib.pyplot as plt


class NetworkVisualization:

    def __init__(self, dataframe):
        self.df = dataframe

    def draw_graph(self, limit=50):

        G = nx.Graph()

        sample = self.df[
            self.df["threat_label"] != "benign"
        ].head(limit)

        node_colors = []

        for _, row in sample.iterrows():

            source = row["source_ip"]
            destination = row["dest_ip"]

            G.add_edge(
                source,
                destination
            )

        for node in G.nodes():

            malicious_match = sample[
                (
                    (sample["source_ip"] == node)
                    |
                    (sample["dest_ip"] == node)
                )
                &
                (
                    sample["threat_label"]
                    == "malicious"
                )
            ]

            if len(malicious_match) > 0:

                node_colors.append("red")

            else:

                node_colors.append("orange")

        fig, ax = plt.subplots(
            figsize=(12, 8)
        )

        pos = nx.spring_layout(
            G,
            seed=42,
            k=1.5
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            node_color=node_colors,
            node_size=700,
            ax=ax
        )

        nx.draw_networkx_edges(
            G,
            pos,
            alpha=0.6,
            ax=ax
        )

        nx.draw_networkx_labels(
            G,
            pos,
            font_size=7,
            ax=ax
        )

        ax.set_title(
            "SOCShield Attack Network"
        )

        ax.axis("off")

        return fig
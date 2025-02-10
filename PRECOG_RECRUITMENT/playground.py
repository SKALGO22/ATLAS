import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add 5 nodes (these will form the independent set)
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# Draw the graph
pos = nx.circular_layout(G, scale=0.001)  # Adjust the 'scale' parameter to bring nodes even closer
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=15, font_weight='bold')

# Show the plot
plt.title("Independent Set of Size 5")
plt.show()
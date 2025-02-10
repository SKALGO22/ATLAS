import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Load the list of countries
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]
full_countries.sort()

# Reduce each country's name to its first and last letter
countries = [f"{country[0]}{country[-1]}" for country in full_countries]
countries = list(set(countries))  # Remove duplicates

# Extract unique letters as nodes
letters = set(letter for country in countries for letter in country)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with special naming
for letter in letters:
    node_name = "A-clique" if letter == "a" else f"{letter.upper()}-set"
    G.add_node(node_name)

# Add edges if a country "AB" exists
for country in countries:
    if len(country) == 2:  
        source = "A-clique" if country[0] == "a" else f"{country[0].upper()}-set"
        target = "A-clique" if country[1] == "a" else f"{country[1].upper()}-set"
        G.add_edge(source, target)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Compute **Betweenness Centrality** for node size
betweenness_centrality = nx.betweenness_centrality(G)
node_sizes = [1000 + 40000 * betweenness_centrality[node] for node in G.nodes()]  # Scale up for better visibility

print(betweenness_centrality)

# Use a smooth color gradient (Inferno colormap)
color_map = cm.get_cmap('inferno', len(G.nodes()))
node_colors = [color_map(i) for i in np.linspace(0, 1, len(G.nodes()))]

# Adjust layout with more spread
plt.figure(figsize=(16, 16))
pos = nx.spring_layout(G, seed=42, k=1.4)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)

# Draw curved, soft-colored edges
nx.draw_networkx_edges(
    G, pos, edge_color="#AAAAAA", width=1.8, alpha=0.7, connectionstyle="arc3,rad=0.2"
)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")

# Add title
plt.title("Letter-Based Country Graph (Betweenness Centrality-Based)", fontsize=20, fontweight="bold")
plt.axis("off")
plt.show()

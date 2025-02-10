import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Load the list of countries
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries.txt", "r") as f:
    countries = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
countries.sort()

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on the last and first letters
for country in countries:
    G.add_node(country)
    last_letter = country[-1]  # Get the last letter
    for other_country in countries:
        if other_country[0] == last_letter and country != other_country:  # Avoid self-loops
            G.add_edge(country, other_country)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Compute centrality
centrality = nx.degree_centrality(G)

# Define thresholds for high, medium, and low centrality
high_threshold = 0.7 * max(centrality.values())
low_threshold = 0.3 * max(centrality.values())

# Assign colors to nodes based on centrality
node_colors = []
for node in G.nodes():
    if centrality[node] >= high_threshold:
        node_colors.append("#800000")  # Dark maroon for high centrality
    elif centrality[node] >= low_threshold:
        node_colors.append("#FF4500")  # Bright orange-red for medium centrality
    else:
        node_colors.append("#FFDAB9")  # Light peach for low centrality

# Assign colors to edges based on the darker node's color
edge_colors = []
for edge in G.edges():
    source, target = edge
    source_color = node_colors[list(G.nodes()).index(source)]
    target_color = node_colors[list(G.nodes()).index(target)]
    # Take the darker of the two colors
    if source_color == "#800000" or target_color == "#800000":
        edge_colors.append("#800000")
    elif source_color == "#FF4500" or target_color == "#FF4500":
        edge_colors.append("#FF4500")
    else:
        edge_colors.append("#FFDAB9")

# Use a force-directed layout
pos = nx.spring_layout(G, k=1.0, iterations=28, seed=42)  # Parameters control spacing and randomness
# Normalize positions to fit within a unit circle
max_radius = max(np.sqrt(x**2 + y**2) for x, y in pos.values())
pos_normalized = {node: (x / max_radius, y / max_radius) for node, (x, y) in pos.items()}

# Visualization parameters
plt.figure(figsize=(15, 15))  # Large figure for better spacing
nx.draw(
    G,
    pos_normalized,
    with_labels=True,
    labels={node: node for node in G.nodes()},
    node_color=node_colors,
    node_size=50,
    font_size=10,
    font_weight="bold",  # Bold node labels
    font_color="#000000",  # Black labels
    edge_color=edge_colors, 
    arrows=False,
    alpha=0.5,
    width=0.15,  # Adjust edge width for better visibility
    connectionstyle="arc3,rad=0.1"  # Slightly curved edges
)

# Add a title
plt.title("Country Atlas Graph - Force-Directed Layout with Centrality-Based Coloring", fontsize=16, fontweight="bold")
plt.axis("off")  # Turn off axes for a clean look
plt.show()


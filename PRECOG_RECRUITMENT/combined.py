import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Load the list of cities
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/cities.txt", "r") as f:
    cities = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries.txt", "r") as f:
    countries = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
combined = cities + countries
combined.sort()

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on the last and first letters
for area in combined:
    G.add_node(area)
    last_letter = area[-1]  # Get the last letter
    for other_area in combined:
        if other_area[0] == last_letter and area != other_area:  # Avoid self-loops
            G.add_edge(area, other_area)

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
        node_colors.append("#FFC107")  # Amber yellow for high centrality
    elif centrality[node] >= low_threshold:
        node_colors.append("#FFEB3B")  # Bright yellow for medium centrality
    else:
        node_colors.append("#FFD700")  # Golden yellow for low centrality

# Assign colors to edges based on the darker node's color
edge_colors = []
for edge in G.edges():
    source, target = edge
    source_color = node_colors[list(G.nodes()).index(source)]
    target_color = node_colors[list(G.nodes()).index(target)]
    # Take the darker of the two colors
    if source_color == "#FFC107" or target_color == "#FFC107":
        edge_colors.append("#FFC107")
    elif source_color == "#FFEB3B" or target_color == "#FFEB3B":
        edge_colors.append("#FFEB3B")
    else:
        edge_colors.append("#FFD700")

# Use a force-directed layout
pos = nx.spring_layout(G, k=1.3, iterations=50, seed=42)  # Parameters control spacing and randomness
# Normalize positions to fit within a unit circle
max_radius = max(np.sqrt(x**2 + y**2) for x, y in pos.values())
pos_normalized = {node: (x / max_radius, y / max_radius) for node, (x, y) in pos.items()}

# Visualization parameters
plt.figure(figsize=(25, 25))  # Large figure for better spacing
nx.draw(
    G,
    pos_normalized,
    with_labels=True,
    labels={node: node for node in G.nodes()},
    node_color=node_colors,
    node_size=45,
    font_size=8,
    font_weight="bold",  # Bold node labels
    font_color="#000000",  # Black labels
    edge_color=edge_colors, 
    arrows=False,
    alpha=0.5,
    width=0.1,  # Adjust edge width for better visibility
    connectionstyle="arc3,rad=0.1"  # Slightly curved edges
)

# Add a title
plt.title("Combined Atlas Graph - Force-Directed Layout with Centrality-Based Coloring", fontsize=16, fontweight="bold")
plt.axis("off")  # Turn off axes for a clean look
plt.show()

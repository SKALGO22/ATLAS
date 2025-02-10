'''import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

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
    if len(country) == 2:  # Ensure the country is a valid 2-letter representation
        source = "A-clique" if country[0] == "a" else f"{country[0].upper()}-set"
        target = "A-clique" if country[1] == "a" else f"{country[1].upper()}-set"
        G.add_edge(source, target)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Compute node size (proportional to out-degree)
in_degree = dict(G.in_degree())
node_sizes = [800 + 200 * in_degree.get(node, 1) for node in G.nodes()]  # Increased node size

# Generate a color gradient using matplotlib's colormap
from matplotlib import cm
color_map = cm.get_cmap('coolwarm', len(G.nodes()))
node_colors = [color_map(i) for i in np.linspace(0, 1, len(G.nodes()))]

# Adjust layout with more spread
plt.figure(figsize=(14, 14))
pos = nx.spring_layout(G, seed=100, k=1.2)  # Increased spread

# Draw the graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    font_size=12,
    font_weight="bold",
    font_color="black",
    edge_color="#555555",  # Darker gray for contrast
    width=2.5,  # Increased edge width
    alpha=0.9
)

# Add title
plt.title("Enhanced Letter-Based Country Graph", fontsize=18, fontweight="bold")
plt.show()
'''
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
    if len(country) == 2:  # Ensure the country is a valid 2-letter representation
        source = "A-clique" if country[0] == "a" else f"{country[0].upper()}-set"
        target = "A-clique" if country[1] == "a" else f"{country[1].upper()}-set"
        G.add_edge(source, target)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Compute node size (proportional to out-degree)
in_degree = dict(G.in_degree())
node_sizes = [1000 + 250 * in_degree.get(node, 1) for node in G.nodes()]  # Even larger nodes

# Generate a visually appealing gradient using 'plasma' colormap
color_map = cm.get_cmap('coolwarm', len(G.nodes()))
node_colors = [color_map(i) for i in np.linspace(0, 1, len(G.nodes()))]

# Adjust layout with more spread for readability
plt.figure(figsize=(16, 16))
pos = nx.spring_layout(G, seed=42, k=1.4)  # Increased spacing

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)

# Draw the edges with curvature & softer, lighter color
nx.draw_networkx_edges(
    G,
    pos,
    edge_color="#AAAAAA",  # Light gray edges for a softer feel
    width=1.8,
    alpha=0.7,
    connectionstyle="arc3,rad=0.2"  # Slightly curved edges for better aesthetics
)

# Draw labels with bold styling
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")

# Add title
plt.title("Letter-Based Country Graph", fontsize=20, fontweight="bold")
plt.axis("off")  # Hide axes for clean visualization
plt.show()

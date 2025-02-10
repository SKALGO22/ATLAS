import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# Exclusion set: do not consider countries starting or ending with these letters.
exclude = {'n', 'a', 'y', 'o', 'r', 'q'}

# Load the list of countries
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]
full_countries.sort()

# Filter the countries: only keep those whose first and last letters are NOT in the exclusion set.
filtered_countries = [country for country in full_countries 
                      if (country[0] not in exclude and country[-1] not in exclude)]

# Reduce each filtered country's name to its first and last letter (2-letter representation)
reduced_countries = [f"{country[0]}{country[-1]}" for country in filtered_countries]

# Remove duplicates (if desired; note: if different countries yield the same pair, we want to count them multiple times)
# For edge weight counting we want duplicates, so do not remove duplicates here.
# However, when creating nodes, we'll extract the unique letters from the reduced countries.
# (Edge weights will be computed by counting the frequency of each two-letter combination.)

# Extract unique letters from the reduced countries
letters = set(letter for country in reduced_countries for letter in country)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with special naming: for each letter, name it "X-set"
for letter in letters:
    node_name = f"{letter.upper()}-set"
    G.add_node(node_name)

# Add weighted edges: for each 2-letter country, add or increment the edge weight.
for country in reduced_countries:
    # Each country is 2 letters: first letter and last letter.
    source_letter = country[0]
    target_letter = country[1]
    source_node = f"{source_letter.upper()}-set"
    target_node = f"{target_letter.upper()}-set"
    if G.has_edge(source_node, target_node):
        G[source_node][target_node]['weight'] += 1
    else:
        G.add_edge(source_node, target_node, weight=1)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Compute, for each node, the difference: (total weight of incoming edges) - (total weight of outgoing edges)
node_diff = {}
for node in G.nodes():
    # Sum weights of incoming edges
    incoming_weight = sum(G[u][node]['weight'] for u in G.predecessors(node))
    # Sum weights of outgoing edges
    outgoing_weight = sum(G[node][v]['weight'] for v in G.successors(node))
    node_diff[node] = incoming_weight - outgoing_weight

# Sort the nodes in descending order by the computed difference
sorted_nodes = sorted(node_diff.items(), key=lambda x: x[1], reverse=True)
nodes_sorted, diff_values = zip(*sorted_nodes)

# Plot a bar graph
plt.figure(figsize=(14, 8))
bars = plt.bar(nodes_sorted, diff_values, color='mediumseagreen', edgecolor='black', alpha=0.8)
plt.xlabel("Nodes", fontsize=14)
plt.ylabel("Incoming Weight - Outgoing Weight", fontsize=14)
plt.title("Node Difference (Incoming - Outgoing) in Countries Graph (Excluding n, a, y, o, r, q)", fontsize=16, fontweight="bold")
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

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

# Find nodes with zero out-degree
zero_outdegree_nodes = [node for node in G.nodes() if G.out_degree(node) == 0]

# Print the nodes
print("Nodes with zero out-degree:")
for node in zero_outdegree_nodes:
    print(node)

# Print the total number of such nodes
print(f"\nTotal number of nodes with zero out-degree: {len(zero_outdegree_nodes)}")

# Find nodes with zero out-degree
zero_indegree_nodes = [node for node in G.nodes() if G.in_degree(node) == 0]

# Print the nodes
print("Nodes with zero in-degree:")
for node in zero_indegree_nodes:
    print(node)

# Print the total number of such nodes
print(f"\nTotal number of nodes with zero in-degree: {len(zero_indegree_nodes)}")

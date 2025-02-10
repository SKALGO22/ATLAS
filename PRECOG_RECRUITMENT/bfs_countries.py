'''import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Load the list of countries
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
full_countries.sort()

# Reduce each country's name to its first and last letter
countries = [f"{country[0]}{country[-1]}" for country in full_countries]
countries = list(set(countries))  # Remove duplicates

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

# Add a pseudo node 'a' with edges to 'an' and 'aa'
G.add_node('a')
G.add_edge('a', 'an')
G.add_edge('a', 'aa')

# Perform BFS and identify edges
bfs_tree_edges = set()  # Tree edges
backward_edges = set()  # Backward edges
non_tree_edges = set()  # Non-tree edges
layers = defaultdict(list)  # Nodes in each BFS layer

# BFS Traversal
visited = set()
queue = [('a', 0)]  # (node, layer)
visited.add('a')

while queue:
    node, layer = queue.pop(0)
    layers[layer].append(node)

    for neighbor in G.neighbors(node):
        if neighbor not in visited:  # Tree edge
            visited.add(neighbor)
            bfs_tree_edges.add((node, neighbor))
            queue.append((neighbor, layer + 1))
        elif (node, neighbor) not in bfs_tree_edges:  # Not a tree edge
            if neighbor in layers[layer]:  # Backward edge
                backward_edges.add((node, neighbor))
            else:  # Non-tree edge
                non_tree_edges.add((node, neighbor))

# Print nodes in each BFS layer
print("\nBFS Layers:")
for layer, nodes in sorted(layers.items()):
    print(f"Layer {layer}: {nodes}")

# Print edge classifications
print("\nTree Edges:")
print(bfs_tree_edges)

print("\nBackward Edges:")
print(backward_edges)

print("\nNon-Tree Edges:")
print(non_tree_edges)'''



# Working version of the code


import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Load the list of countries
with open("./countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
full_countries.sort()

# Reduce each country's name to its first and last letter
countries = [f"{country[0]}{country[-1]}" for country in full_countries]
countries = list(set(countries))  # Remove duplicates

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

# Add a pseudo node 'a' with edges to 'an' and 'aa'
G.add_node('a')
G.add_edge('a', 'an')
G.add_edge('a', 'aa')

# Perform BFS and identify edges
bfs_tree_edges = set()  # Tree edges
backward_edges = set()  # Backward edges
non_tree_edges = set()  # Non-tree edges
layers = defaultdict(list)  # Nodes in each BFS layer
backward_count = defaultdict(int)  # Count of back edges for each node

# BFS Traversal
visited = set()
queue = [('a', 0)]  # (node, layer)
visited.add('a')

while queue:
    node, layer = queue.pop(0)
    layers[layer].append(node)

    for neighbor in G.neighbors(node):
        if neighbor not in visited:  # Tree edge
            visited.add(neighbor)
            bfs_tree_edges.add((node, neighbor))
            queue.append((neighbor, layer + 1))
        elif (node, neighbor) not in bfs_tree_edges:  # Not a tree edge
            for i in range(layer-1, -1, -1):  # Check all previous layers
                if neighbor in layers[i]:  # Backward edge
                    backward_edges.add((node, neighbor))
                    backward_count[node] += 1  # Increment the back edge count for the source node
                else:  # Non-tree edge
                    non_tree_edges.add((node, neighbor))

# Print nodes in each BFS layer
print("\nBFS Layers:")
for layer, nodes in sorted(layers.items()):
    print(f"Layer {layer}: {nodes}")
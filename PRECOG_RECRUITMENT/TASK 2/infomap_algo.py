'''from infomap import Infomap
import networkx as nx 

# Load your graph (replace with your data)
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

# Initialize Infomap
im = Infomap(directed=True, silent=True)

# Add nodes and edges
for node in G.nodes():
    im.add_node(int(node))  # Infomap requires integer node IDs
for u, v in G.edges():
    im.add_edge(int(u), int(v))

# Run Infomap
im.run()

# Extract communities
communities = {}
for node in im.tree:
    if node.is_leaf:
        communities[str(node.node_id)] = node.module_id

print("Infomap Communities:", communities)'''

import networkx as nx
from infomap import Infomap
from collections import defaultdict

# --- Step 1: Convert Graph Nodes to Integer IDs ---
def run_infomap(G):
    """Runs InfoMap on the directed graph and returns the detected communities."""
    infomap = Infomap(silent=True, directed=True)

    # Create a mapping from country names to unique integer IDs
    node_to_id = {node: idx for idx, node in enumerate(G.nodes())}
    id_to_node = {idx: node for node, idx in node_to_id.items()}  # Reverse mapping
    
    # Add edges using integer IDs
    for u, v in G.edges():
        infomap.add_link(node_to_id[u], node_to_id[v])
    
    # Run the InfoMap clustering algorithm
    infomap.run()

    # Store communities with original country names
    communities = {}
    for node in infomap.nodes:
        communities[id_to_node[node.node_id]] = node.module_id  # Convert back to country names
    
    return communities

# --- Step 2: Format Communities for Output ---
def format_infomap_communities(communities):
    """Formats and prints the communities found by InfoMap."""
    sorted_communities = defaultdict(list)
    
    for country, community in communities.items():
        sorted_communities[community].append(country)

    for community in sorted(sorted_communities.keys()):
        sorted_communities[community].sort()  # Sort country names alphabetically
    
    return sorted_communities

def directed_modularity(G, partition):
    """Computes directed modularity based on Leicht & Newman's formula."""
    m = G.number_of_edges()  # Total number of edges
    if m == 0:
        return 0  # Avoid division by zero

    in_degrees = dict(G.in_degree(weight='weight'))  # Weighted in-degree
    out_degrees = dict(G.out_degree(weight='weight'))  # Weighted out-degree

    modularity_sum = 0
    for u, v in G.edges():
        if partition[u] == partition[v]:  # Nodes belong to the same community
            A_uv = 1  # Adjacency matrix (1 if edge exists)
            expected_weight = (in_degrees[u] * out_degrees[v]) / m
            modularity_sum += (A_uv - expected_weight)

    return modularity_sum / m  # Normalize by total edges

# Load your graph (replace with your data)
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

# --- Step 3: Run InfoMap and Print Communities ---
infomap_communities = run_infomap(G)
sorted_infomap_communities = format_infomap_communities(infomap_communities)

# Print communities
for community, countries in sorted_infomap_communities.items():
    print(f"Community {community}: {', '.join(countries)}")

# Compute modularity for InfoMap communities
directed_modularity_score = directed_modularity(G, infomap_communities)
print(f"Directed Modularity Score (InfoMap): {directed_modularity_score}")

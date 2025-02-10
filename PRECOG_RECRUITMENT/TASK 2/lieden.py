import leidenalg as la
import igraph as ig
import networkx as nx
from scipy.sparse import csr_matrix

# Convert NetworkX directed graph to igraph
def nx_to_ig(nx_graph):
    # Get the adjacency matrix in sparse format
    adj_matrix = nx.adjacency_matrix(nx_graph)
    # Convert sparse matrix to dense array and then to a list of lists
    adj_dense = adj_matrix.toarray()
    # Convert to igraph
    return ig.Graph.Adjacency(adj_dense.tolist(), mode=ig.ADJ_DIRECTED)

# Load your graph (replace with your data)
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
# Convert to igraph
ig_graph = nx_to_ig(G)

# Run Leiden with CPMVertexPartition for directed graphs
partition = la.find_partition(
    ig_graph,
    la.CPMVertexPartition,
    resolution_parameter=0.1  # Tune this (0.1 to 1.0)
    #weights="weight",  # Optional
)

# Assign communities back to NetworkX
communities = {}
for i, node in enumerate(G.nodes()):
    communities[node] = partition.membership[i]

print("Leiden Communities:", communities)
# Calculate modularity score
modularity_score = partition.modularity
print(f"Modularity Score: {modularity_score}")
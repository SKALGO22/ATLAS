import networkx as nx

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

# Find all strongly connected components
sccs = list(nx.strongly_connected_components(G))

# Print the SCCs
print("Strongly Connected Components:")
for i, scc in enumerate(sccs, 1):
    print(f"Component {i}: {sorted(scc)}")

# Total number of SCCs
print(f"\nTotal number of strongly connected components: {len(sccs)}")

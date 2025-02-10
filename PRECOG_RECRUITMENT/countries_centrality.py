import networkx as nx
import matplotlib.pyplot as plt

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

# Compute degrees
out_degree = dict(G.out_degree())
in_degree = dict(G.in_degree())
degree_difference = {node: in_degree[node] - out_degree[node] for node in G.nodes()}

# Sort by descending order
out_degree_sorted = sorted(out_degree.items(), key=lambda x: x[1], reverse=True)
in_degree_sorted = sorted(in_degree.items(), key=lambda x: x[1], reverse=True)
degree_diff_sorted = sorted(degree_difference.items(), key=lambda x: x[1], reverse=True)

# Extract data for plotting
out_degree_nodes, out_degree_values = zip(*out_degree_sorted)
in_degree_nodes, in_degree_values = zip(*in_degree_sorted)
degree_diff_nodes, degree_diff_values = zip(*degree_diff_sorted)

# Create bar plots
fig, axs = plt.subplots(3, 1, figsize=(15, 20), constrained_layout=True)

# Out-degree bar graph
axs[0].bar(out_degree_nodes, out_degree_values, color='skyblue', alpha=0.9, edgecolor='black')
axs[0].set_title("Out-degree of Vertices (Descending Order)", fontsize=16)
axs[0].set_xlabel("Countries (First and Last Letters)", fontsize=12)
axs[0].set_ylabel("Out-degree", fontsize=12)
axs[0].tick_params(axis='x', rotation=90)

# In-degree bar graph
axs[1].bar(in_degree_nodes, in_degree_values, color='lightgreen', alpha=0.9, edgecolor='black')
axs[1].set_title("In-degree of Vertices (Descending Order)", fontsize=16)
axs[1].set_xlabel("Countries (First and Last Letters)", fontsize=12)
axs[1].set_ylabel("In-degree", fontsize=12)
axs[1].tick_params(axis='x', rotation=90)

# Out-degree minus in-degree bar graph
axs[2].bar(degree_diff_nodes, degree_diff_values, color='salmon', alpha=0.9, edgecolor='black')
axs[2].set_title("In-degree - Out-degree (Descending Order)", fontsize=16)
axs[2].set_xlabel("Countries (First and Last Letters)", fontsize=12)
axs[2].set_ylabel("In-degree - Out-degree", fontsize=12)
axs[2].tick_params(axis='x', rotation=90)

# Show the plots
plt.show()

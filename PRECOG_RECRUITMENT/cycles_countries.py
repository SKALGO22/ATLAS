import networkx as nx

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

# Find and print all cycles of length up to 15
print("\nCycles of length up to 3:")

'''i=0
for cycle in nx.simple_cycles(G, 3):
    cycle_length = len(cycle)
    i+=1
    Cycle of length {cycle_length}
    print(f" {i}: {cycle}")
'''
# Find all cycles (simple cycles) and filter for those of length 3 or less
cycles_leq3 = list(nx.simple_cycles(G, 3))
#cycles_leq3 = [cycle for cycle in all_cycles if len(cycle) <= 3]

print("\nCycles of length <= 3:")
for i, cycle in enumerate(cycles_leq3, 1):
    print(f"{i}: {cycle}")

# Count how many cycles (of length <= 3) each node participates in
cycle_counts = {node: 0 for node in G.nodes()}
for cycle in cycles_leq3:
    for node in cycle:
        cycle_counts[node] += 1

# Filter out nodes with zero cycle counts and sort the remaining in descending order
nonzero_cycle_counts = [(node, count) for node, count in cycle_counts.items() if count > 0]
sorted_cycle_counts = sorted(nonzero_cycle_counts, key=lambda x: x[1], reverse=True)

# Extract node names and counts for plotting
nodes, counts = zip(*sorted_cycle_counts)

# Plot the bar graph
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.bar(nodes, counts, color='mediumseagreen', edgecolor='black')
plt.xlabel('Nodes', fontsize=14)
plt.ylabel('Number of Cycles (length <= 3)', fontsize=14)
plt.title('Nodes vs. Cycle Count (Cycles of Length <= 3)', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()


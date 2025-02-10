import matplotlib.pyplot as plt

# Given centrality dictionaries
degree_centrality = {
    'Q-set': 0.125, 'R-set': 0.3125, 'O-set': 0.4375, 'G-set': 0.375, 'C-set': 0.5625,
    'Y-set': 0.375, 'E-set': 0.5625, 'L-set': 0.5, 'T-set': 0.5625, 'S-set': 0.8125,
    'K-set': 0.3125, 'A-clique': 1.0, 'D-set': 0.625, 'M-set': 0.4375, 'I-set': 0.6875,
    'U-set': 0.5625, 'N-set': 1.125
}

betweenness_centrality = {
    'C-set': 0.0122, 'I-set': 0.1349, 'G-set': 0.0132, 'R-set': 0.0625, 'S-set': 0.0733,
    'N-set': 0.4489, 'K-set': 0.0121, 'M-set': 0.0083, 'U-set': 0.0960, 'Y-set': 0.0,
    'O-set': 0.0044, 'T-set': 0.0485, 'Q-set': 0.0027, 'D-set': 0.2139, 'A-clique': 0.1274,
    'L-set': 0.0758, 'E-set': 0.0700
}

# Sort the dictionaries in descending order
degree_sorted = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
betweenness_sorted = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

# Extract data for plotting
degree_labels, degree_values = zip(*degree_sorted)
betweenness_labels, betweenness_values = zip(*betweenness_sorted)

# Create bar plots
fig, axs = plt.subplots(2, 1, figsize=(12, 12), constrained_layout=True)

# Degree Centrality Bar Graph
axs[0].bar(degree_labels, degree_values, color='dodgerblue', alpha=0.85, edgecolor='black')
axs[0].set_title("Degree Centrality (Descending Order)", fontsize=16, fontweight="bold")
axs[0].set_xlabel("Nodes", fontsize=12)
axs[0].set_ylabel("Degree Centrality", fontsize=12)
axs[0].tick_params(axis='x', rotation=45)

# Betweenness Centrality Bar Graph
axs[1].bar(betweenness_labels, betweenness_values, color='tomato', alpha=0.85, edgecolor='black')
axs[1].set_title("Betweenness Centrality (Descending Order)", fontsize=16, fontweight="bold")
axs[1].set_xlabel("Nodes", fontsize=12)
axs[1].set_ylabel("Betweenness Centrality", fontsize=12)
axs[1].tick_params(axis='x', rotation=45)

# Show the plots
plt.show()

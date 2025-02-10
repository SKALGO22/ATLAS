import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Load the list of countries
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    countries = [line.strip().lower() for line in f if line.strip()]  # Ensure consistent formatting
countries.sort()

# Count occurrences of starting and ending letters
start_letter_counts = Counter(country[0] for country in countries)
end_letter_counts = Counter(country[-1] for country in countries)

# Sort counts in descending order
start_letter_sorted = sorted(start_letter_counts.items(), key=lambda x: x[1], reverse=True)
end_letter_sorted = sorted(end_letter_counts.items(), key=lambda x: x[1], reverse=True)

# Extract data for plotting
start_letters, start_counts = zip(*start_letter_sorted)
end_letters, end_counts = zip(*end_letter_sorted)

# Create bar plots
fig, axs = plt.subplots(2, 1, figsize=(15, 15), constrained_layout=True)

# Plot for starting letters
axs[0].bar(start_letters, start_counts, color='skyblue', alpha=0.9, edgecolor='black')
axs[0].set_title("Number of Countries Starting with Each Letter (Descending Order)", fontsize=16)
axs[0].set_xlabel("Starting Letters", fontsize=12)
axs[0].set_ylabel("Number of Countries", fontsize=12)
axs[0].tick_params(axis='x', rotation=90)

# Plot for ending letters
axs[1].bar(end_letters, end_counts, color='lightgreen', alpha=0.9, edgecolor='black')
axs[1].set_title("Number of Countries Ending with Each Letter (Descending Order)", fontsize=16)
axs[1].set_xlabel("Ending Letters", fontsize=12)
axs[1].set_ylabel("Number of Countries", fontsize=12)
axs[1].tick_params(axis='x', rotation=90)

# Show the plots
plt.show()

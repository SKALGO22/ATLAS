'''import networkx as nx
import matplotlib.pyplot as plt
import random
import copy
from collections import defaultdict

# ---------------------------
# Step 1. Build the Weighted Graph
# ---------------------------

# Excluded letters: we do not consider countries that start or end with these
exclude = {'n','a', 'y', 'o', 'r', 'q'}

# Load the list of countries from file
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]
full_countries.sort()

# Reduce each country's name to its first and last letter.
# We only keep those countries whose first and last letters are NOT in the exclusion set.
filtered_countries = [country for country in full_countries 
                      if (country[0] not in exclude and country[-1] not in exclude)]
reduced_countries = [f"{country[0]}{country[-1]}" for country in filtered_countries]
# (We do not remove duplicates here because we need counts for weights.)

# Extract unique letters from the reduced countries
letters = set(letter for country in reduced_countries for letter in country)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with special naming: "A-clique" for letter 'a', otherwise "X-set"
for letter in letters:
    node_name = "A-clique" if letter == "a" else f"{letter.upper()}-set"
    G.add_node(node_name)

# Add weighted edges: for each two-letter string from reduced_countries,
# add (or increment) an edge from the node corresponding to its first letter to the node corresponding to its last letter.
for country in reduced_countries:
    if len(country) == 2:
        source = "A-clique" if country[0] == "a" else f"{country[0].upper()}-set"
        target = "A-clique" if country[1] == "a" else f"{country[1].upper()}-set"
        if G.has_edge(source, target):
            G[source][target]['weight'] += 1
        else:
            G.add_edge(source, target, weight=1)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Save the original weights so we can reset for each game.
original_weights = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}

# ---------------------------
# Step 2. Define Priority Order and Move Functions
# ---------------------------

# Given descending order of node difference (incoming - outgoing) is: {e, s, d, i, t, l, k, g, u, c, m}.
# The increasing order (from lowest to highest difference) is:
order_list = ['m', 'c', 'u', 'g', 'k', 'l', 't', 'i', 'd', 's', 'e']
# Build a dictionary for ranking a letter:
rank = {letter: idx for idx, letter in enumerate(order_list)}

def get_letter_from_node(node):
    # Given a node name like "X-set" or "A-clique", return the lowercase letter.
    if node == "A-clique":
        return 'a'
    else:
        return node[0].lower()

def player1_move(current_node, graph):
    """
    Player1 considers all legal moves (edges with weight > 0) from current_node.
    Among these, he selects the move (current_node -> target) with the highest priority,
    where the priority key is (source_rank, -target_rank).
    Since the source is fixed (current_node), we choose the move with target having the highest rank (i.e. largest index in order_list).
    If no legal move exists, return None.
    """
    legal_moves = []
    for _, target, data in graph.out_edges(current_node, data=True):
        if data.get('weight', 0) > 0:
            target_letter = get_letter_from_node(target)
            # Only consider if target_letter is in our ranking dictionary.
            if target_letter in rank:
                legal_moves.append((target, rank[target_letter]))
    if not legal_moves:
        return None
    # Choose move with maximum rank value (i.e. highest target letter in our increasing order).
    legal_moves.sort(key=lambda x: x[1], reverse=True)
    chosen_target = legal_moves[0][0]
    return (current_node, chosen_target)

def player2_move(current_node, graph):
    """
    Player2 picks a random legal move from current_node.
    Return the edge (current_node, target) or None if no legal moves.
    """
    legal_moves = [(current_node, target) 
                   for _, target, data in graph.out_edges(current_node, data=True) if data.get('weight', 0) > 0]
    if not legal_moves:
        return None
    return random.choice(legal_moves)

# ---------------------------
# Step 3. Simulate Games
# ---------------------------

def simulate_game(start_node, graph):
    """
    Simulate one game.
    - The graph's edge weights are modified during the game.
    - Player1 uses the strategy defined in player1_move.
    - Player2 picks a random legal move.
    - Players alternate turns. 
    - The game ends when the current player has no legal move.
    Returns the winner: 1 if Player1 wins, 2 if Player2 wins.
    """
    current_node = start_node
    current_player = 1  # 1 for Player1, 2 for Player2
    # Continue until a player cannot move.
    while True:
        # Check legal moves (edges with weight > 0) from current_node.
        legal_moves = [(u, v) for u, v, d in graph.out_edges(current_node, data=True) if d.get('weight', 0) > 0]
        if not legal_moves:
            # Current player cannot move; the other player wins.
            return 2 if current_player == 1 else 1
        
        # Select move based on player strategy
        if current_player == 1:
            move = player1_move(current_node, graph)
        else:
            move = player2_move(current_node, graph)
        
        if move is None:
            return 2 if current_player == 1 else 1
        
        # Execute the move: decrease edge weight by 1 (not below 0)
        u, v = move
        graph[u][v]['weight'] = max(graph[u][v]['weight'] - 1, 0)
        # Set new current node and switch player
        current_node = v
        current_player = 2 if current_player == 1 else 1

# Starting positions for Player1: {s, u, l, d} → Their node names: "S-set", "U-set", "L-set", "D-set"
starting_letters = ['s', 'u', 'l', 'd']
starting_nodes = [f"{letter.upper()}-set" for letter in starting_letters]

num_games = 100
player1_wins = 0

# For reproducibility
random.seed(42)

for i in range(num_games):
    # For each game, reset a fresh copy of the graph with original edge weights.
    game_graph = nx.DiGraph()
    game_graph.add_nodes_from(G.nodes(data=True))
    for u, v, data in G.edges(data=True):
        game_graph.add_edge(u, v, weight=original_weights[(u, v)])
    
    # Choose a starting node for Player1 at random among the specified ones.
    start_node = random.choice(starting_nodes)
    
    winner = simulate_game(start_node, game_graph)
    if winner == 1:
        player1_wins += 1

player1_win_percentage = (player1_wins / num_games) * 100
print(f"Player1 wins {player1_win_percentage:.2f}% of the {num_games} games.")
'''
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy
from collections import defaultdict

# ---------------------------
# Helper Functions and Global Preference Setup
# ---------------------------

# Our given descending order (incoming wt - outgoing wt) is {e, s, d, i, t, l, k, g, u, c, m}.
# Thus the increasing order (lowest to highest) is:
order_list = ['m', 'c', 'u', 'g', 'k', 'l', 't', 'i', 'd', 's', 'e']
# Build a ranking dictionary: lower index = lower "value"
rank = {letter: idx for idx, letter in enumerate(order_list)}

def get_letter_from_node(node):
    """
    Given a node name like "A-clique" or "X-set", return the underlying lowercase letter.
    """
    if node == "A-clique":
        return 'a'
    else:
        # Assume node name is like "X-set"; extract first character and convert to lowercase.
        return node[0].lower()

def is_dead_end(node, graph):
    """
    Returns True if the node has no outgoing edge with nonzero weight.
    """
    for u, v, data in graph.out_edges(node, data=True):
        if data.get('weight', 0) > 0:
            return False
    return True

# ---------------------------
# Step 1. Build the Weighted Graph for ATLAS
# ---------------------------

# Exclusion set for this game is given in the previous instructions when building the graph,
# but here we are using your pre-built graph from countries_inPlay.txt.
# For this simulation, we assume the graph G is built using the two-letter reduction.
# (Below is your code to build the graph.)

# Load the list of countries
# ---------------------------
# Step 1. Build the Weighted Graph
# ---------------------------

# Excluded letters: we do not consider countries that start or end with these
exclude = {'n','a', 'y', 'o', 'r', 'q'}

# Load the list of countries from file
with open("/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/countries_inPlay.txt", "r") as f:
    full_countries = [line.strip().lower() for line in f if line.strip()]
full_countries.sort()

# Reduce each country's name to its first and last letter.
# We only keep those countries whose first and last letters are NOT in the exclusion set.
filtered_countries = [country for country in full_countries 
                      if (country[0] not in exclude and country[-1] not in exclude)]
reduced_countries = [f"{country[0]}{country[-1]}" for country in filtered_countries]
# (We do not remove duplicates here because we need counts for weights.)

# Extract unique letters from the reduced countries
letters = set(letter for country in reduced_countries for letter in country)

# Create a directed graph
G = nx.DiGraph()

# Add nodes with special naming: "A-clique" for letter 'a', otherwise "X-set"
for letter in letters:
    node_name = "A-clique" if letter == "a" else f"{letter.upper()}-set"
    G.add_node(node_name)

# Add weighted edges: for each two-letter string from reduced_countries,
# add (or increment) an edge from the node corresponding to its first letter to the node corresponding to its last letter.
for country in reduced_countries:
    if len(country) == 2:
        source = "A-clique" if country[0] == "a" else f"{country[0].upper()}-set"
        target = "A-clique" if country[1] == "a" else f"{country[1].upper()}-set"
        if G.has_edge(source, target):
            G[source][target]['weight'] += 1
        else:
            G.add_edge(source, target, weight=1)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Save the original weights (so we can reset them between games)
original_weights = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}

# ---------------------------
# Step 2. Define Player Move Functions with Modified Player1 Strategy
# ---------------------------

def player1_move(current_node, graph):
    """
    Player1's strategy:
      1. Among all legal moves (edges with weight > 0) from current_node,
         check if any move leads to a dead-end (i.e. target node has no outgoing edge with weight > 0).
         If one or more exist, choose the one whose target letter has the highest rank (largest rank value).
      2. Otherwise, among all legal moves, choose the one with highest target rank (i.e., maximum rank[target_letter]).
    Return the chosen move as a tuple (current_node, target) or None if no legal moves.
    """
    legal_moves = []
    dead_end_moves = []
    for _, target, data in graph.out_edges(current_node, data=True):
        if data.get('weight', 0) > 0:
            # Check if target is a dead end
            if is_dead_end(target, graph):
                dead_end_moves.append(target)
            # Record legal move with target's rank
            target_letter = get_letter_from_node(target)
            if target_letter in rank:
                legal_moves.append((target, rank[target_letter]))
    
    # If any move leads to a dead end, choose the one with highest target rank.
    if dead_end_moves:
        # Sort the dead_end_moves by their target letter rank (largest rank first)
        dead_end_moves.sort(key=lambda t: rank[get_letter_from_node(t)], reverse=True)
        return (current_node, dead_end_moves[0])
    
    if not legal_moves:
        return None
    # Otherwise, sort legal moves by target rank (largest rank first)
    legal_moves.sort(key=lambda x: x[1], reverse=True)
    return (current_node, legal_moves[0][0])

def player2_move(current_node, graph):
    """
    Player2 picks a random legal move from current_node (i.e., any edge with weight > 0).
    """
    legal_moves = [(current_node, target) 
                   for _, target, data in graph.out_edges(current_node, data=True)
                   if data.get('weight', 0) > 0]
    if not legal_moves:
        return None
    return random.choice(legal_moves)

# ---------------------------
# Step 3. Simulate the Game
# ---------------------------

def simulate_game(start_node, graph):
    """
    Simulate one game.
      - The graph's edge weights are modified during the game.
      - Player1 uses the modified strategy.
      - Player2 makes random legal moves.
      - Players alternate turns.
    The game ends when the current player has no legal move; the other player wins.
    Returns: 1 if Player1 wins, 2 if Player2 wins.
    """
    current_node = start_node
    current_player = 1  # 1 for Player1, 2 for Player2
    while True:
        # List legal moves from current_node: edges with weight > 0.
        legal_moves = [(u, v) for u, v, d in graph.out_edges(current_node, data=True) if d.get('weight', 0) > 0]
        if not legal_moves:
            # No legal moves from current_node, so current player loses.
            return 2 if current_player == 1 else 1
        
        if current_player == 1:
            move = player1_move(current_node, graph)
        else:
            move = player2_move(current_node, graph)
        
        if move is None:
            return 2 if current_player == 1 else 1
        
        # Execute the move: reduce edge weight by 1 (min 0)
        u, v = move
        graph[u][v]['weight'] = max(graph[u][v]['weight'] - 1, 0)
        # Set new current node and switch player
        current_node = v
        current_player = 2 if current_player == 1 else 1

# ---------------------------
# Step 4. Run 100 Simulations and Report Results
# ---------------------------

# Starting positions for Player1: allowed starting letters {s, u, l, d} → corresponding nodes: "S-set", "U-set", "L-set", "D-set"
starting_letters = ['s', 'u', 'l', 'd']
starting_nodes = [f"{letter.upper()}-set" for letter in starting_letters]

num_games = 100000
player1_wins = 0

random.seed(42)

for i in range(num_games):
    # For each game, create a fresh copy of the graph with original weights.
    game_graph = nx.DiGraph()
    game_graph.add_nodes_from(G.nodes(data=True))
    for u, v, data in G.edges(data=True):
        game_graph.add_edge(u, v, weight=original_weights[(u, v)])
    
    # Choose a starting node at random from the allowed starting positions.
    start_node = random.choice(starting_nodes)
    
    winner = simulate_game(start_node, game_graph)
    if winner == 1:
        player1_wins += 1

player1_win_percentage = (player1_wins / num_games) * 100
print(f"Player1 wins {player1_win_percentage:.2f}% of the {num_games} games.")

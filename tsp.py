import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations

# Function to calculate the total distance of a route
def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance_matrix[route[i-1]][route[i]]
    return total_distance

# Function to visualize the route along with other short distances
def visualize_route_with_others(route, distance_matrix, title="TSP Route"):
    G = nx.DiGraph()
    n = len(distance_matrix)
    # Add all nodes and edges to the graph with default weights
    for i in range(n):
        G.add_node(i)
        for j in range(n):
            if i != j:  # Avoid loops
                G.add_edge(i, j, weight=distance_matrix[i][j])
    
    pos = nx.circular_layout(G)  # Circular layout for better visualization
    # Draw all edges with light grey color and dashed lines to represent "roads not taken"
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color="gray", style="dashed")
    # Highlight the route edges
    route_edges = [(route[i-1], route[i]) for i in range(len(route))]
    nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color="blue", width=2, arrows=True)
    
    # Draw nodes and labels
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title(title)
    plt.axis('off')
    plt.show()

# Function to solve the TSP with visualization, including other paths
def tsp_brute_force_with_advanced_visualization(distance_matrix):
    n = len(distance_matrix)  # Number of cities
    all_routes = permutations(range(n))
    min_distance = float('inf')
    best_route = None
    for route in all_routes:
        current_distance = calculate_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
            visualize_route_with_others(route, distance_matrix, f"Current Best: {min_distance}")
    return best_route, min_distance

# Updated distance matrix for 6 cities
distance_matrix = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 20, 15],
    [15, 35, 0, 30, 25, 20],
    [20, 25, 30, 0, 15, 10],
    [25, 20, 25, 15, 0, 35],
    [30, 15, 20, 10, 35, 0]
]

# Solve the TSP with advanced visualization
best_route, min_distance = tsp_brute_force_with_advanced_visualization(distance_matrix)

print(f"The best route is: {best_route} with a total distance of {min_distance}")
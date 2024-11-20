def nearest_neighbor(distance_matrix, start_node):
    """
    Implements the Nearest Neighbor Algorithm for finding a route.

    :param distance_matrix: 2D list representing distances between nodes.
    :param start_node: The starting node (hub).
    :return: A list representing the route and the total distance traveled.
    """
    n = len(distance_matrix)  # Number of locations
    visited = [False] * n  # Keep track of visited nodes
    route = [start_node]  # Start from the given start node
    total_distance = 0  # Total distance traveled

    current_node = start_node
    visited[start_node] = True

    for _ in range(n - 1):  # Visit all nodes
        nearest_distance = float('inf')
        nearest_node = None

        # Find the nearest unvisited node
        for next_node in range(n):
            if not visited[next_node] and distance_matrix[current_node][next_node] < nearest_distance:
                nearest_distance = distance_matrix[current_node][next_node]
                nearest_node = next_node

        # Travel to the nearest node
        if nearest_node is not None:
            route.append(nearest_node)
            total_distance += nearest_distance
            visited[nearest_node] = True
            current_node = nearest_node

    # Return to the start node to complete the route (optional for a closed route)
    if route[0] != current_node:
        total_distance += distance_matrix[current_node][start_node]
        route.append(start_node)

    return route, total_distance


# Example Usage
if __name__ == "__main__":
    # Example distance matrix (symmetric for undirected graph)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_node = 0  # Start at node 0 (hub)

    route, total_distance = nearest_neighbor(distance_matrix, start_node)
    print(f"Optimal Route: {route}")
    print(f"Total Distance: {total_distance}")

    # @staticmethod
    # def nearest_neighbor(matrix, addresses, start_index=0):
    #     """
    #     Nearest Neighbor Algorithm using an adjacency matrix.

    #     :param matrix: 2D list representing the adjacency matrix.
    #     :param nodes: List of node names corresponding to the matrix indices.
    #     :param start_index: Index of the starting node.
    #     :return: A tuple containing the route (list of nodes) and total distance.
    #     """
    #     n = len(matrix)
    #     visited = [False] * n
    #     route = [start_index]
    #     total_distance = 0

    #     current_index = start_index
    #     visited[current_index] = True

    #     for _ in range(n - 1):
    #         nearest_distance = float('inf')
    #         nearest_index = None

    #         for next_index in range(n):
    #             current_dist = float(matrix[current_index][next_index])
    #             if not visited[next_index] and current_dist < nearest_distance:
    #                 nearest_distance = current_dist
    #                 nearest_index = next_index

    #         if nearest_index is not None:
    #             route.append(nearest_index)
    #             total_distance += nearest_distance
    #             visited[nearest_index] = True
    #             current_index = nearest_index

    #     # Optionally return to the starting node
    #     total_distance += float(matrix[current_index][start_index])
    #     route.append(start_index)

    #     # Convert route indices to node names
    #     route_names = [addresses[i] for i in route]
    #     return route, route_names, total_distance
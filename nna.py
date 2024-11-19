def euclidean_distance_helper(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

def nearest_neighbor(query_point, data_points):

    nearest = None
    min_distance = float('inf')  # Initialize to infinity

    # for each of the data points
    for point in data_points:
      # find the distance between the point
      # if the distance is smaller than the current min_distance update
      # do it for all the points
      # you should have the smallest distance from the query point to the point
        distance = euclidean_distance_helper(query_point, point)
        if distance < min_distance:
            min_distance = distance
            nearest = point

    return nearest, min_distance

# Example usage
data_points = [[1, 2], [3, 4], [5, 6], [8, 9]]  # Dataset
query_point = [4, 4]  # Point to search for its nearest neighbor

nearest, distance = nearest_neighbor(query_point, data_points)
print(f"Nearest Neighbor: {nearest}, Distance: {distance:.2f}")

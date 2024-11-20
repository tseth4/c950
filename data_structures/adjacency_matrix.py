class AdjacencyMatrix:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def set_distance(self, i, j, distance):
        self.matrix[i][j] = distance
        self.matrix[j][i] = distance  # Symmetric for undirected graph

    def get_distance(self, i, j):
        return self.matrix[i][j]

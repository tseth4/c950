class AdjacencyMatrix:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def set_distance(self, i, j, distance):
        self._validate_indices(i, j)
        self.matrix[i][j] = distance
        self.matrix[j][i] = distance  # Symmetric for undirected graph

    def get_distance(self, i, j):
        self._validate_indices(i, j)
        return self.matrix[i][j]

    def add_node(self):
        """Add a new node to the adjacency matrix."""
        self.size += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.size)

    def find_neighbors(self, node):
        """Find all neighbors of a given node."""
        self._validate_indices(node, node)
        return [i for i, distance in enumerate(self.matrix[node]) if distance > 0]

    def _validate_indices(self, i, j):
        """Ensure indices are within bounds."""
        if not (0 <= i < self.size and 0 <= j < self.size):
            raise IndexError("Invalid indices for adjacency matrix.")

    def __str__(self):
        """Return a string representation of the adjacency matrix."""
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

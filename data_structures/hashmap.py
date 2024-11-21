from datetime import datetime
from src.package_status import PackageStatus 

class HashMap:
    def __init__(self, initial_size=10):
        """Initialize the hash map with a default number of buckets."""
        self.size = initial_size
        self.map = [None] * self.size
        self.count = 0  # Track the number of elements in the hash map

    def _hash(self, key):
        """Generate a hash for the key using Python's built-in hash function."""
        return hash(key) % self.size

    def _resize(self):
        """Resize the hash map when the load factor exceeds the threshold."""
        print("Resizing hash map...")
        # double the size
        new_size = self.size * 2
        new_map = [None] * new_size

        # Rehash all existing elements
        for bucket in self.map:
            if bucket is not None:
                for key, value in bucket:
                    new_hash = hash(key) % new_size
                    if new_map[new_hash] is None:
                        new_map[new_hash] = []
                    new_map[new_hash].append([key, value])

        # Replace old map with the new map
        self.map = new_map
        self.size = new_size

    def add(self, key, value):
        """Add a key-value pair to the hash map."""
        if self.count / self.size > 0.75:  # Load factor threshold
            self._resize()

        key_hash = self._hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            self.count += 1
        else:
            for pair in self.map[key_hash]:
              # if the elements key matches our key, update the value
                if pair[0] == key:
                    pair[1] = value
                    return
              # if the key is not in there just append or add new
            self.map[key_hash].append(key_value)
            self.count += 1

    def get(self, key):
        """Retrieve the value associated with the given key."""
        key_hash = self._hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash map."""
        key_hash = self._hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                self.count -= 1
                return True
        return False

    def keys(self):
        """Return a list of all keys in the hash map."""
        keys_list = []
        for bucket in self.map:
            if bucket:
                for pair in bucket:
                    keys_list.append(pair[0])
        return keys_list

    def print(self):
        """Print the contents of the hash map."""
        print("-- HashMap Contents --")
        for i, bucket in enumerate(self.map):
            if bucket is not None:
                print(f"Bucket {i}: {bucket}")

    def get_sorted_packages_by_deadline(self):
        """
        Return all packages sorted by deadline. 
        Packages with "EOD" deadlines appear last.
        """
        # Collect all packages
        packages = []
        for bucket in self.map:
            if bucket:
                for _, package in bucket:
                    packages.append(package)

        # Define a key function to sort by deadline
        def parse_deadline(package):
            if package.deadline == "EOD":
                return datetime.max  # Treat "EOD" as the latest possible time
            else:
                return datetime.strptime(package.deadline, "%I:%M %p")

        # Sort the packages
        sorted_packages = sorted(packages, key=parse_deadline)

        return sorted_packages

    def sort_packages_by_deadline_and_proximity(self, adjacency_matrix, addresses):
        """
        Return all packages sorted by deadline (earliest first) and proximity to the hub.
        Packages with "EOD" deadlines appear last.

        :param adjacency_matrix: 2D list representing distances between addresses.
        :param addresses: List of address names corresponding to matrix indices.
        :return: List of sorted packages.
        """
        # Collect all packages
        packages = []
        for bucket in self.map:
            if bucket:
                for _, package in bucket:
                    packages.append(package)

        # Define a key function to calculate sorting priority
        def sort_key(package):
            # Parse deadline
            if package.deadline == "EOD":
                deadline = datetime.max  # Treat "EOD" as the latest possible time
            else:
                deadline = datetime.strptime(package.deadline, "%I:%M %p")

            # Calculate proximity (distance from hub)
            hub_index = 0
            package_address_index = addresses.index(package.address)
            proximity = adjacency_matrix[hub_index][package_address_index]

            return (deadline, proximity)

        # Sort packages by deadline first, then proximity
        sorted_packages = sorted(packages, key=sort_key)

        return sorted_packages

    def values(self):
        """Return a list of all values in the hash map."""
        values_list = []
        for bucket in self.map:
            if bucket:  # Check if the bucket is not empty
                for _, value in bucket:
                    values_list.append(value)
        return values_list
    def get_undelivered_packages(self):
        """
        Retrieve all undelivered packages from the hash map.

        :return: List of undelivered Package objects.
        """
        at_hub = []
        for bucket in self.map:
            if bucket:  # If the bucket is not empty
                for _, package in bucket:
                    if package.status == PackageStatus.AT_HUB:
                        at_hub.append(package)
        return at_hub


class HashMap:
    # 50 elements 50 buckets
    # 40 packages -> 40 buckets?
    # key % 40
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._hash(key)
        key_value = [key, value]
        # if cell is empty then we can add to the map with a list with a value inside
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True
        else:
            # if cell is not empty. check if key exists to update. or if not exist append
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # if we dont find a  match append
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._hash(key)
        if self.map[key_hash] is not None:
            for k, v in self.map[key_hash]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        key_hash = self._hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print("--phonebook--")
        for item in self.map:
            if item is not None:
                print(str(item))



class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hashVal = 0
        for char in key:
            hashVal += ord(char)
        return hashVal % 5

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        added = False

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            added = True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    added = True
                    return added
            self.map[key_hash].append(key_value)
            return added
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

h = HashMap()
h.add('bob','test')
h.add('nice','what')

h.print()

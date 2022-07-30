# Hash map implementation from scratch using chaining to handle collisions

class HashMap:
    def __init__(self):
        self.max = 10
        self.hash_map = [[] for x in range(self.max)]

    def compute_hash(self, key):
        val = 0
        for char in key:
            val += ord(char)
        return val % 10

    def __setitem__(self, key, value):
        index = self.compute_hash(key)
        found = False
        for idx, item in enumerate(self.hash_map[index]):
            if item[0] == key:
                self.hash_map[index][idx] = (key, value)
                found = True
                break

        if not found:
            self.hash_map[index].append((key, value))

    def __getitem__(self, key):
        index = self.compute_hash(key)
        for item in self.hash_map[index]:
            if item[0] == key:
                return item[1]

    def __delitem__(self, key):
        index = self.compute_hash(key)
        for item in self.hash_map[index]:
            if item[0] == key:
                self.hash_map[index].remove(item)
                break


dict = HashMap()
dict['ramesh'] = 'hahaha'
dict['ramshe'] = 'pavan'
print(dict.hash_map)
del dict['ramesh']
print(dict.hash_map)

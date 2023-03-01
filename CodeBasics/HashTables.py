class HashTables:
    def __init__(self):
        self.arrayMax = 100
        self.array = [None for a in range(self.arrayMax)]

    def get_hash_value(self, key):
        value = 0
        for letter in key:
            # The ord() function returns the number representing the unicode code of a specified character.
            # Convert back to character with the chr() function.
            value += ord(letter)
        return value % self.arrayMax

    def add_item(self, key, value):
        hash_value = self.get_hash_value(key)
        self.array[hash_value] = value

    # Over-riding the get - set methods to use the operator '[ ] '

    def __getitem__(self, key):
        hash_value = self.get_hash_value(key)
        return self.array[hash_value]

    def __setitem__(self, key, value):
        hash_value = self.get_hash_value(key)
        self.array[hash_value] = value

    def get_item(self, key):
        hash_value = self.get_hash_value(key)
        return self.array[hash_value]


if __name__ == '__main__':
    Hash = HashTables()

    Hash.add_item('harsh', 20)
    Hash.add_item('slow', 10)
    Hash['potent'] = 70

    print(Hash.get_item('slow'))
    print(Hash['harsh'])
    print(Hash['potent'])

class HashTablesWithChaining:
    def __init__(self):
        self.arrayMax = 100
        self.array = [[] for a in range(self.arrayMax)]

    def get_hash_value(self, key):
        value = 0
        for letter in key:
            # The ord() function returns the number representing the unicode code of a specified character.
            # Convert back to character with the chr() function.
            value += ord(letter)
        return value % self.arrayMax

    def add_item(self, key, value):
        hash_value = self.get_hash_value(key)
        for item in self.array[hash_value]:
            if item[0] == key:
                item[1] = value
                return
        self.array[hash_value].append([key, value])

    # Over-riding the get - set methods to use the operator '[ ] '

    def __getitem__(self, key):
        hash_value = self.get_hash_value(key)
        for item in self.array[hash_value]:
            if item[0] == key:
                return item[1]

    def __setitem__(self, key, value):
        hash_value = self.get_hash_value(key)
        for item in self.array[hash_value]:
            if item[0] == key:
                item[1] = value
                return
        self.array[hash_value].append([key, value])

    def get_item(self, key):
        hash_value = self.get_hash_value(key)
        for item in self.array[hash_value]:
            if item[0] == key:
                return item[1]
        raise Exception('Values does not exist for key' + key)

    def __delitem__(self, key):
        hash_value = self.get_hash_value(key)
        for index, item in enumerate(self.array[hash_value]):
            if item[0] == key:
                print(index)
                del self.array[hash_value][index]


if __name__ == '__main__':
    HashWChaining = HashTablesWithChaining()

    HashWChaining.add_item('harsh', 20)
    HashWChaining.add_item('harsh', 30)

    HashWChaining.add_item('march 6', 100)
    HashWChaining.add_item('hcram 6', 300)

    print(HashWChaining.array)

    HashWChaining.add_item('slow', 10)
    HashWChaining['potent'] = 70
    #
    print('HashWChaining.get_item("slow")', HashWChaining.get_item('slow'))
    print('HashWChaining.get_item("march 6")', HashWChaining.get_item('march 6'))
    # print(HashWChaining.get_item('masda 6')) Throws Exception

    print('HashWChaining["harsh"]', HashWChaining['harsh'])
    print('HashWChaining["potent"]', HashWChaining['potent'])

    del HashWChaining['harsh']

    print(HashWChaining.array)

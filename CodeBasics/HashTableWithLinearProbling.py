class HashTablesWithLinearProbing:
    def __init__(self):
        self.arrayMax = 10
        self.array = [None for a in range(self.arrayMax)]

    def get_hash_value(self, key):
        value = 0
        for letter in key:
            # The ord() function returns the number representing the unicode code of a specified character.
            # Convert back to character with the chr() function.
            value += ord(letter)
        return value % self.arrayMax

    def get_hash_slots(self, index):
        return [*range(index, self.arrayMax)] + [*range(0, index)]

    def get_new_hash(self, key, index):
        hash_slots = self.get_hash_slots(index)
        for slot in hash_slots:
            if self.array[slot] is None:
                return slot
            else:
                if self.array[slot][0] == key:
                    return slot

        raise Exception('Full')

    def add_item(self, key, value):
        hash_value = self.get_hash_value(key)
        if self.array[hash_value]:
            if self.array[hash_value][0] == key:
                self.array[hash_value] = (key, value)
                return
            else:
                new_hash = self.get_new_hash(key, hash_value)
                self.array[new_hash] = (key, value)
                return
        self.array[hash_value] = (key, value)

    # Over-riding the get - set methods to use the operator '[ ] '

    def __getitem__(self, key):
        hash_value = self.get_hash_value(key)
        hash_slots = self.get_hash_slots(hash_value)
        for slot in hash_slots:
            if self.array[slot][0] == key:
                return self.array[slot][1]

        raise Exception('Values does not exist for key' + key)

    def __setitem__(self, key, value):
        hash_value = self.get_hash_value(key)
        if self.array[hash_value]:
            if self.array[hash_value][0] == key:
                self.array[hash_value] = value
                return
            else:
                new_hash = self.get_new_hash(key, hash_value)
                self.array[new_hash] = (key, value)
                return
        self.array[hash_value] = (key, value)

    def get_item(self, key):
        hash_value = self.get_hash_value(key)
        hash_slots = self.get_hash_slots(hash_value)
        for slot in hash_slots:
            if self.array[slot][0] == key:
                return self.array[slot][1]

        raise Exception('Values does not exist for key' + key)

    def __delitem__(self, key):
        hash_value = self.get_hash_value(key)
        hash_slots = self.get_hash_slots(hash_value)
        for slot in hash_slots:
            if self.array[slot] is None:
                return
            if self.array[slot][0] == key:
                self.array[slot] = None

        raise Exception('Values does not exist for key' + key)


if __name__ == '__main__':
    HashWLinearProbing = HashTablesWithLinearProbing()

    HashWLinearProbing.add_item('harsh', 20)
    HashWLinearProbing.add_item('harsh', 30)

    HashWLinearProbing.add_item('march 6', 100)
    HashWLinearProbing.add_item('hcram 6', 300)

    print(HashWLinearProbing.array)

    HashWLinearProbing.add_item('slow', 10)
    HashWLinearProbing['potent'] = 70
    #
    print('HashWLinearProbing.get_item("slow")', HashWLinearProbing.get_item('slow'))
    print('HashWLinearProbing.get_item("march 6")', HashWLinearProbing.get_item('march 6'))
    # print(HashWLinearProbing.get_item('masda 6')) Throws Exception

    print('HashWLinearProbing["harsh"]', HashWLinearProbing['harsh'])
    print('HashWLinearProbing["potent"]', HashWLinearProbing['potent'])

    del HashWLinearProbing['potent']

    print(HashWLinearProbing.array)

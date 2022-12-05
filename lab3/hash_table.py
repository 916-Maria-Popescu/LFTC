class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for index in range(size):
            self.table.append([])

    def getSize(self):
        return self.size

    def __hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char.lower())
        return sum % self.size

    def add(self, key):
        hash_value = self.__hash(key)
        if key not in self.table[hash_value]:
            self.table[hash_value].append(key)

    def find(self, key):
        hash_value = self.__hash(key)
        return key in self.table[hash_value]

    def remove(self, key):
        hash_value = self.__hash(key)
        if key in self.table[hash_value]:
            self.table[hash_value].remove(key)

    def position(self, key):
        return self.__hash(key), self.table[self.__hash(key)].index(key)

    def __str__(self):
        string = ""
        hash_value = 0
        for i in self.table:
            string = string + str(hash_value) + ": "
            for keyword in i:
                string = string + keyword + ", "
            string = string + "\n"
            hash_value += 1
        return string
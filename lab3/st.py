from hash_table import HashTable


class ST:
    def __init__(self, size):
        self.__hash_table = HashTable(size)

    def add(self, key):
        self.__hash_table.add(key)

    def remove(self, key):
        self.__hash_table.remove(key)

    def find(self, key):
        return self.__hash_table.find(key)

    def position(self, key):
        return self.__hash_table.position(key)

    def __str__(self):
        return str(self.__hash_table)


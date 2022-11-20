class PIF:
    def __init__(self):
        self.__pairs = []

    def insert_with_position(self, token, position):
        self.__pairs.append((token, position))

    def insert(self, token):
        self.__pairs.append((token, (-1, -1)))

    def __str__(self):
        text = "Token                      Position\n"
        for pair in self.__pairs:
            spaces = ""
            for i in range(10-len(pair[0])):
                spaces += " "
            text += pair[0] + spaces + "                 " + str(pair[1]) + "\n"
        return text

import re
from pif import PIF
from st import ST


def is_identifier(elem):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', elem) is not None


def is_constant(elem):
    return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', elem) is not None


class Scanner:
    def __init__(self, st: ST, pif: PIF):
        self.__st = st
        self.__pif = pif
        self.__exceptions = []
        self.__reserved_words = []
        self.__separators = []
        self.__operators = []
        self.initialise()

    def get_exceptions(self):
        return self.__exceptions

    def get_reserved_words(self):
        return self.__reserved_words

    def get_separators(self):
        return self.__separators

    def get_operators(self):
        return self.__operators

    def get_all_tokens_declared(self):
        return self.__reserved_words + self.__separators + self.__operators

    def is_operator(self, elem):
        if self.__operators.__contains__(elem):
            return True
        return False

    def initialise(self):
        with open('files/token.in', 'r') as f:
            line = " "
            while line != "/done/":
                line = f.readline().strip()
                if line == "space":
                    self.__separators.append(" ")
                self.__separators.append(line)
            line = " "
            while line != "/done/":
                line = f.readline().strip()
                self.__operators.append(line)
            line = " "
            while line != "/done/":
                line = f.readline().strip()
                self.__reserved_words.append(line)

    def scan(self, program_file):
        index = 1
        with open(program_file, 'r') as f:
            for line in f:
                tokens = self.get_line_tokens(line.strip())
                for i in range(len(tokens)):
                    current_token = tokens[i]
                    if current_token in self.get_all_tokens_declared() and current_token != ' ':
                        self.__pif.insert(current_token)
                    elif is_identifier(current_token):
                        self.__st.add(current_token)
                        self.__pif.insert_with_position(current_token, self.__st.position(current_token))
                    elif is_constant(current_token):
                        self.__st.add(current_token),
                        self.__pif.insert_with_position("const", self.__st.position(current_token))
                    else:
                        exception_string = str(len(self.__exceptions)+1) + ". " + current_token + " at line " + \
                                           str(index) + "."
                        self.__exceptions.append(exception_string)
                index += 1

    def get_line_tokens(self, line: str):
        for separator in self.__separators:
            if separator != " ":
                new_separator = " " + separator + " "
                line = line.replace(separator, new_separator)

        for operator in self.__operators:
            new_operator = " " + operator + " "
            line = line.replace(operator, new_operator)
        tokens = line.split()
        return tokens

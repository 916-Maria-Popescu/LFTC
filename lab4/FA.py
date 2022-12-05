class MyFA:

    def __init__(self):
        self.all_states = {}
        self.input_symbols = {}
        self.initial_states = {}
        self.final_states = {}
        self.transition_function = {}
        self.read_input_file()

    def read_input_file(self):
        with open("FA.in") as file:
            self.all_states = file.readline().strip().replace(" ", "")[12:-1].split(',')
            self.input_symbols = file.readline().strip().replace(" ", "")[15:-1].split(',')
            self.initial_states = file.readline().strip().replace(" ", "")[15:-1].split(',')
            self.final_states = file.readline().strip().replace(" ", "")[13:-1].split(',')

            file.readline()
            self.transition_function = {}
            for line in file:
                if line != '}' and len(line) > 0:
                    pair = line.strip().replace(" ", "").split('->')[0].strip()[1:-1].split(",")
                    origin = pair[0]
                    path = pair[1]
                    target = line.strip().replace(" ", "").split('->')[1].strip()

                    if (origin, path) in self.transition_function.keys():
                        self.transition_function[(origin, path)].append(target)
                    else:
                        self.transition_function[(origin, path)] = [target]

    def is_deterministic(self):
        for key in self.transition_function.keys():
            if len(self.transition_function[key]) > 1:
                return False
        return True

    def check_null(self):
        if self.initial_states in self.final_states:
            return True
        return False

    def is_accepted_by_fa(self, sequence):
        if self.is_deterministic():
            start = self.initial_states
            for c in sequence:
                print(self.transition_function)
                if (start, c) in self.transition_function.keys():
                    start = self.transition_function[(start, c)][0]
                else:
                    return False
            if start in self.final_states:
                return True

        return False

    def is_fa_valid(self):
        if self.initial_states not in self.all_states:
            return False
        for final in self.final_states:
            if final not in self.all_states:
                return False
        for (origin, path) in self.transition_function.keys():
            if origin not in self.all_states:
                return False
            if path not in self.input_symbols:
                return False
            for target in self.transition_function[(origin, path)]:
                if target not in self.all_states:
                    return False
        return True

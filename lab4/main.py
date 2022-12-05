from FA import MyFA

if __name__ == '__main__':
    fa = MyFA()

    while True:
        print("1: States")
        print("2: Alphabet")
        print("3: Transitions")
        print("4: Initial states")
        print("5: Final states")
        print("6: Check DFA")
        print("7: Accepted")
        print("8: Exit")

        option = input("Option: ")

        if option == "1":
            print('State = {' + ', '.join([str(x) for x in fa.all_states]) + '}')

        elif option == "2":
            print('Alphabet = {' + ', '.join([str(x) for x in fa.input_symbols]) + '}')

        elif option == "3":
            T = ""
            for (origin, path) in fa.transition_function.keys():
                T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(fa.transition_function[(origin, path)]) + "\n"
            print('T = {\n' + T + '}')

        elif option == "4":
            print("initial states = {" + str(fa.initial_states) + "}")

        elif option == "5":
            print('final states = {' + ', '.join([str(x) for x in fa.final_states]) + '}')

        elif option == "6":
            print(fa.is_deterministic())

        elif option == "7":
            if fa.is_deterministic():
                sequence = input("Input sequence: ")
                split_sequence = sequence.split(",")
                if len(split_sequence) == 1:
                    print(fa.check_null())
                else:
                    print(fa.is_accepted_by_fa(split_sequence))
            else:
                print("Not deterministic")

        elif option == "8":
            break
        else:
            print("option is not valid")



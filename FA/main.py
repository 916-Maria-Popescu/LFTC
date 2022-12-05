from FA import FA

if __name__ == '__main__':

    fa = FA("FA.in")

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
            print('Q = {' + ', '.join([str(x) for x in fa.Q]) + '}')

        elif option == "2":
            print('E = {' + ', '.join([str(x) for x in fa.E]) + '}')

        elif option == "3":
            T = ""
            for (origin, path) in fa.T.keys():
                T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(fa.T[(origin, path)]) + "\n"
            print('T = {\n' + T + '}')

        elif option == "4":
            print("q0 = {" + str(fa.q0) + "}")

        elif option == "5":
            print('F = {' + ', '.join([str(x) for x in fa.F]) + '}')

        elif option == "6":
            print(fa.is_dfa())

        elif option == "7":
            if fa.is_dfa():
                sequence = input("Input sequence: ")
                split_sequence = sequence.split(",")
                if len(split_sequence) == 1:
                    print(fa.check_if_null())
                else:
                    print(fa.is_accepted_by_fa(split_sequence))
            else:
                print("its not a dfa")

        elif option == "8":
            break
        else:
            print("option is not valid")
from pif import PIF
from scanner import Scanner
from st import ST

if __name__ == '__main__':
    st = ST(20)
    pif = PIF()
    scanner = Scanner(st, pif)

    program_file = "files/p1"
    pid_file = "files/PIF.out"
    st_file = "files/ST.out"

    scanner.scan(program_file)

    with open(pid_file, "w") as writer:
        writer.write(str(pif))

    with open(st_file, 'w') as writer:
        writer.write(str(st))

    if len(scanner.get_exceptions()) > 0:
        print("Lexical errors: ")
        for e in scanner.get_exceptions():
            print(e)
    else:
        print("No errors")

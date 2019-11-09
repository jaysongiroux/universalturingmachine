import engine.turingMachine as pos
from colorama import Fore

class assertion:
    def equals(expected, intial, message):
        if expected == intial:
            print(Fore.GREEN + "[PASS] " + message)
        else:
            print(Fore.RED + "[FAIL] " + message + ". received input: ", intial)
            return


tape = "[,>a,b,c,]"
assertion.equals("[,>a,b,c,]",pos.tapePadding(tape),"Testing tape padding in turingMachine.py")

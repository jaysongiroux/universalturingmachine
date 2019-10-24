from engine.turingMachine import position as pos
from engine.turingMachine import parseInput as parse
from engine.turingMachine import parseTape as tape
from colorama import Fore

class assertion:
    def equals(expected, intial, message):
        if expected == intial:
            print(Fore.GREEN + "[PASS] " + message)
        else:
            print(Fore.RED + "[FAIL] " + message + ". received input: ", intial)
            return


def positionTest():
    assertion.equals(1, pos("q1"),"input: 'q1' should equal '1'")
    assertion.equals(10, pos("q10"), "input: 'q1' should equal '1'")
    assertion.equals(None, pos("1"),"input: '1' should equal 'None'")

def parseTest():
    assertion.equals(['{', 'q1', 'a', 'q3', 'c', 'R', '}'],parse("{q1,a,q3,c,R}",","),"input: '{q1,a,q3,c,R}' should equal '['{', 'q1', 'a', 'q3', 'c', 'R', '}']'")

def parseTapeTest():
    assertion.equals(['[', ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'], ']'],tape("a,b,c,a,b,c,a,b,c"),"'a,b,c,a,b,c,a,b,c' should equal: '['[', ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'], ']']'")

positionTest()
parseTest()
parseTapeTest()

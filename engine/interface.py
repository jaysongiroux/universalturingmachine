import requests
import sys
import turingMachine as tm
import re

option = sys.argv[1]

# this is the script the javascript executes importing another python file for turing machines
def input(input):
    # x = re.search("{(.*)", option)
    x = tm.parseInput(input)
    return x


print(input(option))
sys.stdout.flush()


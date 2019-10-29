import requests
import sys
import turingMachine as tm
import re
import JSONConvert as con
import exampleEngine as ex
option = sys.argv[1]
example = sys.argv[2]

# this is the script the javascript executes importing another python file for turing machines
def input(input,exampleNum):
    if exampleNum != 0:
        ex.process(exampleNum)
    else:
        x = con.removebraces(input)
        name, currentState, read, goto, write, move = con.seperater(x)
        currentState = con.duplicate_states(currentState)
        obj = con.jsonObj(name, currentState, read, goto, write, move)
        con.creatJSON(obj)
    tape = tm.main()
    return tape

input(option,example)
sys.stdout.flush()

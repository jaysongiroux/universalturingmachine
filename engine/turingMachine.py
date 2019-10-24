import re
#####################
##  INPUT PARSING  ##
#####################
logger = []
# example:
# Input is "{q1,a,q3,c,R}"
# Output is "['{', 'q1', 'a','q3','c', 'R', '}']"
def parseInput(input,tape):
    global logger
    evaled = []
    tempString = "[INPUT] ", input
    logger.append(tempString)
    for i in range(len(input)):
        if input[i] == "{" or input[i] == "}":
            evaled.append(input[i])

        elif input[i] != "," and input[i+1] != ",":
            if input[i+1] == "}":
                evaled.append(input[i])
            else:
                evaled.append(input[i] + input[i+1])
        elif input[i] == "a" or input[i] == "v" or input[i] == "c" or input[i] == "R" or input[i] == "L" or input[i] == "Δ":
            evaled.append(input[i])
    tape = parseTape(tape)
    tempString = "[Parsed Input]: ", evaled
    logger.append(tempString)
    tempString = "[Parsed Tape]: ", tape
    logger.append(tempString)
    return evaled

# given tape: "a,b,c,d"
# output: ['[', ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
def parseTape(tape):
    tempString = tape.split(",")
    tempString = "[",tempString,"]"

    obj = []
    for i in tempString:
        obj.append(i)

    return obj


# determine the position from the Q value
# input "q1" output "1" for position 1 in the array
# can be changed the offset if needed
def position(a):
    offset = 0
    reg  = "[0-9]*"
    # if the unit contains "q"
    if "q" in a:
        x = re.findall(reg, a, flags=0)
        return int(x[1]) + offset
    else:
        return None



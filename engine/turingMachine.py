    #####################
    ##  INPUT PARSING  ##
    #####################
# example:
# Input is "{q1,a,q3,c,R}"
# Output is "['{', 'q1', 'q3', 'R', '}']"
def parseInput(input):
    logger = []
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
    tempString = "[Parsed Input]: ", evaled
    logger.append(tempString)
    return evaled

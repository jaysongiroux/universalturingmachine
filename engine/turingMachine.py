import json
import re
import time
import os
import encoding as encoding
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# defining variables
jsonFile = ROOT_DIR+"/data.json"
tapeFile = ROOT_DIR+"/tape.txt"
startingpos = 0
startingSymbol = ">"
startingPosOffset = 0

# read json file into obj file
def readJSON():
    with open(jsonFile) as json_file:
        data = json.load(json_file)
    return data

def readTape():
    f = open(tapeFile,"r")
    data = f.read().split(",")
    return data

def tapePadding(tape):
    spacePadding = []
    leftBounded = False
    rightBounded = False

    for i in range(73):
        spacePadding.append(" ")

#     check if tape is bounded
    for i in range(len(tape)):
        if "[" in tape[i]:
            leftBounded = True
        if "]" in tape[i]:
            rightBounded = True

    if leftBounded == True and rightBounded == True:
        return tape
    elif leftBounded == True and rightBounded == False:
        tape = tape + spacePadding
        return tape
    elif leftBounded == False and rightBounded == True:
        tape = spacePadding + tape
        return tape
    elif leftBounded == False and rightBounded == False:
        tape = spacePadding + tape + spacePadding
        return tape

def startingPosOnTape(t):
    global startingpos
    for i in range(len(t)):
        if startingSymbol in t[i]:
            startingpos = i+startingPosOffset
    cleanString = re.sub('>', '', t[startingpos])
    t[startingpos] = cleanString
    return t

def currentstate(trans,number):
    counter = 0
    states = []
    contains = "q"+str(number)
    jsonkeys = trans.keys()
    listKeys = []

    for keys in jsonkeys:
        listKeys.append(keys)
    # print("keys from json file: ",listKeys)
    print("checking if matching: ", contains)
    for i in range(len(listKeys)):
        if contains in listKeys[counter]:
            states.append(listKeys[counter])
        counter = counter+1
    return states


def whatToRead(states, transitions):
    toRead = []
    togo = []
    write = []
    move = []
    currentState = []

    for i in range(len(states)):
        currentState.append(transitions[states[i]]["state"])
        toRead.append(transitions[states[i]]["input"])
        togo.append(transitions[states[i]]["transition_to"])
        write.append(transitions[states[i]]["write"])
        move.append(transitions[states[i]]["move"])
    return currentState, toRead, togo, write, move

def getStates(a):
    cleanString = re.sub('\D', '', a)
    # print("clean string: ", cleanString)
    return int(cleanString)


def encode():
    print("-----------")
    l = encoding.main()
    for i in range(len(l)):
        print("Encoded State:",l[i])


def UTM(tape, transitions):
    counter = 1
    stateNum = 1
    whileBool = True
    while whileBool == True:
        statesToCheck = currentstate(transitions,stateNum)
        print("states to check", statesToCheck)
        currentstates, toRead, togo, write, move = whatToRead(statesToCheck,transitions)

        for i in range(len(toRead)):
            print("current Tape: ", tape)
            # haults if in q2
            if currentstates[i] in "q2":
                print("Final Tape: ", tape)
                print("In state q2 --> haulting")
                print("ACCEPTED")
                encode()
                exit()

            print("checking if tape: ", tape[startingpos + counter - 1], "==", toRead[i])

            if not tape[startingpos + counter - 1] in toRead:
                print("[STOPPED] Read: ", tape[startingpos + counter - 1], "expected these options: ", toRead)
                encode()
                exit()

            if tape[startingpos + counter - 1] == toRead[i]:
                print("matched! with tape: ",tape[startingpos + counter -1], "and to read: ", toRead[i])
                state = i
                #         writing to tape
                tape[startingpos + counter - 1] = write[state]
                print("Writing: ", write[state])
                stateNum = getStates(togo[state])

                #       movement:
                print("Current states: ", currentstates[i])

                if move[state] == "R":
                    print("Moving Right")
                    counter = counter + 1
                elif move[state] == "L":
                    print("Moving Left")
                    counter = counter - 1

                if tape[startingpos + counter - 1] == "]" and currentstates[i] in "q2":
                    print("Final Tape: ", tape)
                    print("in state q2 and finished")
                    print("ACCEPTED")
                    encode()
                    exit()
                if tape[startingpos + counter - 1] == "[" and currentstates[i] in "q2":
                    print("Final Tape: ", tape)
                    print("in state q2 and finished")
                    print("ACCEPTED")
                    encode()
                    exit()

                # hits bracket will on continue since it is bounded
                # if tape[startingpos + counter - 1] == "]":
                #     print("[STOPPED] hit bracket ]")
                #     print("[STOPPED] In state: ", currentstates[i])
                #     print("Tape: ", tape)
                #     encode()
                #     whileBool = False
                #     break
                # elif tape[startingpos + counter - 1] == "[":
                #     print("[STOPPED] hit bracket [")
                #     print("[STOPPED] In state: ", currentstates[i])
                #     print("Tape: ", tape)
                #     encode()
                #     whileBool = False
                #     break
                break
    return tape

def main():
    print("Starting Turing Machine")
    transitions = readJSON()
    tape = readTape()
    tape = tapePadding(tape)
    tape = startingPosOnTape(tape)
    tape = UTM(tape, transitions)
    return tape
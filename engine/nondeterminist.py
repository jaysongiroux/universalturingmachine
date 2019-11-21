# check if conflicting states
import json
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
jsonFile = ROOT_DIR+"/data.json"
deterministic = False


def read_json():
    with open(jsonFile) as json_file:
        data = json.load(json_file)
    return data


def whatToRead(transitions):
    states = []
    jsonKeys = transitions.keys()
    for keys in jsonKeys:
        states.append(keys)

    toRead = []
    togo = []
    write = []
    move = []
    currentState = []
    key = []

    for i in range(len(states)):
        key.append(states[i])
        currentState.append(transitions[states[i]]["state"])
        toRead.append(transitions[states[i]]["input"])
        togo.append(transitions[states[i]]["transition_to"])
        write.append(transitions[states[i]]["write"])
        move.append(transitions[states[i]]["move"])
    return currentState, toRead, togo, write, move


def checker(trans):
    tempA = []
    for i in range(len(trans[0])):
        tempA.append(transitions[0][i] + transitions[1][i])
    print(tempA)
    tempI = []
    tempX = []
    for i in range(len(tempA)):
        # goes through 3 times
        for x in range(len(tempA)):
            if tempA[i] == tempA[x] and x != i:
                print("MATCH - comparing:", tempA[i], tempA[x])
                tempI.append(i)
                tempX.append(x)

    print(tempX,tempI)
    for i in range(len(tempI)):
        print(transitions[0][tempI[i]],transitions[1][tempX[i]])
    obj = []
    for i in range(len(trans)):
        obj.append({
            "state": trans[0],
            "input": trans[1],
            "write": trans[3],
            "transition_to":trans[2],
            "move":trans[4]
        })
    print(obj)
    # for i in range(len(trans[1])):



# instead of changing the turing machine, lets approach this from a data processing point of view
# determine IF it is nondeterministic
# begin to create branches
# dump into folder with seperate json files
# run the turing machine through each file untill accepted


transitions = read_json()
print(whatToRead(transitions))
transitions = whatToRead(transitions)
print(transitions[0])
checker(transitions)

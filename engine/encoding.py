import json
import alphabet as alpha
import re
import os
import turingMachine as tm
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

jsonFile = ROOT_DIR+"/data.json"
# read json file into obj file
def readJSON():
    with open(jsonFile) as json_file:
        data = json.load(json_file)
    return data

def lengthJson(trans):
    return len(trans)

def getKeys(trans):
    a = []
    b = trans.keys()
    for i in b:
        a.append(i)
    return a

def numberbuilder(a):
    b = [1] * int(a)
    c = ''
    for i in range(len(b)):
        c +=str(b[i])
    return c

def encoding(trans):
    final = []
    states = getKeys(trans)
    currentState, toRead, togo, write, move = tm.whatToRead(states,trans)
#     get length of json file
    for i in range(len(states)):
        # q
        en = []
        en.append("1") # pushed for "q"
        en.append("0") # trailing 0
        temp = states[i]
        temp = re.sub('q','',temp)
        en.append(numberbuilder(temp[0])) #number following q
        en.append("0") #trailing 0

        # handels the dash and after the dash
        if "-" in states[i]:
            en.append(alpha.alphabet("-"))
            en.append("0") # trailing 0
            temp3 = re.search("-.*$",temp).group(0)
            temp3 = re.sub('-','',temp3)
            en.append(numberbuilder(temp3))
            en.append("0")

        en.append(alpha.alphabet(toRead[i]))
        en.append('0')
        en.append(alpha.alphabet('q'))
        en.append("0")
        temp = re.sub('q','',togo[i])
        en.append(numberbuilder(temp))
        en.append('0')
        en.append(alpha.alphabet(write[i].lower()))
        en.append('0')
        en.append(alpha.alphabet(move[i]))
        temp = ''.join(en)
        final.append({
            states[i]:temp
        })
    return final



def main():
    test = readJSON()
    return encoding(test)

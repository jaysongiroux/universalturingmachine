import json

# input  = q1,b,q2,c,R
# returns array
def string_to_array(x):
    a = x.split(",")
    return a

# seperates the array into catagories
def seperater(x):
    currentState = []
    read = []
    goto = []
    write = []
    move = []
    for i in range(len(x)):
        o = i * 5
        if i == len(x)/5:
            break
        currentState.append(x[o])
        read.append(x[o+1])
        goto.append(x[o+2])
        write.append(x[o+3])
        move.append(x[o+4])
    return currentState, read, goto, write, move

def jsonObj(current,read,goto,write,move):
    obj = []
    for i in range(len(current)):
        obj.append({
            current[i]:{
                "state":current[i],
                "input": read[i],
                "transition_to": goto[i],
                "write": write[i],
                "move": move[i]
            }
        })
    return obj

def duplicate_states(current):
    print(current)
    counter = 1
    for i in range(len(current)):
        if i == len(current) - 1:
            break
        if current[i] == current[i+1]:
            compare = current[i]
        if compare == current[i+1]:
            current[i+1] = str(current[i+1]) + "-" + str(counter)
            counter = counter + 1
        elif compare != current[i+1]:
            counter = 1
    return current


def creatJSON(obj):
    with open('data.json', 'w') as outfile:
        json.dump(obj, outfile, indent=2)



input = "q1,b,q2,c,R,q1,c,q3,b,L,q1,b,q2,c,R,q1,c,q3,b,L,q2,c,q3,b,L,q2,c,q3,b,L"
x = string_to_array(input)
currentState, read, goto, write, move = seperater(x)
currentState = duplicate_states(currentState)
print(x)
obj = jsonObj(currentState, read, goto, write, move)
creatJSON(obj)
import json

# input  = q1,b,q2,c,R
# returns array
def string_to_array(x):
    a = x.split(",")
    return a

# seperates the array into catagories
def seperater(x):
    name = []
    currentState = []
    read = []
    goto = []
    write = []
    move = []
    for i in range(len(x)):
        o = i * 5
        if i == len(x)/5:
            break
        name.append(x[o])
        currentState.append(x[o])
        read.append(x[o+1])
        goto.append(x[o+2])
        write.append(x[o+3])
        move.append(x[o+4])
    return name, currentState, read, goto, write, move

def jsonObj(name,current,read,goto,write,move):
    with open("data.json", 'w') as fp:
        fp.write("{"+"\n")
        for i in range(len(current)):
            fp.write("\""+currentState[i]+"\":{\n")
            fp.write("\"state\":\""+name[i]+"\",\n")
            fp.write("\"input\":\""+read[i]+"\",\n")
            fp.write("\"transition_to\":\""+goto[i]+"\",\n")
            fp.write("\"write\":\""+ write[i]+"\",\n")
            fp.write("\"move\":\""+ move[i]+"\"\n")
            if i == len(current)-1:
                fp.write("}" + "\n")
            else:
                fp.write("},"+"\n")
        fp.write("}"+"\n")

def duplicate_states(current):
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

# formats the json files after been written to by jsonobj method
def creatJSON(obj):
    data = 0
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
        print(data)
    with open("data.json", "w") as json_file:
        json.dump(data,json_file,indent=2)


input = "q1,b,q2,c,R,q1,c,q3,b,L,q1,b,q2,c,R,q1,c,q3,b,L,q2,c,q3,b,L,q2,c,q3,b,L"
x = string_to_array(input)
name, currentState, read, goto, write, move = seperater(x)
currentState = duplicate_states(currentState)
obj = jsonObj(name, currentState, read, goto, write, move)
print(obj)
creatJSON(obj)
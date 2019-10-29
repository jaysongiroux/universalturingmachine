import re

# input is going to be:
#  {a,b,c,d,e}{...}
current = []
ifseen = []
state = []
write = []
action = []
logger = []

def process_input(ing):
    global logger
    temp = []
    for i in range(len(ing)):
        if ing[i] != '{':
            if ing[i] != '}':
                temp.append(ing[i])
    # returns array without brackets
    tempLogger = 'process_input: ', temp
    logger.append(tempLogger)
    return temp

def seperate_input(ing):
    global current,ifseen,state,write,action
    # defining seperate arrays for types of actions in OBJ format
    lengthSelector = int(len(ing)/5)

    for i in range(lengthSelector):
        current.append(ing[i*5])
        ifseen.append(ing[i*5+1])
        state.append(ing[i*5+2])
        write.append(ing[i*5+3])
        action.append(ing[i*5+4])

# generates our tape
def processTape(tape):
    global logger
    a = tape.split(',')
    temp = 'processTape: ', a
    logger.append(temp)
    return a

def position(a):
    global logger
    offset = 0
    reg  = "[0-9]*"
    # if the unit contains "q"
    if "q" in a:
        x = re.findall(reg, a, flags=0)
        return int(x[1]) + offset
    else:
        return None

def main(trans, tape):
    seperate_input(process_input(trans))
    tape = processTape(tape)
    print('Current:', current)
    print('ifSeen: ', ifseen)
    print('state: ', state)
    print('Write', write)
    print('action', action)
    print('tape', tape)
    counter = 0
    #define starting point which is q0
    # loop through using i as a counter
    # length of the array = number of transitions
    while True:
        currentPosition = position(current[counter])
        print('current position', currentPosition)
        tapePosition = tape[currentPosition]
        print('tape position: ',tapePosition)
        currentIfSeen = ifseen[counter]
        print('current if seen: ',currentIfSeen)
        currentWrite = write[counter]
        currentAction = action[counter]

        # writes to the tape
        if currentIfSeen == tapePosition:
            tape[counter] = currentWrite
            print("changing: ",currentIfSeen," to: ", currentWrite)
        else:
            print("HAULING STATE")
            print("Final Tape: ", tape)
            return False

        # What to do when seeing an R or L
        if currentAction == 'R':
            print('moving right...')
            counter = counter + 1
        elif currentAction == 'L':
            print('moving left...')
            counter = counter - 1

        # what to do when seeing the arrows


        # what to do when seeing brackets


        # determine when it is the final state
        # TODO: should this be 1 or 2 since accepting state is q2?
        if currentPosition == 2 and counter == len(current):
            # todo: unclear to me if it lands on q2 it passes or if q2 needs to equal something in order to pass
            print("Final Tape: ", tape)
            print("Counter: ", counter, " Current Position: ", currentPosition)
            print("FINAL POSITION WAS Q2 WITH VALUE: ", tape[currentPosition])
            return True

            # determine if haulting state by determining if the counter exceeds the length of the tape
        if counter >= len(current):
            print("False, does not finish on q2")
            break


    print('final tape: ', tape)

# for debugging purposes only. called from UI.
trans = ['{', 'q0', 'a', 'q1', 'b', 'R', '}', '{', 'q1', 'b', 'q2', 'c', 'R', '}','{', 'q2', 'c', 'q2', 'b', 'R', '}']
tape = "a,b,c,a,b,c,a,b,c,a,b,c"
main(trans, tape)




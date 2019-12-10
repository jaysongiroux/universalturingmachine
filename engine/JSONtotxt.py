import json
import os
import re
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

FILE = "/examples/6.json"
# REPLACE "<<FILE>>" WITH THE JSON FILE YOU WOULD LIKE TO CONVERT
def readJSON():
    with open(ROOT_DIR + FILE, "r+") as json_file:
        data = json.load(json_file)
    return data

data = readJSON()
keys = data.keys()
a = []
for key in keys:
    a.append(key)


# state, read, goto, write, movement
txtString = []
for i in range(len(data)):
    tempString = "{" + data[a[i]]["state"] + ","+ data[a[i]]["input"] + "," + data[a[i]]["transition_to"] + "," + data[a[i]]["write"] + "," + data[
        a[i]]["move"] + "}"
    if i != len(data)-1:
        tempString=tempString+","
    txtString.append(tempString)

str1 = ""
for i in txtString:
    str1 += i

print(str1)


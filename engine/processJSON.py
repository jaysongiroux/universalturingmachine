import json
# reading the json file

def readJSON(fileName):
    with open(fileName) as json_file:
        obj = json.load(json_file)
    return obj

data = readJSON("data.json")
print(data[{"q1"}])
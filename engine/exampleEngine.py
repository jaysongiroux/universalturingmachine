# this will be used if the user chooses an example in the GUI drop down
import json
import os
import re
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def process(exampleNum):
    tempString = ROOT_DIR+"/examples/"+str(exampleNum)+".json"

    # if no example is choosen
    if exampleNum == 0:
        return False

    # copy data from example json files to main data.json file
    with open(tempString,"r") as json_file:
        data = json.load(json_file)

    with open(ROOT_DIR+"/data.json","w+")as json_file:
        json.dump(data,json_file,indent=2)

import requests
from bs4 import BeautifulSoup as bs
import sys

option = sys.argv[1]

# parsing input for backend
def input(input):
    a = ["line 1","\nline 2","\nline 3","\nthis is from the python backend"]
    return a



print(input(option))
sys.stdout.flush()

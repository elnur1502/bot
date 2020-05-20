import requests
from bs4 import BeautifulSoup
f = open("skidki.html", "r")
x = 0
for line in f:
    if x == 1:
        print(line.split()[3])
    x += 1

f.close()

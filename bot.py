import requests
from bs4 import BeautifulSoup

=open("skidki.html","r+")
s=(f.read())
soup = BeautifulSoup(html, 'lxml')
line = s.find('tbody').find_all('tr')
print(a)   #(если у вас в файле дание через пробел топишем  пробел, через точку-точку)
f.close()

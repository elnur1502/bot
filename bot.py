f=open("skidki.html","r+")
s=(f.read())
a=s.split(',')#вместо запятой может бить точка, любой символ
print(a)   #(если у вас в файле дание через пробел топишем  пробел, через точку-точку)
f.close()

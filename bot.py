import re

  
# инициализирующая строка

test_string = "There are 2.5 apples for 4,6 persons"

  
# печать оригинальной строки

print("The original string : " + test_string)

  
# используя re.findall ()
# получение чисел из строки

temp = re.findall(r'\d+', test_string)

res = list(map(int, temp))

  
# результат печати

print("The numbers list is : " + str(res))

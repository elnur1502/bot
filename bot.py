b = 1.6
a = 2.05
while a >= 1.5:
    a -= 0.05
    if a > b:
        print(round(a*2, 1))
    else:
        print('')

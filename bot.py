b = 1.6
a = 2
while a >= 1.5:
    a -= 0.05
    if a > b:
        print(round(a*2))
    else:
        print('')

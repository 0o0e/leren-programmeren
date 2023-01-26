antw = int(input('hoe vaak? '))

def fibionacci(antw):
    print(0)
    variab , variab2 = 0 , 1
    print(variab2)

    for i in range(antw):
        antwo = variab2 + variab
        variab = variab2
        variab2 = antwo
        print(antwo)

fibionacci(antw)

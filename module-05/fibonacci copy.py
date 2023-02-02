antw = int(input('hoe vaak? '))
def fibionacci(int):
    list = []
    variab , variab2 = 0 , 1
    list.append(variab)
    list.append(variab2)
    for i in range(antw - 2):
        antwo = variab2 + variab
        variab = variab2
        variab2 = antwo
        list.append(antwo)
    return list


print(fibionacci(antw))


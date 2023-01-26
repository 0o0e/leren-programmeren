antw = int(input('hoe vaak? '))

def fibionacci(antw):
    if antw <= 1:
        return antw
    else:
        return (fibionacci(antw -1) + fibionacci(antw -2))
if antw < 0:
    print('alleen getallen boven 0 ')
else:
    for i in range(antw):
        print(fibionacci(i))
    


fibionacci(antw)
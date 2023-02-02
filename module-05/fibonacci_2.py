antw = int(input('hoe vaak? '))

def fibionacci(hoeveel):
    if hoeveel <= 1:
        return hoeveel
    else:
        return (fibionacci(hoeveel -1) + fibionacci(hoeveel -2))
if antw < 0:
    print('alleen getallen boven 0 ')
else:
    for i in range(antw):
        print(fibionacci(i))
    


fibionacci(antw)
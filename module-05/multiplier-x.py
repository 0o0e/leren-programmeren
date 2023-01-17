getal = int(input('van welk getal wilt u de tafel zien? '))

def multiplier(nummer:int=getal):
    for i in range(1,11):
        antw = i * nummer
        print(f'{i} * {nummer} = {antw} ')


multiplier()
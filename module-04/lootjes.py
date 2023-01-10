import random

waarofnietwaar = True

namen = []
naam = {}
nieuwelijst = []


aantal= int(input('Hoeveel deelnemers zijn er? '))
while aantal < 3:
    print('minimaal 3 namen')
    aantal= int(input('Hoeveel deelnemers zijn er? '))

teller = 1
while teller <= aantal:
    name = input(f'wat is de naam van deelnemer {teller}: ')
    if name.lower() in namen:
        print('alleen unieke namen ')
    else:
        namen.append(name)
        nieuwelijst.append(name)
        teller +=1

tellen = 0
for i in (namen):
    random_naam = random.choice(nieuwelijst)
    if len(nieuwelijst) == 1 and random_naam == i:
        nieuwelijst.clear()
        for namn in namen:
            nieuwelijst.append(namn)
            print(f'newlist = {nieuwelijst}')
        for i in namen:
            random_naam = random.choice(nieuwelijst)
            while i == random_naam:
                random_naam = random.choice(nieuwelijst)
            naam[i] = random_naam
            nieuwelijst.remove(random_naam)
    else:
        while i == random_naam:
            random_naam = random.choice(nieuwelijst)
        else:
            naam[i] = random_naam
            nieuwelijst.remove(random_naam)
print(naam)

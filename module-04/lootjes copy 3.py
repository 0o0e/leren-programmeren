import random


123 #int
'abc' #string
namen = [] #lijst
naam = {} # dictionary
nieuwelijst = [] #lijst

# aantal deelnemers
aantal= int(input('Hoeveel deelnemers zijn er? '))
while aantal < 3:
    print('minimaal 3 namen')
    aantal= int(input('Hoeveel deelnemers zijn er? '))

teller = 1
while len(namen) < aantal:
    name = input(f'wat is de naam van deelnemer {len(namen)+1}: ')
    if name.lower() in namen:
        print('alleen unieke namen ')
    else:
        namen.append(name)
        nieuwelijst.append(name)
        teller +=1
# 


tellen = 0
ok = False
while not ok:
    for i in namen:
        random_naam = random.choice(nieuwelijst)
        if len(nieuwelijst) == 1 and random_naam == i:
            nieuwelijst.clear()
            naam.clear()
            for namn in namen:
                nieuwelijst.append(namn)
            # ok = False
        else:
            # random_naam = random.choice(nieuwelijst)
            while random_naam == i:
                random_naam = random.choice(nieuwelijst)
            naam[i] = random_naam
            nieuwelijst.remove(random_naam)
    if len(nieuwelijst) == 0:
        ok = True
print(naam)

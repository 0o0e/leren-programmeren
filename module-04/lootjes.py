import random




namen = []
naam = {}
nieuwelijst = []

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

tellen = 0
ok = False
while not ok:
    random_naam = random.choice(nieuwelijst)
    if len(nieuwelijst) == 1 and random_naam == i:
        nieuwelijst.clear()
        for namn in namen:
            nieuwelijst.append(namn)
        ok =False
        print('false')
    else:
        for i in namen:
            random_naam = random.choice(nieuwelijst)
            while i == random_naam:
                random_naam = random.choice(nieuwelijst)
            else:
                naam[i] = random_naam
                nieuwelijst.remove(random_naam)
            while random_naam == i:
                nieuwelijst.clear()
                for namn in namen:
                    nieuwelijst.append(namn)
                ok =False
            else:
                ok = True

print(naam)

import random

waar = True

namen = []
naam = {}
nieuwelijst = []
teller = 3
while waar == True:
    name = input(f'noem een naam : ')
    if name.lower() in namen:
        print('alleen unieke namen')
    else:
        namen.append(name)
        nieuwelijst.append(name)
        teller -= 1
    if len(namen) < 3:
        print(f'nog minimaal {teller} namen')
    if len(namen) >= 3:
        meer = input('wil je meer namen toevoegen? (ja/nee) ').lower()
        if meer != 'ja':
            waar = False

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
            else:
                naam[i] = random_naam
                nieuwelijst.remove(random_naam)
    else:
        while i == random_naam:
            random_naam = random.choice(nieuwelijst)
        else:
            naam[i] = random_naam
            nieuwelijst.remove(random_naam)

print(naam)

import random

# voor aantal deelnemers:
VRAAG = 'Wat is de aantal van de deelnemers? '
aantal = int(input(VRAAG))
while aantal < 3:
    print('Aantal deelnemers moet 3 of meer zijn.')
    aantal = int(input(VRAAG))

# voor namen van deelnemers:
namen_list= []
newList = []
lootjes ={}

teller = 1 
while teller <= aantal:
    naam= input(f'wat is de naam van deelnemers {teller}?   ')
    if naam.lower() in namen_list:
        print('Mag alleen unieke namen! Probeer nog een keer.')
    else:
        namen_list.append(naam.lower())
        newList.append(naam.lower())
        teller +=1


# voor lootjes trekken:
for deelnemer in namen_list:
    keuze= random.choice(newList)
    if len(newList) == 1 and keuze == deelnemer:
        newList.clear()
        for namen in namen_list:
            newList.append(namen)
        for deelnemer in namen_list:
            keuze= random.choice(newList)
            while deelnemer == keuze:
                keuze = random.choice(newList)
            lootjes[deelnemer] = keuze
            newList.remove(keuze)
    else:
        while deelnemer == keuze:
            keuze = random.choice(newList)
        lootjes[deelnemer] = keuze
        newList.remove(keuze)

print(lootjes)
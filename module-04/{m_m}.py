import random
kleuren = ['rood','blauw','groen','geel','bruin']

hoeveel_toevoegen = int(input('Hoeveel mnms wil je toevoegen? '))

values = []
zak = {}

for i in range(len(kleuren) - 1):
    nummer = random.randint(0,hoeveel_toevoegen) # value nummer word random int
    values.append(nummer) # de nummer word toegevoegt aan values list
    hoeveel_toevoegen -= nummer # hoeveel_toevoegen word verminderd met 1, dus de volgende nummer word gekozen tussen 0 en de nieuwe hoeveel_toevoegen
values.append(hoeveel_toevoegen)# hoeveel_toevoegen word toegevoegt aan values list (alles at over is)
 

for kleur in kleuren: 
    for nummer in values: 
        zak[kleur] = nummer # kleur in kleuren is nummer in values  en toegevoegd aan zak
        values.remove(nummer) # random nummer word verwijdrd uit values
        break
    if zak[kleur] == 0:
        del zak[kleur] # als een kleur de value 0 heeft word het verwijerd
print(zak)




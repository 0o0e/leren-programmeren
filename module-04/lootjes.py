import random

waar = True
namen = []
hoeveel = int(input('Hoeveel namen wil je toevoegen? '))
while waar == True:
    welkekleur = input(f'noem een naam(minstens 3): ')
    namen.append(welkekleur) 
    print(namen)
    if len(namen) < 3:
        print('minstens 3 namen')
    print(len(namen))
    if len(namen) >= 3:
        meer = input('wil je meer namen toevoegen? ')
        if meer == 'nee':
            waar = False
print(namen)

# naam = {}
# teller = 0
# for i in range (hoeveel):
#     random_naam = random.choice(namen)
#     if random_naam == namen[teller]:
#         while random_naam == namen[teller]:
#             random_naam = random.choice(namen)
#     else:
#         naam.update({namen[teller] : random_naam})
#         namen.remove(random_naam)
#         teller += 1
# print(naam)
naam = {}
teller = 0

aa = True
while aa == True:
    random_naam = random.choice(namen)
    print(namen[teller])
    if random_naam == namen[teller] or random_naam in naam:
        while random_naam == namen[teller]:
            random_naam = random.choice(namen)
    else:
        naam.update({namen[teller] : random_naam})
        namen.remove(random_naam)
        teller += 1
        print(naam)
    if len(naam) == 3:
        aa =False

print(naam)
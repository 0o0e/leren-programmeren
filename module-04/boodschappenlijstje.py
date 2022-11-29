# lijst = {}
# boodschappenlijst = []
# values = []
# meer_toevoegen = 'ja'
# while meer_toevoegen == 'ja':
#     item_toevoegen = input('Voeg een item toe: ').lower()
#     hoeveelkeer= int(input('Hoeveel keer wil je deze item: '))
#     values.append(hoeveelkeer)
#     boodschappenlijst.append(item_toevoegen)
#     for lijstje in boodschappenlijst:
#         for hoeveelkeer in values:
#             lijst[lijstje] = hoeveelkeer
#         boodschappenlijst.remove(item_toevoegen)
#     print(lijst)
#     meer_toevoegen = input('Wil je meer dingen toevoegen? ')
# print(f"""boodschappenlijst: {lijst} """)

lijst = {}
meer_toevoegen = 'ja'
while meer_toevoegen == 'ja':
    item_toevoegen = input('Voeg een item toe: ').lower()
    hoeveelkeer= int(input('Hoeveel keer wil je deze item: '))
    if item_toevoegen in lijst:
        lijst[item_toevoegen] += hoeveelkeer
    else:
        lijst[item_toevoegen] = hoeveelkeer

    meer_toevoegen = input('Wil je meer dingen toevoegen? ')
print(f"""boodschappenlijst: {lijst} """)
import random


colors = ['harten','klaveren','schoppen','ruiten']
values = [2,3,4,5,6,7,8,9,10,'boer','vrouw','heer','aas']
jokers = ['joker']
deck = []
for color in colors:
    for value in values:
        deck.append((color,value,))
for jokers_toevoegen in range(2):
    deck.append((jokers))

# teller = 1
random.shuffle(deck)
print(deck)

# for gekozen_kaarten in range(7):
#     choice =random.choice(deck)
#     print(f'kaart {teller} {choice}')
#     deck.remove(choice)
#     teller += 1
# print(f'deck {len(deck)} kaarten: , {deck}')
kaartnumr = 1
for i in range(7):
    print(f'kaart {kaartnumr} {deck[0]}')
    deck.pop(0)
    kaartnumr+=1
print(deck)
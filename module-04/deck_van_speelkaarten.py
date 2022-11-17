import random


colors = ['harten','klaveren','schoppen','ruiten']
values = [2,3,4,5,6,7,8,9,10,'boer','vrouw','heer','aas']
jokers = ['joker']
deck = []
for color in colors:
    for value in values:
        deck.append((color,value,))
for i in range(2):
    deck.append((jokers))

teller = 1
random.shuffle(deck)
for i in range(7):
    choice =random.choice(deck)
    print(f'kaart {teller} {choice}')
    deck.remove(choice)
    teller += 1
print(f'deck {len(deck)} kaarten: , {deck}')



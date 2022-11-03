import random, sys
punten = 0
score = 0
ronde = 0
vraag = input('Wil je de spel spelen? ')
if vraag != 'ja':
    print('oke')
    sys.exit

while ronde < 20 and vraag == 'ja':
    getal = random.randint(1,1000)
    punten = 0
    while vraag == 'ja':
        raad = int(input('Raad het getal: '))
        punten += 1
        diff = abs(getal - raad)
        if raad < getal:
            print('hoger')
        if raad > getal:
            print('lager')
        if diff <= 50 and diff >= 20 and getal != raad:
            print('je bent warm')
        if diff <= 20 and getal != raad:
            print('je bent heel warm')
        if getal == raad:
            break
        if punten == 10:
            break
    if getal == raad: 
        score += 1
        ronde += 1
        print(f'Je hebt het getal geraden! Dit was ronde {ronde}. Je score is {score}.')
        vraag = input('Wil je nog een ronde spelen? ')
        punten == 0
        if vraag != 'ja':
            print(f'je score is {score}. het spel eindigt nu.')
            break 
    if punten == 10:
        ronde += 1
        if ronde != 20:
            print(f'Je hebt het nummer niet geraden. Het nummer was {getal}. ')
            print(f'Dit was ronde {ronde}. Je score is {score}.')
            vraag = input('Wil je nog een ronde spelen? ')
            punten = 0
        if vraag != 'ja':
            print(f'je score is {score}. het spel eindigt nu.')
            break
        if ronde == 20:
            print(f'Dit was de laatste ronde. je score is {score}')
            break

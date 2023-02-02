import random, sys
MAXRONDES = 2
punten = 0
score = 0
ronde = 0
vraag = input('Wil je de spel spelen? ')
if vraag != 'ja':
    print('oke')
    sys.exit

while ronde < MAXRONDES and vraag == 'ja':
    getal = random.randint(1,1000)
    punten = 0
    geraden = False
    while punten < 10 and geraden == False : #zolang niet geraden en het aantal pogingen kleiner dan 10
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
            geraden = True
    ronde += 1
    punten == 0
    if geraden:
        score += 1
        print(f'Je hebt het getal geraden! Je score is {score}.')
    else:
        print(f'Je hebt het nummer niet geraden. Het nummer was {getal}. ')
    if ronde == MAXRONDES:
        print(f'Dit was de laatste ronde.')
    else:
        print(f'Dit was ronde {ronde}.')
        vraag = input('Wil je nog een ronde spelen? ')

print(f'je eindscore is {score}. het spel eindigt nu.')           
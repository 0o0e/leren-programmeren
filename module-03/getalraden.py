import random

# while getal != raad:


raad = 0

punten = 0
score = 0
ronde = 0
vraag = 'ja'

getal = random.randint(1,1000)
print(getal)
while vraag == 'ja':
    raad = int(input('Raad het getal: '))
    diff = abs(getal - raad)
    if punten == 10:
        break
    if raad < getal:
        print('hoger')
    if raad > getal:
        print('lager')
    if diff <= 50 and diff >= 20:
        print('je bent warm')
    if diff <= 20:
        print('je bent heel warm')
    punten = punten + 1
    if getal == raad:
        score = score + 1
        ronde = ronde + 1
        print(f'Dit was ronde {ronde}. Je score is {score}.')
        vraag = input('Wil je nog een ronde spelen? ')
    if punten == 10:
        ronde = ronde + 1
        print(f'Dit was ronde {ronde}. Je score is {score}.')
        vraag = input('Wil je nog een ronde spelen? ')
        


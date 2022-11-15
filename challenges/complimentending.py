import random

naam = input('Wat is je naam? ')
hoeveel = int(input(f'Hoeveel complimenten wil je, {naam}? '))
complimenten = ['geweldig','super','mooi','slim','lang']

vorigekans = ''
for i in range(hoeveel):
    rando = random.choice(complimenten)
    while rando == vorigekans:
        rando = random.choice(complimenten)
    print(f'{naam} je bent {rando}.')
    vorigekans = rando
    
from fruitmand import fruitmand
import random
aantal = int(input('Hoeveel keer? '))

for fruit in range(0,aantal):
    randm_fruit = random.choice(fruitmand)
    print(randm_fruit['name'])

from fruitmand import fruitmand
import random
aantal = int(input('Hoeveel keer? '))

for i in range(0,aantal):
    randm_in = random.choice(fruitmand)
    print(randm_in['name'])

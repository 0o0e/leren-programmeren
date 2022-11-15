import random
kleuren = ('oranje','blauw','groen','bruin')
hoeveel = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))
zakmetmnms = [random.choice(kleuren) for x in range(hoeveel)]
print(zakmetmnms)
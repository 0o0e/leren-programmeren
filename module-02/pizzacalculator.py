#esma kilic
from timeit import repeat


print('pizzakeuzes: small, medium, large')

small = int (5)
medium = int (10)
large = int (15)

try:
  aantalsmall = int(input(f"hoeveel small pizza's wil je? "))
  aantalmedium = int(input(f"hoeveel medium pizza's wil je? "))
  aantallarge = int(input(f"hoeveel large pizza's wil je? "))
except: 
    print('je kan alleen hele getallen invoeren.')
    aantalsmall = int(input(f"hoeveel small pizza's wil je? "))
    aantalmedium = int(input(f"hoeveel medium pizza's wil je? "))
    aantallarge = int(input(f"hoeveel large pizza's wil je? "))


small_prijs = small * aantalsmall
medium_prijs = medium * aantalmedium
large_prijs = large * aantallarge

totaalprijs = small_prijs + medium_prijs + large_prijs

print("""aantal pizza's:"""
,aantalsmall ,"""small pizza's,"""
,aantalmedium ,"""medium pizza's en"""
,aantallarge ,"""large pizza's""")
print("de totaalprijs is",totaalprijs, "euro")
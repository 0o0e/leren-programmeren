#esma kilic

print('pizzakeuzes: small, medium, large')

small = int (5)
medium = int (10)
large = int (15)

aantalsmall = int(input("hoeveel small pizza's wil je? "))
aantalmedium = int(input("hoeveel medium pizza's wil je? "))
aantallarge = int(input("hoeveel large pizza's wil je? "))

small_prijs = small * aantalsmall
medium_prijs = medium * aantalmedium
large_prijs = large * aantallarge

totaalprijs = small_prijs + medium_prijs + large_prijs

print("""aantal pizza's:"""
,aantalsmall ,"""small pizza's,"""
,aantalmedium ,"""medium pizza's en"""
,aantallarge ,"""large pizza's""")
print("de totaalprijs is",totaalprijs, "euro")
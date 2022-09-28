#esma kilic



print('pizzakeuzes: small, medium, large')

small = int (5)
medium = int (10)
large = int (15)

print('small pizza 5 euro, medium pizza 10 euro, large pizza 15 euro')


while True:
  try:
    smallpizza = int(input('hoeveel small pizzas? '))
    break
  except ValueError: 
    print('Alleen hele nummers invoeren. ')

while True:
  try:
    mediumpizza = int(input('hoeveel medium pizzas? '))
    break
  except ValueError:
    print('Alleen hele nummers invoeren. ')

while True:
  try:
    largepizza = int(input('hoeveel large pizzas? '))
    break
  except ValueError:
    print('Alleen hele nummers invoeren. ')



small_prijs = small * smallpizza
medium_prijs = medium * mediumpizza
large_prijs = large * largepizza

totaalprijs = small_prijs + medium_prijs + large_prijs

print(f"aantal pizza's: {smallpizza} small pizza's, {mediumpizza} medium pizza's en {largepizza} large pizza's")
print("de totaalprijs is",totaalprijs, "euro")
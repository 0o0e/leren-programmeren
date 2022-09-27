import random


name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteSeason = input(f'Wat is jouw favorite seizoen {name}? A) Lente, B) Zomer, C) Herfst of D) Winter ').lower()
answer = favoriteSeason

if answer == 'a':
 print("Ik hou ook van de lente!")
elif answer == 'b':
 print("De zomer is voor mij te warm.")
elif answer == 'c':
 print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'd':
 print("Is de winter niet erg koud?")
else:
 print("Die ken ik niet...")

favoriteoclor = input('En wat is je favoriete kleur? ') 
trueOrFalse = int(random.randint(0,5))
if True:
   print('Ik vind dat ook een mooie kleur!')
if not False:
   print(f'TBH, ik hou niet zo van {favoriteoclor}...')


num1 = random.randint(1,10)
num2 = random.randint(5,15)

try:
   number = int(input(f"En weet jij wat {num1} - {num2} is?"))
except:
    print('Nee dat klopt niet {}'.format(name))
if int(number == num1-num2):
   print('Dat is juist')
else:
   print('Dat is geen nummer!')
   
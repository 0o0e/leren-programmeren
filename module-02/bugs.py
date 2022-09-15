import random
name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteseason = input ('Wat is jouw favorite seizoen ' + name +'? A) Lente, B) Zomer, C) Herfst of D) Winter ')
answer = favoriteseason

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

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = str(random.randint(0,5))
if True:
  print('Ik vind dat ook een mooie kleur!')
if not False:
  print('TBH, ik hou niet zo van {}...'.format(favoriteColor))

num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

try:
   number = int(input(f"En weet jij wat  {num1}  -  {num2}  is? "))
except:
  print('Nee dat klopt niet {}'.format(name))
if int(num1 - num2 == number):
   print('Dat is juist')
else:
   print('Dat is geen nummer!')


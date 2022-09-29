gewicht = int(input('vraag '))

heeft_gewicht = gewicht >= 90

print(heeft_gewicht)
import os, sys, time, string
import string, time, sys

age = int(input ('how old are u? '))
heeft_age = age >=18

length = int(input('how long are you? (in cm) '))
heeft_lengte = length >= 160

weight= int(input('how much do you weigh? (in kg) '))
heeft_weight = weight <= 55


fitforit = heeft_age and heeft_lengte and heeft_weight

if fitforit:
    print('Congratulations, you are fit to work with us! please leave your contact information.')
else:
    print('Sory, you did not pass the online interview. ')
if fitforit:
  contact = input('emailadress: ')
  tel = input('phone-number: ')
  print('We will soon contact you soon ')


os.system('cls')

def typewriter(string):
  for char in string:
    sys.stdout.write(char)
    if char == '.':
      time.sleep('1')


typewriter('jfhutjhkojbh')



ervaring_jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? ')) #5
ervaring_dieren = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ')) #4
ervaring_acrobatiek = int(input('Hoeveel jaar prakttijkervaring heeft u met acrobatiek? ')) #3
mbo = input('Bent u in bezit van een MBO 4 diploma ondernemen? (ja/nee) ')
rijbewijs = input('Bent u in bezit van een vrachtwagen rijbewijs? (ja/nee) ')
hoed = input('Bent u in bezit van een hoge hoed? (ja/nee) ')
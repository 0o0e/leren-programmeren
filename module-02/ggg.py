

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
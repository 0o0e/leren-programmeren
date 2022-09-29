import random, sys

numb1 = random.randint(1,10)
numb2 = random.randint(1,10)
invitation = input('do you accept it? ')
if invitation in ('no', 'NO', 'n'):
    sys.exit()
if invitation in('yes', 'YES', 'y'):
    print('The game will start in another world. to teleport to this world solve the quiz.\n\
')

while True:
  try: 
    quiz = int(input(f'What is the anwser to {numb1} * {numb2}? '))
    if int(numb1 * numb2 != quiz):
     print('That is wrong.')
    if int(numb1 * numb2 == quiz):
     break
  except ValueError: 
    print('Alleen hele nummers invoeren. ')

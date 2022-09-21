from operator import contains
import sys, time, os, string, random

os.system('cls')
def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.03)
        else:
            time.sleep(1)


zin1= "You wake up in a bus. Suddenly an explosion is heard. A bright light flashed from the front of the bus. Than a monster-like creature appeared. \n\
"
wakeup = input("Do you want to wake up? (yes/no) ").lower()

if wakeup == 'yes':
    typewriter(zin1)
else:
    typewriter('keep sleeping')
    sys.exit()


first_choice = input('What do you want to do? [a. Try to kill the monster] [b. Run] ').lower()
dead_1 = "You are too weak. You died. "
live_1 = "You run to the back of the bus. The monster is still in your sight, but too far to hurt you. "

if first_choice == 'b':
    typewriter(live_1)
elif first_choice == 'a':
    typewriter(dead_1)
    sys.exit()
else:
    sys.exit()
    

zin2 = "The monster starts talking\n\
'The game will start soon.'\n\
The monster continued talking.\n\
'Some of you are invited for the game.'\n\
. . .\n\
'your invitation will arive at any moment'\n\
"
typewriter(zin2)

name = input('What is your name? ')
invitation = input(f'Dear {name},\n\
you are invited to participate in the game. do you accept the invitation? (yes/no) ').lower()

numb1 = int(random.randint(1,10))
numb2 = int(random.randint(1,10))

if invitation =='no':
    sys.exit()
if invitation =='yes':
    typewriter('The game will start in another world. to teleport to this world solve the quiz.\n\
')
    quiz = int(input(f'What is the anwser to {numb1} * {numb2}? '))
    if int (numb1 * numb2 == quiz):
        typewriter('That is correct. You will teleport to another world in a few seconds.\n\
')
    if int(numb1 * numb2 != quiz):
        typewriter('That is wrong.')
        sys.exit()

typewriter('. . . \n\
')
typewriter('You are now in another world to continue the game. choose a weapon to continue.\n\
')

weapon = input('choose one from the following: hammer, sword, magic book or spear. ')

typewriter(f'congrats! you are now in possession of a {weapon}\n\
')
typewriter('You can use this weapon to defeat the monster. but first you have to level up your weapon by playing games. \n\
')

typewriter("""<The first game will start now.>
The game is simple.
You have to guess the color based on the information given.\n\
""")

weaponlevel = int('1')
coins = int('0')

color_list = ['blue', 'red','green']
color = random.choice(color_list)

if color == 'red':
    typewriter('The color of blood. ')
    guessred = input('What color do you think it is? ').lower()
    if guessred == 'red':
        weaponlevel = int('2')
        coins = int(coins + 100)
        typewriter(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your weapon has to be level 6.
You earned 100 coins.
Current amount of coins = 100
\n\
""")
    else:
        typewriter("Wrong answer. your weapon won't level up this round. Your weapon is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 6.\n\
")
        weaponlevel = int('1')
        coins = int(coins)

elif color == 'blue':
    typewriter('The color is seen a lot outside when you look up. its also seen when you look in water. ')
    guessblue = input('what color do you think it is? ').lower()
    if guessblue == 'blue':
        weaponlevel = int('2')
        coins = int(coins + 100)
        typewriter(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your weapon has to be level 5.
You earned 100 coins.
Current amount of coins = 100
\n\
""")
    else:
        typewriter("Wrong answer. your weapon won't level up this round. Your weapon is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 7.\n\
")
        weaponlevel = int('1')
        coins = int(coins)

elif color == 'green':
    typewriter('The color of spinach and broccoli. ')
    guessgreen = input('What color do you think it is? ').lower()
    if guessgreen == 'green':
        weaponlevel = int('2')
        coins = int(coins + 100)
        typewriter(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your {weapon} has to be level 7.
You earned 100 coins.
Current amount of coins = 100
\n\
""")
    else:
        typewriter(f"Wrong answer. your weapon won't level up this round. Your {weapon} is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 7.\n\
")
        weaponlevel = int('1')
        coins = int(coins)
       

choices = ['rock','paper','scissors']
minigame = input('Do you want to play a small game for extra points? This is not necessary. (yes/no) ').lower()
if minigame == 'no':
    print('ok')
    weaponlevel = int(weaponlevel + 1)
    typewriter(f"""
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
if minigame == 'yes':
    choices = ['rock','paper','scissors']
    steenpapierschaar = random.choice (choices)
    mychoice = input('rock, paper or scissors? ').lower()
    typewriter(f'computers choice = {steenpapierschaar} \n\
')
    typewriter(f'your choice = {mychoice} \n\
')
    if steenpapierschaar == mychoice:
        typewriter("It's a tie, you won't earn any points. \n\
")
        weaponlevel2 = weaponlevel
    elif mychoice == 'rock':
        if steenpapierschaar == 'paper':
            typewriter('you lose, no points or coins.\n\
')
            weaponlevel = weaponlevel2
        if steenpapierschaar == 'scissors':
           weaponlevel2 = int(weaponlevel + 1)
           typewriter(f"""you win
Your {weapon} is leveling up.
level {weaponlevel} > {weaponlevel2}
current weapon level is {weaponlevel2}
Your current amount of coins is {coins}\n\
""")
    elif mychoice == 'paper':
        if steenpapierschaar == 'rock':
            weaponlevel2 = int(weaponlevel + 1)
            typewriter(f"""you win
Your {weapon} is leveling up.
level {weaponlevel} > {weaponlevel2}
current weapon level is {weaponlevel2}
Your current amount of coins is {coins}\n\
""")
        if steenpapierschaar == 'scissors':
            typewriter('you lose, no points or coins.\n\
')
            weaponlevel2 = weaponlevel
    elif mychoice == 'scissors':
        if steenpapierschaar == 'rock':
            typewriter('you lose, no points or coins.\n\
')
            weaponlevel2 = weaponlevel
        if steenpapierschaar == 'paper':
            weaponlevel2 = int(weaponlevel + 1)
            typewriter(f"""you win
Your {weapon} is leveling up.
level {weaponlevel} > {weaponlevel2}
current weapon level is {weaponlevel2}
Your current amount of coins is {coins}\n\
""")



typewriter(f'Your {weapon} level is now {weaponlevel2} and you have {coins} coins. The games will continue tomorrow, get some sleep. \n\
')

typewriter(f'You go to sleep in a big house. All the players are in this house. there is only one sleeping room. You go to sleep. \n\
 \n\
The next morning you wake up at 9 a.m. You go to the cafeteria with the other players. there is only one menu: bread. The cost of one bread is only 5 coins. \n\
current amount of coins = {coins}\n\
')
bread = input('You will need 200 coins later to acsend your {weapon} to level 7. Do you want to buy bread? (yes/no) ')
if bread == 'yes':
    coins = coins - int(5)
    typewriter(f'One bread is bought. You are not hungry anymore.\n\
current amount of coins = {coins}\n\
')
if bread == 'no':
    typewriter("You don't eat anything. You are hungry and can't think straight anymore. \n\
")

    sure = input("Are you sure? Do you want to buy bread? (yes/no) ")
    if sure == 'no':
        typewriter("You can't hold on anymore and you die.")
        sys.exit
    if sure == 'yes':
        coins = coins - int(5)
        typewriter(f"You buy bread and you're not hungry anymore. \n\
current amount of coins = {coins} \n\
")

typewriter('You go back to the sleeping room and wait for the next game to start. \n\
. . .\n\
')

typewriter('<The second game will begin now>\n\
you have to guess what the answer is based on the information you get.\n\
')
print("""★ * ★ * ★ = 30
★ + ♦ + ♦ = 18 
♦ - ◑ = 2
""")
antwoord = input('What is ★ + ♦ + ◑ ? ')
if antwoord == '16':
    coins = int(coins + 100)
    weaponlevel3 = (weaponlevel2 + int(1))
    typewriter(f"""That is right!
Your weapon is leveling up.
level {weaponlevel2} > {weaponlevel3}
current weapon level is {weaponlevel3}
Your current amount of coins is {coins}\n\
""")
else:
    weaponlevel3 = weaponlevel2
    typewriter(f"That is not the answer. Your weapon can't level up.\n\
current weapon level = {weaponlevel3}\n\
current amount of coins is {coins}\n\
")



typewriter("The monster started talking again.\n\
'There are a few games remaining.'\n\
'The person who wins all the games will be able to kill me and become king.'\n\
")


typewriter("<The third game will begin now.>\n\
Guess the number that belongs to the question mark.")
print("""
   9
  7 2
 5 7 6
4 6 ? 8
""")
antw = input('Which number belongs to the question mark? ')
if antw == '9':
    coins = int(coins + 50)
    weaponlevel4 = (weaponlevel3 + int(1))
    typewriter(f"""That is right!
Your {weapon} is leveling up
level {weaponlevel3} > {weaponlevel4}
current weapon level is {weaponlevel4}
current amount of coins is {coins}\n\
""")
else:
    weaponlevel4 = weaponlevel3
    typewriter(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel4}
current amount of coins is {coins}\n\
""")

typewriter(f"Your current weapon level is {weaponlevel4} and you have {coins} coins.\n\
You have to get your weapon level to 6 and have 200 coins to win.\n\
")

typewriter("<The fourth game will begin now.>\n\
Choose the arrow that belongs on the question mark. only answer with a, b, c or d\n\
")
print(""" 
➡ ⬊ ⬇
⬇ ⬋ ⬅
⬆ ⬈ ?
""")
answer = input('Which arrow belongs on the question mark? [a. ⬇ ] [b. ⬆ ] [c. ⬅ ] [d. ➡ ]')
if answer in ('d', 'D'):
    coins = int(coins + 100)
    weaponlevel5 = (weaponlevel4 + int(1))
    typewriter(f"That is correct. \n\
your {weapon} is leveling up\n\
level {weaponlevel4} > {weaponlevel5}\n\
current weapon level is {weaponlevel5}\n\
current amount of coins is {coins}")
else:
    weaponlevel5 = weaponlevel4
    typewriter(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel5}
current amount of coins is {coins}\n\
""")

typewriter("""<The fourth game will begin now.>\n\
You have to answer what number should come on the dots in this series.""")

series = input('Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come on the dots? ')
if series == '10':
    weaponlevel6 = weaponlevel5
    typewriter("""That is correct!""")
    typewriter(f"""you win
Your {weapon} is leveling up.
level {weaponlevel5} > {weaponlevel6}
current weapon level is {weaponlevel6}
Your current amount of coins is {coins}\n\
""")
    weaponlevel2 = int(weaponlevel + 1)
    coins = int(coins + 50)
if minigame =='no':
    weaponlevel2 = weaponlevel
import sys, time, os, string, random

wakeup = input("Do you want to wake up? (yes/no) ").lower()

if wakeup == 'yes':
    print("You wake up in a bus. Suddenly an explosion is heard. A bright light flashed from the front of the bus. Than a monster-like creature appeared. \n\
")
else:
    print('goodbye')
    sys.exit()


first_choice = input('What do you want to do? [a. Try to kill the monster] [b. Run] ').lower()
dead_1 = "You are too weak, you died. "
live_1 = "You run to the back of the bus. The monster is still in your sight, but too far to kill you. "

if first_choice in ('b','B'):
    print(live_1)
elif first_choice == 'a':
    print(dead_1)
    sys.exit()
else:
    sys.exit()
    

zin2 = "The monster starts talking\n\
'The game will start soon.'\n\
. . .\n\
The monster continued talking.\n\
'Some of you are invited for the game.'\n\
. . .\n\
'your invitation will arive at any moment'\n\
"
print(zin2)

name = input('What is your name? ')
invitation = input(f'Dear {name},\n\
you are invited to participate in the game. do you accept the invitation? (yes/no) ').lower()

numb1 = int(random.randint(1,10))
numb2 = int(random.randint(1,10))

if invitation in ('no', 'NO', 'n'):
    sys.exit()
if invitation in('yes', 'YES', 'y'):
    print('The game will start in another world. to teleport to this world solve the quiz.\n\
')
    quiz = int(input(f'What is the anwser to {numb1} * {numb2}? '))
    if int (numb1 * numb2 == quiz):
        print('That is correct. You will teleport to another world in a few seconds.\n\
')
    if int(numb1 * numb2 != quiz):
        print('That is wrong.')
        sys.exit()

print('. . . \n\
You are now in another world to continue the game. choose a weapon to continue.\n\
')
weapon = input('choose one from the following: hammer, sword, magic book or spear. ')

print(f'congrats! you are now in possession of a {weapon}\n\
You can use this weapon to defeat the monster. but first you have to level up your weapon by playing games. \n\
')
print("""<The first game will start now.>
The game is simple.
You have to guess the color based on the information given.\n\
""")

weaponlevel = int('1')
coins = int('0')

color_list = ['blue', 'red','green']
color = random.choice(color_list)

if color == 'red':
    print('The color of strawberries. ')
    guessred = input('What color do you think it is? ').lower()
    if guessred == 'red':
        weaponlevel = int('2')
        coins = int(coins + 100)
        print(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your weapon has to be level 6.
You earned coins.
Current amount of coins = 100
\n\
""")
    else:
        print("Wrong answer. your weapon won't level up this round. Your weapon is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 6.\n\
")
        weaponlevel = int('1')
        coins = int(coins)

elif color == 'blue':
    print('The color is seen a lot outside when you look up. its also seen when you look in water. ')
    guessblue = input('what color do you think it is? ').lower()
    if guessblue == 'blue':
        weaponlevel = int('2')
        coins = int(coins + 100)
        print(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your weapon has to be level 6.
You earned coins.
Current amount of coins = 100
\n\
""")
    else:
        print("Wrong answer. your weapon won't level up this round. Your weapon is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 6.\n\
")
        weaponlevel = int('1')
        coins = int(coins)

elif color == 'green':
    print('The color of spinach and broccoli. ')
    guessgreen = input('What color do you think it is? ').lower()
    if guessgreen == 'green':
        weaponlevel = int('2')
        coins = int(coins + 100)
        print(f"""That is right!
Your {weapon} is leveling up
level 1 > 2
Your weapon is now level 2. To deafeat the monster your {weapon} has to be level 6.
You earned coins.
Current amount of coins = 100
\n\
""")
    else:
        print(f"Wrong answer. your weapon won't level up this round. Your {weapon} is level 1 and you have 0 coins. To deafeat the monster your weapon has to be level 6.\n\
")
        weaponlevel = int('1')
        coins = int(coins)
       

minigame = input('Do you want to play a small game for extra points? This is not necessary. (yes/no) ').lower()
if minigame == 'no':
    print('ok')
    weaponlevel = int(weaponlevel)
    print(f"""
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
if minigame in ('yes', 'Yes', 'y'):
    choices = ['rock','paper','scissors']
    steenpapierschaar = random.choice (choices)
    mychoice = input('rock, paper or scissors? ').lower()
    print(f'computers choice = {steenpapierschaar} \n\
')
    print(f'your choice = {mychoice} \n\
')
    if steenpapierschaar == mychoice:
        print("It's a tie, you won't earn any points. \n\
")
        
        weaponlevel
    elif mychoice == 'rock':
        if steenpapierschaar == 'paper':
            print('you lose, no points or coins.\n\
')
            weaponlevel
        if steenpapierschaar == 'scissors':
           weaponlevel = int(weaponlevel + 1)
           print(f"""you win
Your {weapon} is leveling up.
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
    elif mychoice == 'paper':
        if steenpapierschaar == 'rock':
            weaponlevel = int(weaponlevel + 1)
            print(f"""you win
Your {weapon} is leveling up.
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
        if steenpapierschaar == 'scissors':
            print('you lose, no points or coins.\n\
')
            weaponlevel
    elif mychoice == 'scissors':
        if steenpapierschaar == 'rock':
            print('you lose, no points or coins.\n\
')
            weaponlevel
        if steenpapierschaar == 'paper':
            weaponlevel = int(weaponlevel + 1)
            print(f"""you win
Your {weapon} is leveling up.
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")



print(f'The games will continue tomorrow, get some sleep. \n\
')

print(f'You go to a house. All the players are in this house. There is only one sleeping room. You go to sleep. \n\
 \n\
The next morning you wake up at 9 a.m. You go to the cafeteria with the other players. there is only one menu: bread. The cost of one bread is only 5 coins. \n\
current amount of coins = {coins}\n\
')
bread = input(f'You will need 200 coins later to acsend your {weapon} to level 6. Do you want to buy bread? (yes/no) ').lower()
if bread == 'yes':
    coins = coins - int(5)
    print(f'One bread is bought. You are not hungry anymore.\n\
current amount of coins = {coins}\n\
')
if bread == 'no':
    print("You don't eat anything. You are hungry and can't think straight anymore. \n\
")

    sure = input("Are you sure? Do you want to buy bread? (yes/no) ").lower()
    if sure == 'no':
        print("You can't hold on anymore and you die.")
        sys.exit
    if sure == 'yes':
        coins = coins - int(5)
        print(f"You buy bread and you're not hungry anymore. \n\
current amount of coins = {coins} \n\
")

print('You go back to the sleeping room and wait for the next game to start. \n\
. . .\n\
')

print('<The second game will begin now>\n\
you have to guess what the answer is based on the information you get.\n\
')
print("""★ * ★ * ★ = 30
★ + ♦ + ♦ = 18 
♦ - ◑ = 2
""")
antwoord = input('What is ★ + ♦ + ◑ ? ')
if antwoord in ('16','sixteen'):
    coins = int(coins + 100)
    weaponlevel = (weaponlevel + int(1))
    print(f"""That is right!
Your weapon is leveling up.
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
else:
    weaponlevel = weaponlevel
    print(f"That is not the answer. Your weapon can't level up.\n\
current weapon level = {weaponlevel}\n\
current amount of coins is {coins}\n\
")

print("The monster started talking again.\n\
'There are a few games remaining.'\n\
'The person who wins all the games will be able to kill me and become king.'\n\
<The third game will begin now.>\n\
Guess the number that belongs on the question mark.\n\
")
print("""
   9
  7 2
 5 7 6
4 6 ? 8
""")
antw = input('Which number belongs on the question mark? ')
if antw in ('9','nine',):
    coins = int(coins + 50)
    weaponlevel = (weaponlevel + int(1))
    print(f"""That is right!
Your {weapon} is leveling up
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
current amount of coins is {coins}\n\
""")
else:
    weaponlevel = weaponlevel
    print(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel}
current amount of coins is {coins}\n\
""")

print('You have to get to weapon level 6 to win. But to go from level 5 to 6 you have to acsend your weapon with 200 coins.\n\
')

print("<The fourth game will begin now.>\n\
Choose the arrow that belongs on the question mark. only answer with a, b, c or d\n\
")
print(""" 
➡ ⬊ ⬇
⬇ ⬋ ⬅
⬆ ⬈ ?
""")
answer = input('Which arrow belongs on the question mark? [a. ⬇ ] [b. ⬆ ] [c. ⬅ ] [d. ➡ ] ')
if answer in ('d', 'D'):
    coins = int(coins + 100)
    weaponlevel = (weaponlevel + int(1))
    if weaponlevel == int(6):
        print('You have to acsend your weapon to get to level 6. This will cost 200 coins.\n\
')
        acsend = input(f'You currently have {coins} coins. Say yes if you want to acsend your weapon, otherwise say no. ')
        if acsend == 'yes':
            print(f'Acsending your {weapon} . . .\n\
level 5 > 6\n\
congratulations! You are the first person to reach weapon level 6. ')
    if weaponlevel == int(5):
      print(f"That is correct. \n\
your {weapon} is leveling up\n\
level {weaponlevel - int(1)} > {weaponlevel}\n\
current weapon level is {weaponlevel}\n\
current amount of coins is {coins}\n\
")
else:
    weaponlevel = weaponlevel
    print(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel}
current amount of coins is {coins}\n\
""")



if weaponlevel <= 5:
    print("""<The fifth game will begin now.>\n\
You have to answer what number should come on the dots in this series.\n\
""")
    series = input('Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come on the dots? ')
    if series == '10':
        weaponlevel = (weaponlevel + 1)
        print("""That is correct! """)
        print(f"""
Your {weapon} is leveling up.
level {weaponlevel - int(1)} > {weaponlevel}
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
        coins = int(coins + 50)
    if minigame =='no':
        weaponlevel = weaponlevel


if weaponlevel < 6:
    print('You have lost the game. You die')
    sys.exit()
if weaponlevel >= 6:
    print(f"""Your {weapon} is level {weaponlevel}! you can kill the monster now.
You start walking towards the monster.
You are close enough to the monster to kill him.\n\
""")
    coins = coins + int(1000)
    kill = input(f'Press enter to kill the monster with your {weapon}.')
    print(f"""You attack the monster with your {weapon}. After a few attacks the monster dies.
. . .
Congratulations! You are the winner of the game.
You have become king.
You can choose a gift and leave.\n\
""")

gift=input('Choose one: frog, dolphin, elephant. ')
if gift in ('frog', 'Frog'):
        print("""           
           .--._.--.
          ( O     O )
          /   . .   \.
         .`._______.'.
        /(           )\.
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\.
         '-'|/   \|`-` \n\
""")
        print(f'Goodbye, {name}')
        sys.exit()
if gift in('dolphin', 'Dolphin'):
        print("""                                      
                                       .--.
                _______             .-"  .'
        .---u"""       """"---._  ."    %
      .'                        "--.    %
 __.--'  o                          "".. "
(____.                                  ":
 `----.__                                 ".
         `----------__                     ".
               ".   . ""--.                 ".
                 ". ".     ""-.              ".
                   "-.)        ""-.           ".
                                   "".         ".
                                      "".       ".
                                         "".      ".
                                            "".    ".
                      ^~^~^~^~^~^~^~^~^~^~^~^~^"".  "^~^~^~^~^
                                            ^~^~^~^  ~^~
                                                 ^~^~^~ \n\
""")
        print(f'Goodbye, {name}')
        sys.exit()
if gift in("elephant, Elephant"):
        print("""
                            _
                          .' `'.__
                         /      \ `'"-,
        .-''''--...__..-/ .     |      \.
      .'               ; :'     '.  G   |
     /                 | :.       \     =\.
    ;                   \':.      /  ,-.__;.-;`
   /|     .              '--._   /-.7`._..-;`
  ; |       '                |`-'      \  =|
  |/\        .   -' /     /  ;         |  =/
  (( ;.       ,_  .:|     | /     /\   | =|
   ) / `\     | `""`;     / |    | /   / =/
     | ::|    |      \    \ \    \ `--' =/
    /  '/\    /       )    |/     `-...-`
   /    | |  `\    /-'    /;
   \  ,,/ |    \   D    .'  \.
    `""`   \  nnh  D_.-'L__nnh
            `""'\n\
""")    
        print(f'Goodbye, {name}')
        sys.exit()
elif gift != ('frog', 'elephant', 'dolphin'):
        print("""
       o                o
                  o
         o   ______      o
           _/  (   \_
 _       _/  (       \_  O
| \_   _/  (   (    0  \.
|== \_/  (   (           |
|=== _ (   (   (         |
|==_/ \_ (   (           |
|_/     \_ (   (     \__/
          \_ (       _/
            |  |____/
           /__/
         \n\
""")
        print(f"You didn't choose a gift, so we chose one for you. Goodbye, {name}.")
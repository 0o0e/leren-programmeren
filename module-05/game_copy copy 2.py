import sys, time, os, string, random
def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.03)
        else:
            time.sleep(1)
    

uitkomst = ''

def steenpapierschaarr():
    global uitkomst
    choices = ['rock','paper','scissors']
    steenpapierschaar = random.choice (choices)
    mychoice = input('rock, paper or scissors? ').lower()
    typewriter(f'computers choice = {steenpapierschaar}\n\
')
    typewriter(f'your choice = {mychoice}\n\
')
    if steenpapierschaar == mychoice:
        uitkomst = 'tie'

    elif mychoice == 'rock':
        if steenpapierschaar == 'paper':
            uitkomst = 'lose'
        if steenpapierschaar == 'scissors':
            uitkomst = 'win'
    elif mychoice == 'paper':
        if steenpapierschaar == 'rock':
            uitkomst = 'win'
        if steenpapierschaar == 'scissors':
            uitkomst='lose'
    elif mychoice == 'scissors':
        if steenpapierschaar == 'rock':
            uitkomst = 'lose'
        if steenpapierschaar == 'paper':
            uitkomst= 'win'
    print(f"it's a {uitkomst} ! ")

coins = 0
weaponlevel = 1

def up(weaponname):
    global weaponlevel
    global coins
    typewriter(f"""That is the right answer!
Your {weaponname} is leveling up
level {weaponlevel - 1 } > {weaponlevel}
Your weapon is now level {weaponlevel}. To deafeat the monster your weapon has to be level 6.
You earned coins.
Current amount of coins = {coins}
""")


def main():
    global weaponlevel
    global coins

    typewriter("You wake up in a bus. Suddenly an explosion is heard. A bright light flashed from the front of the bus. Than a monster-like creature appeared. \n\
")
    first_choice = input('What do you want to do? [a. Try to kill the monster] [b. Run] ').lower()
    live_1 = ("You run to the back of the bus. The monster is still in your sight, but too far to kill you. ")

    if first_choice in ('b','B'):
        typewriter(live_1)
    elif first_choice == 'a':
        typewriter('press enter to attack ')
        input('')
        typewriter('You are too weak and are thrown back by the monster.\n\
')
        verder = input('Do you want to keep attacking him or run away? [a. keep attacking] [b. run] ')
        if verder == 'b'.lower():
            typewriter(live_1)
        else:
            typewriter('You are too weak. You died. ')
            return


    typewriter ("The monster starts talking:\n\
'The game will start soon.'\n\
. . .\n\
The monster continued talking.\n\
'Some of you are invited for the game.'\n\
. . .\n\
'your invitation will arive at any moment'\n\
")

    name = input('What is your name? ')
    invitation = input(f'Dear {name},\n\
you are invited to participate in the game. do you accept the invitation? (yes/no) ').lower()

    if invitation == 'no':
        typewriter('you died ')
        return
    if invitation in('yes', 'YES', 'y'):
        typewriter('The game will start in another world. to teleport to this world solve the quiz.\n\
')


    numb1 = random.randint(1,10)
    numb2 = random.randint(1,10)

    while True:
        try: 
            quiz = int(input(f'What is the anwser to {numb1} * {numb2}? '))
            if int(numb1 * numb2 != quiz):
                print('That is wrong, you died.')
                return
            if int(numb1 * numb2 == quiz):
                typewriter('That is correct. You will teleport to another world in a few seconds.\n\
')
            break
        except ValueError: 
            print('That is not a number.')


    typewriter('. . . \n\
You are now in another world to continue the game. choose a weapon to continue.\n\
')
    weapon = input('choose one from the following: hammer, sword, magic book or spear. ')
    while weapon not in ('hammer','sword','magic book','spear'):
        print('that is not a choice.')
        weapon = input('choose one from the following: hammer, sword, magic book or spear. ')

    typewriter(f'congrats! you are now in possession of a {weapon}\n\
You can use this weapon to defeat the monster. but first you have to level up your weapon by playing games. \n\
\n\
<The first game will start now.>\n\
The game is simple.\n\
You have to guess the color based on the information given.\n\
')

    color_list = ['blue', 'red','green']
    color = random.choice(color_list)
    wrong_answer= (f"Wrong answer. your weapon won't level up this round. Your weapon is level {weaponlevel} and you have {coins} coins. To deafeat the monster your weapon has to be level 6.\n\
")

    if color == 'red':
        typewriter('The color of strawberries. ')
        guessred = input('What color do you think it is? ').lower()
        if guessred in ('red','rood'):
            weaponlevel += 1
            coins += 100
            up(weapon)

        else:
            typewriter(wrong_answer)

    elif color == 'blue':
        typewriter('The color is seen a lot outside when you look up. its also seen when you look in water. ')
        guessblue = input('what color do you think it is? ').lower()
        if guessblue in ('blue','blauw'):
            weaponlevel += 1
            coins += 100
            up(weapon)

        else:
            typewriter(wrong_answer)

    elif color == 'green':
        typewriter('The color of spinach and broccoli. ')
        guessgreen = input('What color do you think it is? ').lower()
        if guessgreen in ('green','groen'):
            weaponlevel += 1
            coins += 100
            up(weapon)

        else:
            typewriter(wrong_answer)


    minigame = input('Do you want to play a small game for extra points? This is not necessary. (yes/no) ').lower()
    if minigame == 'no':
        typewriter('ok\n\
')
    if minigame in ('yes','y'):
        steenpapierschaarr()
        if uitkomst == 'win':
            coins += 100
            weaponlevel+=1
        print(coins)
        print(weaponlevel)

    typewriter(f'The games will continue tomorrow, get some sleep. \n\
You go to a house. All the players are in this house. There is only one sleeping room. You go to sleep. \n\
\n\
The next morning you wake up at 9 a.m. You go to the cafeteria with the other players. there is only one menu: bread. The cost of one bread is only 5 coins. \n\
current amount of coins = {coins}\n\
')
    bread = input(f'You will need 200 coins later to acsend your {weapon} to level 6. Do you want to buy bread? (yes/no) ').lower()
    if bread == 'yes':
        coins -= 5
        typewriter(f'One bread is bought. You are not hungry anymore.\n\
current amount of coins = {coins}\n\
')
    else:
        typewriter("You don't eat anything. You are hungry and can't think straight anymore. \n\
")
        sure = input("Are you sure? Do you want to buy bread? (yes/no) ")
        if sure == 'no':
            typewriter("You can't hold on anymore and you die.")
            return
        else:
            coins -=5
            typewriter(f'One bread is bought. You are not hungry anymore.\n\
current amount of coins = {coins}\n\
')

    typewriter('You go back to the sleeping room and wait for the next game to start. \n\
. . .\n\
<The second game will begin now>\n\
you have to guess what the answer is based on the information you get.\n\
')
    print("""★ * ★ * ★ = 30
★ + ♦ + ♦ = 18 
♦ - ◑ = 2
""")
    antwoord = input('What is ★ + ♦ + ◑ ? ')
    if antwoord in ('16','sixteen'):
        coins += 100
        weaponlevel += 1
        up(weapon)
    else:
        typewriter(f"That is not the answer. Your weapon can't level up.\n\
current weapon level = {weaponlevel}\n\
current amount of coins is {coins}\n\
")

    typewriter("The monster started talking again.\n\
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
        coins += 50
        weaponlevel += 1
        up(weapon)
    else:
        typewriter(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel}
current amount of coins is {coins}\n\
""")

    typewriter("You have to get to weapon level 6 to win. But to go from level 5 to 6 you have to acsend your weapon with 200 coins.\n\
<The fourth game will begin now.>\n\
Choose the arrow that belongs on the question mark. only answer with a, b, c or d\n\
")
    print(""" 
    ➡ ⬊ ⬇
    ⬇ ⬋ ⬅
    ⬆ ⬈ ?
    """)
    answer = input('Which arrow belongs on the question mark? [a. ⬇ ] [b. ⬆ ] [c. ⬅ ] [d. ➡ ] ')
    if answer in ('d', 'D'):
        coins += 100
        weaponlevel += 2
        print(weaponlevel)#weaponlevel is 7 als alles goed is, eentje fout is 6
        if weaponlevel >= 6:
            typewriter('You have to acsend your weapon to get to level 6. This will cost 200 coins.\n\
')
            acsend = input(f'You currently have {coins} coins. Say yes if you want to acsend your weapon, otherwise say no. ')
            if acsend != 'yes':
                acsend2=input(f"You have to acsend your weapon to win the game. do you want to acsend you {weapon}? (yes / no) ")
                if acsend2 == 'no':
                    typewriter("You didn't acsend your weapon. You can't defeat the monster and die. ")
                    return
            if acsend == 'yes' or acsend2 == 'yes':
                typewriter(f'Acsending your {weapon} . . .\n\
level 5 > 6\n\
congratulations! You are the first person to reach weapon level 6. ')

    else:
        typewriter(f"""That is not right. You can't level up your {weapon}.
current weapon level {weaponlevel}
current amount of coins is {coins}\n\
""")

# ufedrtyuio /\ /\ /\

    if weaponlevel <= 5:
        typewriter("""<The fifth game will begin now.>\n\
You have to answer what number should come on the dots in this series.\n\
""")
        series = input('Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come on the dots? ')
        if series == '10':
            weaponlevel += 1
            typewriter("""That is correct! \n\
""")
        if weaponlevel >= 6:
            acsend3 = input(f'You currently have {coins} coins. Say yes if you want to acsend your weapon, otherwise say no. ')
            if acsend3 == 'yes':
                coins -= 200
                typewriter(f"""
Your {weapon} is leveling up.
level 5 > 6
current weapon level is {weaponlevel}
Your current amount of coins is {coins}\n\
""")
            if acsend2 == 'no':
                typewriter("You couldn't get to weapon level 6. You died. ")
                return

    if weaponlevel < 6:
        typewriter('There are no games remaining, and your weapon level is too low. You have lost the game. You die\n\
')
        return
        
    typewriter(f"""Your {weapon} is level {weaponlevel}! you can kill the monster now.
You start walking towards the monster.
You are close enough to the monster to kill him.\n\
""")
    kill = input(f'Press enter to kill the monster with your {weapon}.')
    typewriter(f"""You attack the monster with your {weapon}. After a few attacks the monster dies.
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
    _ /  \  \   /  /  \_
  .~   `  \  \ /  /  '   ~.
 {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
/. - ~ ,_-'  .^.  `-_, ~ - .\.
        '-'|/   \|`-` \n\
""")
        print(f'Goodbye, {name}')
        return
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
        return
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
        return
    elif gift != ('frog', 'elephant', 'dolphin'):
        print("""
    o                o
                o
        o    ______      o
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
        """)
        typewriter(f"You didn't choose a gift, so we chose one for you. Goodbye, {name}.\n\
")
    return


while True:
    main()
    again=input('do you want to play again? (yes/no) ')
    if again in ('no','b'):
        break
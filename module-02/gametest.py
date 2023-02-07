import sys, time

coins = 0
# weaponlevel = 0
# def coin_update(coin):
#     coin += 100
#     coins = coin_update(coins)
#     return coin
    
# def weapon_update(weaplevel):
#     weaplevel += 1

#     return weaplevel

# # coins = coin_update(coins)
# weaponlevel = weapon_update(weaponlevel)
# print(coins)
# print(weaponlevel)

# weapon = 'gaa'
# coins += 10
# def up(weaponn):
#     print(f"""That is right!
#     Your {weaponn} is leveling up
#     level {weaponlevel -1 } > {weaponlevel}
#     Your weapon is now level {weaponlevel}. To deafeat the monster your weapon has to be level 6.
#     You earned coins.
#     Current amount of coins = {coins}
#     """)
# weaponlevel = 1
# up(weapon)

def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.03)
        else:
            time.sleep(1)

aa = ('hiii')

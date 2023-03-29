from ijssalon import *
bestellen = True

while bestellen == True:
    meer_bestellen = True

    hoorn_bak = bakje_of_hoorntje(aantal_bolletjes())
    if hoorn_bak == 'sorry, zulke grote bakken hebben we niet. ':
        while hoorn_bak == ('sorry, zulke grote bakken hebben we niet.'):
            hoorn_bak = bakje_of_hoorntje(aantal_bolletjes())

    while meer_bestellen == True:
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee':
            bestellen = False
            meer_bestellen = False
        elif meer != 'ja' and meer != 'nee':
            print('sorry, dat snap ik niet')
        elif meer == 'ja':
            meer_bestellen = False
            
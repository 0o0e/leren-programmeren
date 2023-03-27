from ijssalon import *
a = True

while a == True:
    # meer = ''
    meer_bestellen = True

    hoorn_bak = bakje_of_hoorntje(aantal_bolletjes())
    print(hoorn_bak)
    print('dd')
    while hoorn_bak == ('sorry, zulke grote bakken hebben we niet. '):
        hoorn_bak = bakje_of_hoorntje(aantal_bolletjes())
        print(hoorn_bak)

    while meer_bestellen == True:
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee' and meer != 'ja':
            a = False
            b = False
            meer_bestellen = False
        elif meer != 'ja' and meer != 'nee':
            print('sorry, dat snap ik niet')
            continue
        elif meer == 'ja':
            meer_bestellen = False
            
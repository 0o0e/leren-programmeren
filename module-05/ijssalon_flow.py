from ijssalon import *
bestellen = True

while bestellen == True:
    meer_bestellen = True

    aantal_bollen = aantal_bolletjes('')
    hoorn_bak = kies_bakje_of_hoorntje(aantal_bollen,'')
    if hoorn_bak != 'zulke grote bakken hebben we niet':
        print(f'hier is uw {hoorn_bak} met {aantal_bollen} bolletjes.')
    else:
        while hoorn_bak == ('zulke grote bakken hebben we niet'):
            print('zulke grote bakken hebben we niet')
            break
        continue

    while meer_bestellen == True:
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee':
            bestellen = False
            meer_bestellen = False
        elif meer != 'ja' and meer != 'nee':
            print('sorry, dat snap ik niet')
        elif meer == 'ja':
            meer_bestellen = False
            
            
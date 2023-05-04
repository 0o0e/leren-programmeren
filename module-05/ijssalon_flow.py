from ijssalon import *
bestellen = True
bolletje_pr = 0
hoorntje_pr = 0
bakje_pr = 0


aantal_bak = 0
aantal_hoorn = 0


smakenlijst = []
while bestellen == True:
    meer_bestellen = True
    
    

    aantal_bollen = aantal_bolletjes()
    smaak = bolletje_smaak(aantal_bollen)

    smakenlijst += smaak


    hoorn_bak = kies_bakje_of_hoorntje(aantal_bollen)
    bolletje_pr += round((1.10 * aantal_bollen),2)



    if hoorn_bak != AANTAL_KAN_NIET:
        print(f'hier is uw {hoorn_bak} met {aantal_bollen} bolletjes.')
    else:
        print(AANTAL_KAN_NIET)



    if hoorn_bak == 'bakje':
        bakje_pr += 0.75
        aantal_bak += 1
    elif hoorn_bak == 'hoorntje':
        hoorntje_pr += 1.25
        aantal_hoorn +=1

    verder = meerbestellen()
    if verder == 'nee':
        bestellen = False
        meer_bestellen = False
bon(bolletje_pr,hoorntje_pr,bakje_pr,aantal_bak,aantal_hoorn,smakenlijst)


# while meer_bestellen == True:
#     meer = input('wilt u meer bestellen? ')
#     if meer == 'nee':
#         bestellen = False
#         meer_bestellen = False
#     elif meer != 'ja' and meer != 'nee':
#         print('sorry, dat snap ik niet')
#     elif meer == 'ja':
#         meer_bestellen = False
        
        
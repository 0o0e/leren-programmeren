from ijssalon import *

bestellen = True
bolletje_pr = 0
hoorntje_pr = 0
bakje_pr = 0

liter_pr = 0

topping_pr = 0

aantal_bak = 0
aantal_hoorn = 0
aantal_liter = 0

smakenlijst = []
while bestellen == True:
    meer_bestellen = True
    TYPE_KLANT = input('Bent u 1. een particuliere klant of 2. een zakelijke klant? ')
    if TYPE_KLANT not in ('1','2'):
        print(SNAPIKNIET)
        continue

    if TYPE_KLANT == '2':
        aantal_liter = hoeveel_liter()
        smaak_liter = liter_smaak(aantal_liter)
        smakenlijst += smaak_liter
        liter_pr += round((9.80 * aantal_liter),2)
        bestellen = False
        meer_bestellen = False

    elif TYPE_KLANT == '1':
        aantal_bollen = aantal_bolletjes()
        smaak = bolletje_smaak(aantal_bollen)
        hoorn_bak = kies_bakje_of_hoorntje(aantal_bollen)
        topping = toppings(hoorn_bak,aantal_bollen)
        topping_pr += topping
        print(f'hier is uw {hoorn_bak} met {aantal_bollen} bolletjes.')
    


        smakenlijst += smaak


        bolletje_pr += round((0.95 * aantal_bollen),2)





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
bon(bolletje_pr,hoorntje_pr,bakje_pr,aantal_bak,aantal_hoorn,smakenlijst,topping_pr,TYPE_KLANT,liter_pr)

 
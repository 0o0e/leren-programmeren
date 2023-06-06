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


een_bol_pr = 0.95
een_liter_pr = 9.80
typeklant = vraag_typeklant()
print(typeklant)
smakenlijst = []
while bestellen == True:
    meer_bestellen = True


    if typeklant == '2':
        aantal_liter = hoeveel_liter()
        smaak_liter = liter_smaak(aantal_liter)
        smakenlijst += smaak_liter
        liter_pr += round((een_liter_pr * aantal_liter),2)
        bestellen = False
        meer_bestellen = False

    elif typeklant == '1':
        aantal_bollen = aantal_bolletjes()
        smaak = bolletje_smaak(aantal_bollen)
        hoorn_bak = kies_bakje_of_hoorntje(aantal_bollen)
        topping = toppings(hoorn_bak,aantal_bollen)
        topping_pr += topping
        print(f'hier is uw {hoorn_bak} met {aantal_bollen} bolletjes.')
    
        smakenlijst += smaak

        bolletje_pr += round((een_bol_pr * aantal_bollen),2)


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
bon(bolletje_pr,hoorntje_pr,bakje_pr,aantal_bak,aantal_hoorn,smakenlijst,topping_pr,typeklant,liter_pr,een_bol_pr,een_liter_pr)

 
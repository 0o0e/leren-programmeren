
print('Welkom bij Papi Gelato.')

AANTAL_KAN_NIET = 'zulke grote bakken hebben we niet'
SNAPIKNIET = 'Sorry dat is geen optie die we aanbieden...'

def aantal_bolletjes():
    bolletjes = ''
    while type(bolletjes) != int:
        try:
            bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        except ValueError:
            print(SNAPIKNIET)
        else:
            if bolletjes >= 8:
                print(SNAPIKNIET)
                bolletjes = ''
                continue

    return bolletjes


def bolletje_smaak(aantalbolletjes):
    lijst_smaken = []
    nummer = 1
    while nummer != aantalbolletjes + 1:
        smaak = input(f"Welke smaak wilt u voor bolletje nummer {nummer}? A) Aardbei, C) Chocolade of V) Vanille? ")
        if smaak not in ('a','c','v'):
            print(SNAPIKNIET)
            continue
        lijst_smaken.append(smaak)
        nummer+=1


    return lijst_smaken


def kies_bakje_of_hoorntje(aantal_bollen):
    hoorn_of_bak = ''
    while hoorn_of_bak != 'hoorntje' or hoorn_of_bak != 'bakje':
        if aantal_bollen <= 3:
            hoorn_of_bak = input('Wilt u een hoorntje of een bakje? ')
        elif aantal_bollen >= 4 and aantal_bollen < 8:
            hoorn_of_bak = 'bakje'
        elif aantal_bollen >= 8:
            return AANTAL_KAN_NIET
        else:
            print(SNAPIKNIET)
        if hoorn_of_bak == 'bakje' or hoorn_of_bak == 'hoorntje':
            return hoorn_of_bak
        
        
def meerbestellen():
    while True:
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee' or meer == 'ja':
            return meer
        else:
            print(SNAPIKNIET)


            
def bon(bolletjes_pr,hoorntje_prijs,bakje_pr,aantalbak,aantalhoorn,smaken,toppings,typeklant,prijs_liter):
    list =['a','c','v']
    print('----------papi gelato----------')

    for smaak in list:
        if smaak in smaken:
            aantal = smaken.count(smaak)
            if typeklant == '1':
                print(f"b.{smaak} : {aantal} x $1.10 = ${round(1.10 * aantal,2):.2f}")
            elif typeklant == '2':
                print(f"l.{smaak} : {aantal} x $9.80 = ${round(9.80 * aantal,2):.2f}")
    totaalprijs = (bolletjes_pr + hoorntje_prijs + bakje_pr + toppings + prijs_liter)
    if typeklant == '1':
        if bakje_pr > 0:
            print(f'bakjes : {aantalbak} x 0.75 = ${bakje_pr}')
        if hoorntje_prijs > 0:
            print(f'hoorntjes : {aantalhoorn} x 1.25 = ${hoorntje_prijs}')
        if toppings > 0:
            print(f'Topping :   $ {toppings:.2f}')
        print(f"totaal : ${(totaalprijs):.2f}")
    elif typeklant == '2':

        print(f"totaal : ${(totaalprijs + (totaalprijs / 100 * 6)):.2f}")
        print(f"btw (6%): ${(totaalprijs / 100 * 6):.2f}")



    return

def toppings(hoorn_bak,aantalbollen):
    prijs = 0
    # topping = input("Wat voor topping wilt u: A. Geen, B. Slagroom, C. Sprinkels of D. Caramel Saus? ")
    while True: 
        topping = input("Wat voor topping wilt u: A. Geen, B. Slagroom, C. Sprinkels of D. Caramel Saus? ")
        if topping == 'a':
            break

        if topping == 'b':
            prijs += 0.50
            break
        if topping == 'c':
            hoeveel = int(input('Op hoeveel bolletjes wilt u sprinkels? '))
            while hoeveel > aantalbollen:
                print('u hebt niet zoveel bolletjes ')
                hoeveel = int(input('Op hoeveel bolletjes wilt u sprinkels? '))
            else:
                prijs += (hoeveel * 0.30)
                break
        if topping == 'd':
            if hoorn_bak == 'hoorntje':
                prijs +=0.60
                break
            if hoorn_bak == 'bakje':
                prijs += 0.90
                break
        if topping not in ('a','b','c','d'):
            print(SNAPIKNIET)
            continue
    return prijs

def hoeveel_liter():
    aantal_liter = ''
    while type(aantal_liter) != int:
        try:
            aantal_liter = int(input('Hoeveel liter wilt u? '))
        except ValueError:
            print(SNAPIKNIET)
    return aantal_liter


def liter_smaak(aantalliter):
    lijst_smaken = []
    nummer = 1
    while nummer != aantalliter + 1:
        smaak = input(f"Welke smaak wilt u voor liter nummer {nummer}? A) Aardbei, C) Chocolade of V) Vanille? ")
        if smaak not in ('a','c','v'):
            print(SNAPIKNIET)
            continue
        lijst_smaken.append(smaak)
        nummer += 1

    return lijst_smaken


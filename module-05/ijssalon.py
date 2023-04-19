
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

AANTAL_KAN_NIET = 'zulke grote bakken hebben we niet'


def aantal_bolletjes():
    bolletjes = ''
    while type(bolletjes) != int:
        try:
            bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        except ValueError:
            print('dat snap ik niet')

    return bolletjes

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
            print('sorry, dat snap ik niet. ')
        if hoorn_of_bak == 'bakje' or hoorn_of_bak == 'hoorntje':
            return hoorn_of_bak
        
def meerbestellen():
    while True:
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee' or meer == 'ja':
            return meer
        else:
            print('sorry, dat snap ik niet')
            
def bon(aantal_bolletjes,bolletjes_pr,hoorntje_prijs,bakje_pr,aantalbak,aantalhoorn):
    print(f'bolletjes : {aantal_bolletjes} x 1.10 = ${bolletjes_pr}')
    if bakje_pr > 0:
        print(f'bakjes : {aantalbak} x 0.75 = ${bakje_pr}')
    if hoorntje_prijs > 0:
        print(f'hoorntjes : {aantalhoorn} x 1.25 = ${hoorntje_prijs}')
    return


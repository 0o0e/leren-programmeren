
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

def bolletje_smaak(aantalbolletjes):
    lijst_smaken = []
    for i in range(1,aantalbolletjes +1):
        smaak = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        lijst_smaken.append(smaak)
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
            
def bon(bolletjes_pr,hoorntje_prijs,bakje_pr,aantalbak,aantalhoorn,smaken):
    if 'a' in smaken:
        aantal_a = smaken.count('a')
        print(f"b.Aardbei : {aantal_a} x $1.10 = ${round(1.10 * aantal_a,2)}")
    if 'c' in smaken:
        aantal_c = smaken.count('c')
        print(f"b.Chocolade : {aantal_c} x $1.10 = ${round(1.10 * aantal_c,2)}")
    if 'm' in smaken:
        aantal_m = smaken.count('m')
        print(f"b.munt : {aantal_m} x $1.10 = ${round(1.10 * aantal_m,2)}")
    if 'v' in smaken:
        aantal_v = smaken.count('v')
        print(f"b.vanille : {aantal_v} x $1.10 = ${round(1.10 * aantal_v,2)}")

    if bakje_pr > 0:
        print(f'bakjes : {aantalbak} x 0.75 = ${bakje_pr}')
    if hoorntje_prijs > 0:
        print(f'hoorntjes : {aantalhoorn} x 1.25 = ${hoorntje_prijs}')
    print(f"totaal : ${bolletjes_pr + hoorntje_prijs + bakje_pr}")
    return
# aaa
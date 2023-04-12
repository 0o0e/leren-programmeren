
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

def aantal_bolletjes(bolletjes):
    while type(bolletjes) != int:
        try:
            bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        except ValueError:
            print('dat snap ik niet')

    return bolletjes

def kies_bakje_of_hoorntje(aantal_bollen,hoorn_of_bak):
    while hoorn_of_bak != 'hoorntje' or hoorn_of_bak != 'bakje':
        if aantal_bollen <= 3:
            hoorn_of_bak = input('Wilt u een hoorntje of een bakje? ')
        elif aantal_bollen >= 4 and aantal_bollen < 8:
            hoorn_of_bak = 'bakje'
        elif aantal_bollen >= 8:
            return 'zulke grote bakken hebben we niet'
        else:
            print('sorry, dat snap ik niet. ')
        if hoorn_of_bak == 'bakje' or hoorn_of_bak == 'hoorntje':
            return hoorn_of_bak

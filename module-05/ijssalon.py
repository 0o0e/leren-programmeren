print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
a = True
while a == True:
    b = True
    bolletjes = int(input('Hoeveel bolletjes wilt u? '))
    while b == True:
        if bolletjes <= 3:
            hoorn_of_bak = input('Wilt u een hoorntje of een bakje? ')
        elif bolletjes >= 4 and bolletjes <= 8:
            hoorn_of_bak = 'bakje'
        elif bolletjes > 8:
            print('sorry, zulke grote bakjes hebben we niet. ')
            break
        if hoorn_of_bak == 'hoorntje' or hoorn_of_bak == 'bakje':
            print(f'hier is uw {hoorn_of_bak} met {bolletjes} bolletjes.')
            b = False
        else:
            print('sorry, dat snap ik niet')
            continue
        meer = input('wilt u meer bestellen? ')
        if meer == 'nee':
            a = False

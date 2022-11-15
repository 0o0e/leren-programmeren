import random
hoeveelmensen = int(input('Met hoeveel mensen (inclusief jezelf) speel je? '))
stagevangen = 'nee'
aantalhuisjes = 0
aantalstraten = 1
bezeten= ['van iemand','niet van iemand']
keuze = ['van jou', 'niet van jou']
while stagevangen == 'nee' or 'ja':
    roll = input('klik om te rollen ')
    getal = random.randint(2,18)

    if stagevangen == 'ja':
        print('3 beurten overslaan')
    if stagevangen == 'nee':
        vanwie = random.choice(keuze)
        print(f'je hebt {getal} gegooit ')
        print(f'de straat is {vanwie} ')
        if vanwie == 'van jou':
            huisjeskopen = input('wil je huisjes kopen?')
            if huisjeskopen == 'ja':
                aantalhuisjes += 1
                print('Je hebt een huisje gekocht. ')
            else:
                print('niks gekocht. ')
        if vanwie == 'niet van jou':
            straatbezeten = random.choice(bezeten)
            print(f'de straat is {straatbezeten} ')
            if bezeten == 'van iemand':
                print('betaal geld aan bezitter')
            if bezeten == 'van niemand':
                kopen = input('wil je de straat kopen? ')
                if kopen == 'ja':
                    aantalstraten += 1
                    print('je hebt een straat gekocht.')
                else:
                    print('niks gekocht')
        



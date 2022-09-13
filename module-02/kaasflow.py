print("beantwoord de vragen alleen met 'ja' of 'nee' ")

kleur = input ('is de kaas geel? ')

if kleur == 'ja':
    gaten = input('zitten er gaten in? ')
    if gaten == 'ja':
        duur = input('is de kaas belagelijk duur? ')
        if duur == 'ja':
            print('emmenthaler')
        else:
            print('leerdammer')
    if gaten == 'nee':
        hard = input('is de kaas hard als een steen?')
        if hard == 'ja':
            print('parmigiano reggiano')
        else:
            print('goudse kaas')

if kleur == 'nee':
    schimmel = input('heeft de kaas een blauwe schimmel? ')
    if schimmel == 'ja':
        korst = input('heeft de kaas een korst? ')
        if korst == 'ja':
            print('blue rochbaron')
        else:
            print("foume d'ambert")
    if schimmel == 'nee':
        korst_2 = input('heeft de kaas een korst? ')
        if korst_2 == 'ja':
            print('camembert')
        else:
         print('mozzarella')
        
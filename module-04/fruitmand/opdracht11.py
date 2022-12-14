from fruitmand import fruitmand

colors = ['yellow','green','orange','red','brown']
waar = True
while waar == True:
    welkekleur = input(f'Kies een van de volgende kleuren: {(colors)} : ')
    if welkekleur in colors:
        waar = False
    else:
        print('kies een kleur uit de lijst')

welrond = 0
nietrond = 0
for i in range(len(fruitmand)):
    if fruitmand[i]['color'] == welkekleur:
        if fruitmand[i]['round']== True:
            welrond += 1
        else: 
            nietrond += 1
0.

if welrond > nietrond:

    print(f'Er zijn {welrond - nietrond} meer ronde vruchten dan niet ronde vruchten in de kleur {welkekleur}')
elif nietrond > welrond:
    print(f'Er zijn {nietrond- welrond} minder ronde vruchten dan niet ronde vruchten in de kleur {welkekleur}')
elif nietrond == welrond:
    print(f'Er zijn {welrond} ronde vruchten en {nietrond} niet ronde kleuren in de kleur {welkekleur}')
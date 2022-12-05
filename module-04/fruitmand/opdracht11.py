from fruitmand import fruitmand

colors = ['yellow','green','orange','red','brown']
while True:
    welkekleur = input(f'Kies een van de volgende kleuren: {(colors)} : ')
    if welkekleur in colors:
        waar = True
    try:
        waar == True
        break
    except:
        print('kies een kleur uit de lijst')
welrond = 0
nietrond = 0
for i in range(len(fruitmand)):
    if fruitmand[i]['color'] == welkekleur:
        if fruitmand[i]['round']== True:
            welrond += 1
        else: 
            nietrond += 1
verschil1 = (welrond - nietrond)
verschil2 = (nietrond- welrond)
if welrond > nietrond:
    print(f'Er zijn {verschil1} meer ronde vruchten dan niet ronde vruchten in de kleur {welkekleur}')
elif nietrond > welrond:
    print(f'Er zijn {verschil2} minder ronde vruchten dan niet ronde vruchten in de kleur {welkekleur}')
elif nietrond == welrond:
    print(f'Er zijn {welrond} ronde vruchten en {nietrond} niet ronde kleuren in de kleur {welkekleur}')
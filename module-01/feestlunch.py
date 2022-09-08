croissant = 0.39
stokbrood = 2.78

croissantaantal = input ('hoeveel croissanten? ')
stokbroodaantal = input ('hoeveel stokbroden? ')

croissantaantal = float (croissantaantal)
stokbroodaantal = float (stokbroodaantal)

prijscr = croissant * croissantaantal
prijsst = stokbrood * stokbroodaantal

prijszonderkorting = prijscr + prijsst

kortingsbonnen = input ('hoeveel euro korting heb je in totaal? ')
kortingsbonnen = float (kortingsbonnen)

totaalprijs = prijszonderkorting - kortingsbonnen
totaalprijs = float (totaalprijs)

print('De feestlunch kost je bij de bakker ', totaalprijs  ,' euro voor de ', croissantaantal ,' croissantjes en de ', stokbroodaantal ,' stokbroden als je ', kortingsbonnen  ,' euro korting hebt!')



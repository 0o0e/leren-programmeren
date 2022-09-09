from pickletools import int4


croissant = 39
stokbrood = 278

croissantaantal = input ('hoeveel croissanten? ')
stokbroodaantal = input ('hoeveel stokbroden? ')

croissantaantal = int (croissantaantal)
stokbroodaantal = int (stokbroodaantal)

prijscr = croissant * croissantaantal
prijsst = stokbrood * stokbroodaantal

prijszonderkorting = prijscr + prijsst

kortingsbonnen = input ('hoeveel cent korting heb je in totaal? ')
kortingsbonnen = float (kortingsbonnen)

totaalprijs = (prijszonderkorting - kortingsbonnen) 
totaalprijs = float (totaalprijs)

print('De feestlunch kost je bij de bakker ', totaalprijs  ,' cent voor de ', croissantaantal ,' croissantjes en de ', stokbroodaantal ,' stokbroden als je ', kortingsbonnen  ,' cent korting hebt!')



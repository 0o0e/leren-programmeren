iphone_prijs = int(input('Hoe duur is de iphone? '))
samsung_prijs = int(input('Hoe duur is de samsung? '))
asus_prijs = int(input('Hoe duur is de Asus? '))

if iphone_prijs >= asus_prijs and samsung_prijs:
    duurste = iphone_prijs
    duurste_name = 'iphone'    
if samsung_prijs >= iphone_prijs and asus_prijs:
    duurste = samsung_prijs
    duurste_name = 'samsung'
if asus_prijs >= iphone_prijs and samsung_prijs:
    duurste = asus_prijs
    duurste_name = 'asus'
    
if (iphone_prijs <= samsung_prijs and iphone_prijs >= asus_prijs) or (iphone_prijs >= samsung_prijs and iphone_prijs <= asus_prijs):
    middel = iphone_prijs
    middel_name = 'iphone'
if (samsung_prijs <= asus_prijs and samsung_prijs >=iphone_prijs) or (samsung_prijs >= asus_prijs and samsung_prijs <=iphone_prijs):
    middel = samsung_prijs
    middel_name = 'samsung'
if (asus_prijs <= samsung_prijs and asus_prijs >=iphone_prijs) or (asus_prijs >= samsung_prijs and asus_prijs <=iphone_prijs):
    middel = asus_prijs
    middel_name = 'asus'

if (iphone_prijs) <= (asus_prijs and samsung_prijs):
    goedkoopste = iphone_prijs
    goedkoopste_name = 'iphone'
if (samsung_prijs) < (iphone_prijs and asus_prijs):
    goedkoopste = samsung_prijs
    goedkoopste_name = 'samsung'
if (asus_prijs) < (iphone_prijs and samsung_prijs):
    goedkoopste = asus_prijs
    goedkoopste_name = 'asus'

diff = iphone_prijs - samsung_prijs
diff3 = iphone_prijs - asus_prijs 

print(f'De {duurste_name} is het duurst, deze kost {duurste}.')
print(f'De {goedkoopste_name} is het goedkoopst, deze kost {goedkoopste}.')
print(f'De {middel_name} zit er tussen en kost {middel}.')

#iphone kopen = iphone max. 50 duurder dan samsung, asus is NIET 100 euro goedkoper dan allebij
#samsung kopn = iphone is meer dan 50 duurder dan samsung, asus is NIET 100 euro goedkoper dan allebij
#asus kopen = 100 goedkoper dan allebij

asusgoedkoop = iphone_prijs - asus_prijs
asusgoedkoop1 = samsung_prijs - asus_prijs
#moet minimaal 100 zijn om asus te kopen

samsunggoedkoop = iphone_prijs - samsung_prijs
samsungduur = samsung_prijs - asus_prijs

if (asusgoedkoop or asusgoedkoop1) < int(100) and (diff <= 50):
    print(f'Het advies is om de iphone te kopen. Deze is namelijk maar {diff} euro duurder dan de samsung en {diff3} euro duurder dan de asus.')
if (asusgoedkoop or asusgoedkoop1) < int(100) and (diff > 50) :
    print(f'Het advies is om de samsung te kopen. Deze is namelijk {samsunggoedkoop} euro goedkoper dan de iphone en maar {samsungduur} euro duurder dan de asus')
if (asusgoedkoop or asusgoedkoop1) > int(100):
    print('Het advies is om de asus te kopen. Deze is namelijk 100 euro goedkoper dan allebij.')
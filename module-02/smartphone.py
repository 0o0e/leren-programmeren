iphone_prijs = int(input('Hoe duur is de iphone? '))
samsung_prijs = int(input('Hoe duur is de samsung? '))
if iphone_prijs >= samsung_prijs:
    print(f'De iphone is het duurst, de telefoon kost: {iphone_prijs} euro')
    print(f'De samsung is het goedkoopst, de telefoon kost: {samsung_prijs} euro')
elif samsung_prijs >= iphone_prijs:
    print(f'De samsung is het duurst, de telefoon kost: {samsung_prijs} euro')
    print(f'De iphone is het goedkoopst, de telefoon kost: {iphone_prijs} euro')
    
diff = iphone_prijs - samsung_prijs

if diff <= 50:
    print('Het advies is dus om de iphone te kopen.')
else:
    print('Het advies is dus om de samsung te kopen.')
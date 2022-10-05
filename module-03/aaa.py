pity = int(input('Wat is je pity? '))
fiftyfifty = input('heb je laatst dat je een 5ster kreeg de [a. karakter op de banner] gekregen of [b. een wapen/ standaard banner karakter] a/b ')
aantal_primo = int(input('Hoeveel primogems heb je? '))
aantal_wish = int(input('Hoeveel intertwined fates heb je? '))
primo_to_wish = aantal_primo / 160
totaal_wish = int(aantal_wish + primo_to_wish)
# hoeveel wish besteden om gegarandeerd 5star t krijgen
#90 - 50   = 40
hoeveel_nodig = 90 - pity
totaal = hoeveel_nodig - totaal_wish
if fiftyfifty == 'a':
    print(f'Je hebt nog {totaal} intertwined fate nodig om een 5ster te krijgen. Je hebt 50 procent kans om de karakter op de banner te krijgen, anders krijg je een andere 5ster.')
if fiftyfifty == 'b':
    print(f'Je hebt nog {totaal} intertwined fate nodig om een 5ster te krijgen. Je hebt 100 procent kans om de karakter op de banner te krijgen.')

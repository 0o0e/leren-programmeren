# stap 1, 2,  3 en 4
hoogte = float(input('Wat is de hoogte? '))
breedte = float(input('Wat is de breedte? '))
diepte = float(input('Wat is de diepte? '))
m3 = round(hoogte * breedte * diepte)

uitgravengrond = float(m3 * 25)
afvoerengrond = float(m3 * 32.50)

# voorijkosten = round(2.05 * 10)
# voorrijkosten = voorijkosten + 250

afstand = float(input('Wat is de afstand vanaf het bedrijf naar u? '))
if afstand < 50 and m3 < 20:
    extra = afstand * 1.25
    voorrijkosten = 100.00 + extra
if afstand < 50 and m3 > 20:
    extra = afstand * 2.15
    voorrijkosten = 250.0 + extra
if afstand > 50 and m3 < 20:
    extra = afstand * 1.15
    voorrijkosten = 100.0 + extra
if afstand > 50 and m3 > 20:
    extra = afstand * 2.05
    voorrijkosten = 250.0 + extra

kleur = input('Welke kleur tegels wil je? ')
m2 = float(hoogte * breedte)
if m3 < 20 and kleur == 'rood':
    prijs = 250 * m2
    prijs2 = 25 * m2
    totaalprijs = prijs + prijs2
if m3 > 20 and kleur == 'rood':
    prijs = 200 * m2
    prijs2 = 20 * m2
    totaalprijs = prijs + prijs2

if m3 < 20 and kleur != 'rood':
    prijs = 250 * m2
    prijs2 = 100 * m2
    totaalprijs = prijs + prijs2
if m3 < 20 and kleur != 'rood':
    prijs = 250 * m2
    prijs2 = 125 * m2
    totaalprijs = prijs + prijs2

# lengte * breedte= 24

totaal = float (uitgravengrond + afvoerengrond + voorrijkosten + totaalprijs)

# voorrijkosten kloppen alleen als de klant 60 km verweg woont en als de grootte meer dan 20 m3 is dus ik heb er een input van gemaakt

print(f"""
offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud : {m3} m3)
uitgraven: ${uitgravengrond}
afvoeren: ${afvoerengrond}
voorrijkosten ${voorrijkosten}
beton + tegel ({m2} m2) ${totaalprijs}
totaal: ${totaal}
""")

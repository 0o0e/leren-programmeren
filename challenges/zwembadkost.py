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
    voorrijkosten = 100.0
if afstand < 50 and m3 > 20:
    voorrijkosten = 250.0
if afstand > 50 and m3 < 20:
    voorrijkosten = 100.0
    diff = float(afstand - 50)
    extra = diff * 1.15
if afstand > 50 and m3 > 20:
    voorrijkosten = 250.0
    diff = float(afstand - 50)
    extra = diff * 2.05

totaal = float (uitgravengrond + afvoerengrond + voorrijkosten)

# voorrijkosten kloppen alleen als de klant 60 km verweg woont en als de grootte meer dan 20 m3 is dus ik heb er een input van gemaakt

print(f"""
offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud : 36 m3
uitgraven: ${uitgravengrond}
afvoeren: ${afvoerengrond}
voorrijkosten ${voorrijkosten}
totaal: ${totaal}
""")

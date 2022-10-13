# stap 1
m3 = round(float(8 * 3 * 1.5))
print(m3)

# stap 2 en 3
uitgravengrond = float(m3 * 25)
afvoerengrond = float(m3 * 32.50)
voorijkosten = round(2.05 * 10)
voorrijkosten = voorijkosten + 250
totaal = float (uitgravengrond + afvoerengrond + voorrijkosten)

print(f""" 
offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud : 36 m3
uitgraven: ${uitgravengrond}
afvoeren: ${afvoerengrond}
voorrijkosten ${voorrijkosten}
totaal: ${totaal}
""")

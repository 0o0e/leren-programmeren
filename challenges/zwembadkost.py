# stap 1
m3 = round(float(8 * 3 * 1.5))
print(m3)

# stap 2
uitgravengrond = float(m3 * 25)
afvoerengrond = float(m3 * 32.50)
totaal = float (uitgravengrond + afvoerengrond)
print(f""" 
offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud : 36 m3
uitgraven: ${uitgravengrond}
afvoeren: ${afvoerengrond}
totaal: ${totaal}""")
uren = input('hoeveel uur is het? ')
minuten = input('hoeveel minuten is het? ')


tijdstip = uren+'.'+minuten

print(tijdstip)
tijdstip = float(tijdstip)
over = 24 - tijdstip
over = float(over)

print('je hebt',over,'uur tot de dag voorbij is.')

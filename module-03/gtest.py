try:
    if 'a' < 'b':
        print('ok')
    else:
        print('nok')
except:
    print('error')

while True:
    ff = input('ja of nee ')
    if ff == 'ja':
        continue
    if ff == 'nee':
        break
    else:
        break

kost = float(input('Hoeveel euro kost wc papier? '))
hoevaak = float(input('Hoeveel keer per maand koop je wc papier?'))
tot = kost * hoevaak
print(tot * 12)

welkenummer = int(input('Kies een nummer: '))

while welkenummer != 0:
    if welkenummer > 0:
        welkenummer = welkenummer - 1
    if welkenummer < 0:
        welkenummer = welkenummer + 1
    print(welkenummer)

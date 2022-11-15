dagen = ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')

print('alle dagen van de week zijn ',dagen [:7])
print('alle weekdagen van de week zijn ',dagen [:5])
print('de weekenddagen zijn',dagen[-2:])
dagenomgekeerd = reversed(dagen)
dagenomgekeerd = tuple(dagenomgekeerd)
print('alle dagen van de week omgekeerd is',dagenomgekeerd)
print('de werkdagen in omgekeerde volgorde is',dagenomgekeerd[-5:])
print('de weekenddagen in omgekeerde volgorde is',dagenomgekeerd[:2])

# for d in range(0,4):
#     print(dagen[d])

# aa = reversed(dagen)
# aa = tuple(aa)
# print(aa)

from fruitmand import fruitmand
for i in range (0,len(fruitmand)):
    if fruitmand[i]['name'] == 'druif':
        fruitmand.pop(i)
        break
colors = []
for i in range(0,len(fruitmand)):
    if fruitmand[i]['color'] not in colors:
        colors.append(fruitmand[i]['color'])
print(colors)

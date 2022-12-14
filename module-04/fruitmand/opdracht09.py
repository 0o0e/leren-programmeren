from fruitmand import fruitmand
for i in range (len(fruitmand)):
    if fruitmand[i]['name'] == 'druif':
        fruitmand.pop(i)
        break
colors = []
for i in range(len(fruitmand)):
    if fruitmand[i]['color'] not in colors:
        colors.append(fruitmand[i]['color'])
print(colors)

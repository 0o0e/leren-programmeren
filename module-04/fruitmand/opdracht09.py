from fruitmand import fruitmand
fruitmand.pop(4)
colors = []
for i in range(0,len(fruitmand)):
    if fruitmand[i]['color'] not in colors:
        colors.append(fruitmand[i]['color'])
print(colors)

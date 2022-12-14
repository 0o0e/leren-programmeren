from fruitmand import fruitmand

kleuren = {
    0 : 'geel',
    1 : 'groen',
    2 : 'oranje',
    3 : 'geel',
    4 : 'rood',
    5 : 'bruin',
    6 : 'geel',
}

for i in range(len(fruitmand)):
    # fruitmand[i] = fruitmand[i] | {'color': [kleuren[i]]}
    fruitmand[i] += fruitmand[i]['color' : [kleuren[i]]]

max_lengte = 0
for i in fruitmand:
    if len((i)['name']) > max_lengte:
        max_lengte = len((i)['name'])
        name = i['name']
        kleur = i['color']
        gewicht = i['weight']
print(f'de {name} ({max_lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht}.')

from fruitmand import fruitmand


bewerkte_fruitmand = sorted(fruitmand, key = lambda weight:weight['weight'], reverse = True)
for i in range(0,len(bewerkte_fruitmand)):
    print((bewerkte_fruitmand[i]['name']), (bewerkte_fruitmand[i]['weight']))
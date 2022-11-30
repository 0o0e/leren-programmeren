from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight': 1000,
})

totaal = 0
for i in range(0,len(fruitmand)):
    totaal = totaal + fruitmand[i]['weight']
print(totaal)

from fruitmand import fruitmand
teller = 0
for i in range(0,len(fruitmand)):
    if fruitmand[teller]['round']: print(fruitmand[teller]['name'])
    teller += 1
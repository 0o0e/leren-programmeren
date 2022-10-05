i = 50
som = 0

while som < 1000:
    som += i
    print(f'{i} + {i + 1} = {som}')
    i += 1
    if i == 1000:
        break

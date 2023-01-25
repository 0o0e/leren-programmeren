
def namen_en_leeftijd():
    lijst = []
    while True:
        naam = input('noem een naam: ')
        leeftijd = input('noem een leeftijd: ')
        lijst.append({
            'name' : naam,
            'age' : leeftijd
        })
        stoppenofniet = input('Toets enter om door te gaan of stop om te printen ')
        if stoppenofniet == 'stop':
            break
    for i in lijst:
        name = i['name']
        age = i['age']
        print(f'{name} is {age} jaar')


namen_en_leeftijd()

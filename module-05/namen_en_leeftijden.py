

def namen_leeftijden(dict):
    for i in dict:
        print(i,'is',dict[i],'jaar oud')

gegevens={}
stoppenofniet = 'ja'
while stoppenofniet != 'stop':
    naam = input('noem een naam: ')
    leeftijd = input('noem een leeftijd: ')
    gegevens.update({naam :leeftijd})
    stoppenofniet = input('Toets enter om door te gaan of stop om te printen ')
namen_leeftijden(gegevens)
print(gegevens)


def namen_leeftijden(dict):
    for i in dict:
        print(i,'is',dict[i],'jaar oud')
def input_naamleeftijd():
    gegevens={}
    naam = input('noem een naam: ')
    leeftijd = input('noem een leeftijd: ')
    gegevens.update({'name' :naam})
    gegevens.update({'age' :leeftijd})
    
    return gegevens




stoppenofniet = 'ja'
lijst = []

while stoppenofniet != 'stop':
    naam = input_naamleeftijd()
    lijst.append(naam)
    stoppenofniet = input('Toets enter om door te gaan of stop om te printen ')
for dict in lijst:
    print(f"{dict['name']} is {dict['age']} jaar oud ")

# pc testt hello
# testest
for i in range(3):
    print("aa")
# deletelater
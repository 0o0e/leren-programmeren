a = int(input('noem een heel getal: '))
b = int(input('noem een ander heel getal: '))
if a > b:
    max = a
    min = b
    print('a is het grooste getal:',max,)
elif a < b:
    min = a
    max = b
    print('a is het kleinste getal:',min,)
else:
    a == b
    print('a en b zijn even groot')

print('het minimum is',min)
print('het maximum is',max)


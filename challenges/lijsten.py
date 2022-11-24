num1 = 1
num2 = 1

while num1!= 14:
    som = num1 * num2
    print(f'{num1} * {num2} = {som}')
    num2 += 1
    if num2 == 13:
        num1 += 1
        num2 = 1
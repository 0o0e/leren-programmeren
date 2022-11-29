#opdr 1=
# num1 = 1
# num2 = 1
# while num1!= 14:
#     som = num1 * num2
#     print(f'{num1} * {num2} = {som}')
#     num2 += 1
#     if num2 == 13:
#         num1 += 1
#         num2 = 1

# opdr 2 =
lijst = [5, 12, 19, 27, 3]
# opdr 3=
lijst.append(25)
# opdr 4
print(len(lijst))
# opdr 5 =
print(lijst)
lijst.remove(12)
print(lijst)
# opdr 6=
del lijst[0]
print(lijst)
# opdr 7 =
lijst.insert(0,36)
print(lijst)
# opdr 8=
opgetelt = (lijst[0]) + (lijst[1]) + (lijst[2]) + (lijst[3]) + (lijst[4])
print(opgetelt)
# opdr 9=
lijst = []
print(lijst)
# opdr 10=
lijst.extend(range(1,4))
print(lijst)
# opdr 11=
lijst.extend(range(4,51))
print(lijst)
# opdr 12=
print(lijst[25])
# opdr 13=
lijst[0], lijst[49] = lijst[49],lijst[0]
print(lijst)
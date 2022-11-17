dag = input('welke dag van de week is het?(ma,di,wo,do,vr,za of zo) ')
dagen = ['ma','di','wo','do','vr','za','zo']
aaa = dagen[dagen.index(dag)+1:]
while len(aaa) > 0:
    print(aaa[0])
    aaa = aaa [1:]

dagIndex = 0

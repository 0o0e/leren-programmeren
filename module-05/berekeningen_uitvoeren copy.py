def addition(number1: int,number2:int):
    return number1 + number2


def subtraction(number1: int,number2:int):
    return number1 - number2

def multiplication(number1: int,number2:int):
    return number1 * number2

def division(number1: int,number2:int):
    return number1 / number2

uitkomst = ''
n1 = 0
while True:
    if uitkomst == '':
        choice=input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ').lower()
    else:
        choice = input(f'Wil je wat met de uitkomst ({uitkomst}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ').lower()
        if choice == 'i':
            break
    
    if uitkomst != n1:
        n1 = int(input('noem een getal: '))
    else:
        n1 = uitkomst

    if choice == 'e' or choice == 'f': 
        n2 = 1
    elif choice == 'g' or choice == 'h':
            n2 = 2
    else:
        n2 = int(input('noem nog een getal: '))


    if choice == 'a' or choice == 'e':
        uitkomst =(addition(n1,n2))
        n1 = uitkomst
    if choice =='b' or choice == 'f':
        uitkomst=(subtraction(n1,n2))
        n1 = uitkomst
    if choice =='c' or choice == 'g':
        uitkomst=(multiplication(n1,n2))
        n1 = uitkomst 
    if choice =='d' or choice == 'h':
        uitkomst=(division(n1,n2))
        n1 = uitkomst

    # if choice == 'e' or choice == 'f':
    #     n2 = 1
    #     if n1 != uitkomst:
    #         n1 = int(input('noem een getal: '))
    #     else: 
    #         n1 = uitkomst
    # if choice == 'e':
    #     uitkomst= (addition(n1,n2))
    #     n1 = uitkomst
    # if choice == 'f':
    #     uitkomst= (subtraction(n1,n2))
    #     n1 = uitkomst

    # if choice == 'g' or choice == 'h':
    #     n2 = 2
    #     if uitkomst != n1:
    #         n1 = int(input('noem een getal: '))
    #     else: n1 = uitkomst
    #     if choice == 'g':
    #         uitkomst= (multiplication(n1,n2))
    #         n1 = uitkomst
    #     if choice == 'h':
    #         uitkomst = (division(n1,n2))
    #         n1 = uitkomst
    print(uitkomst)


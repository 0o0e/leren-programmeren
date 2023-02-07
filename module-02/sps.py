import random
def steenpapierschaar():
    uitkomst = ''
    choices = ['rock','paper','scissors']
    steenpapierschaar = random.choice (choices)
    mychoice = input('rock, paper or scissors? ').lower()
    print(f'computers choice = {steenpapierschaar} \n\
    ')
    print(f'your choice = {mychoice} \n\
    ')
    if steenpapierschaar == mychoice:
        uitkomst = 'tie'
    elif mychoice == 'rock':
        if steenpapierschaar == 'paper':
            uitkomst = 'lose'
        if steenpapierschaar == 'scissors':
            uitkomst = 'win'
    elif mychoice == 'paper':
        if steenpapierschaar == 'rock':
            uitkomst = 'win'
        if steenpapierschaar == 'scissors':
            uitkomst='lose'
    elif mychoice == 'scissors':
        if steenpapierschaar == 'rock':
            uitkomst = 'lose'
        if steenpapierschaar == 'paper':
            uitkomst= 'win'
    print(f"it's a {uitkomst} ! ")

steenpapierschaar()
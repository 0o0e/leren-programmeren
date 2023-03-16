from functions import *
from data import *

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    
    

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold,interestingInvestors)
    goldCut = 0.0
    fellowship = [mainCharacter] + adventuringFriends + adventuringInvestors

    # verdeel de uitkomsten
    friends_extramoney = 0
    for friend in friends:
        if friend['shareWith'] == True and friend['adventuring'] == True:
            friends_extramoney += 10
        
    begincash = round(getPersonCashInGold(mainCharacter['cash']),2)
    eindcash = begincash + friends_extramoney+ ((profitGold - sum(getInvestorsCuts(profitGold,interestingInvestors))) / len(fellowship))
    earnings.append({
    'name'   : mainCharacter['name'],
    'start'  : begincash,
    'end'    : eindcash
    })

    for i in friends:
        if i['adventuring'] == True and i['shareWith'] == True:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash = (begincash + ((profitGold - sum(getInvestorsCuts(profitGold,interestingInvestors))) / len(fellowship))) - 10

        else:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash = begincash
        earnings.append({
        'name'   : i['name'],
        'start'  : begincash,
        'end'    : eindcash
        })




    for i in investors:
        if i['adventuring'] == True and i['profitReturn'] <= 10:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash =  (round(profitGold / 100 * i[ 'profitReturn'] , 2)) + begincash + ((profitGold - sum(getInvestorsCuts(profitGold,interestingInvestors))) / len(fellowship))
        elif i['adventuring'] == False and i['profitReturn'] <= 10:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash =  (round(profitGold / 100 * i[ 'profitReturn'] , 2)) + begincash
        else:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash = begincash
        earnings.append({
        'name'   : i['name'],
        'start'  : begincash,
        'end'    : eindcash
        })



    return earnings

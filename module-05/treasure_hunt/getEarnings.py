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
    fellowship = len(mainCharacter) + len(adventuringFriends) + len(adventuringInvestors)

    # verdeel de uitkomsten
    for i in interestingInvestors:
        if i['adventuring'] == True:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash =  (round(profitGold / 100 * i[ 'profitReturn'] , 2)) + begincash + getAdventurerCut(profitGold,investorsCuts,fellowship) + 3
            earnings.append({
            'name'   : i['name'],
            'start'  : begincash,
            'end'    : eindcash
            })
        else:
            begincash = round(getPersonCashInGold(i['cash']),2)
            eindcash =  (round(profitGold / 100 * i[ 'profitReturn'] , 2)) + begincash
            # eindcash_adventurer_investors = getAdventurerCut(profitGold,investorsCuts,)
            earnings.append({
            'name'   : i['name'],
            'start'  : begincash,
            'end'    : eindcash
            })

    # for i in adventuringInvestors:
    #     begincash = round(getCashInGoldFromPeople(adventuringInvestors),2)
    #     eindcash = round((getAdventurerCut(profitGold,investors,fellowship)))
    #     earnings.append({
    #     'name'   : i['name'],
    #     'start'  : begincash,
    #     'end'    : eindcash
    #     })

    
    # for i in mainCharacter:
    #     begincash = 


    return earnings

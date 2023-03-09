from functions import *

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold,interestingInvestors)
    goldCut = 0.0

    # verdeel de uitkomsten
    for i in interestingInvestors:
        begincash = round(getPersonCashInGold(i['cash']))
        eindcash_excluding_adventurer = round((getInvestorsCuts(profitGold,interestingInvestors)) + begincash,2) 
        # eindcash_adventurer_investors = getAdventurerCut(profitGold,investorsCuts,)
        earnings.append({
        'name'   : i['name'],
        'start'  : begincash,
        'end'    : eindcash_excluding_adventurer
        })


    # for person in people:



        #code aanvullen

        # earnings.append({
        #     'name'   : '??',
        #     'start'  : 0.0,
        #     'end'    : 0.0
        # })

    return earnings





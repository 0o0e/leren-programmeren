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
        begincash = round(getPersonCashInGold(i['cash']),2)
        eindcash =  (round(profitGold / 100 * i[ 'profitReturn'] , 2)) + begincash
        # eindcash_adventurer_investors = getAdventurerCut(profitGold,investorsCuts,)
        earnings.append({
        'name'   : i['name'],
        'start'  : begincash,
        'end'    : eindcash
        })
    # for i in adventuringInvestors:
    #     begincash = round(getPersonCashInGold(i['cash']),2)
    #     eindcash = round((getAdventurerCut(profitGold,investors,fellowship)))
    #     earnings.append({
    #     'name'   : i['name'],
    #     'start'  : begincash,
    #     'end'    : eindcash
    #     })

    
    # for i in mainCharacter:
    #     begincash = 


    return earnings


testMainCharacter2 = {
    'name' : 'TestChar2',
    'cash' : {
        'platinum' : 1,
        'gold' : 4,
        'silver' : 4,
        'copper' : 10
    }
}

inverstorsTestList2 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 10,
    'adventuring' : False,
    'cash' : {
        'platinum' : 10,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor2',
    'profitReturn' : 5,
    'adventuring' : False,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor3',
    'profitReturn' : 9,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 100,
        'silver' : 0,
        'copper' : 0
    }
}]

print(getEarnigs(10.5,{},[],inverstorsTestList2))




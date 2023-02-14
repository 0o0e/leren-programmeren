import time
from termcolor import colored
from data import JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY


##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    answer =amount / 10
    return answer

def silver2gold(amount:int) -> float:
    answer =amount / 5
    return answer

def copper2gold(amount:int) -> float:
    amount = copper2silver(amount)
    answer = silver2gold(amount)
    return answer


def platinum2gold(amount:int) -> float:
    answer =amount *25
    return answer

def getPersonCashInGold(personCash:dict) -> float:
    answer = 0

    for key, value in personCash.items():
        if key == 'platinum':
            answer += platinum2gold(value)
        elif key == 'silver':
            answer+= silver2gold(value)
        elif key == 'copper':
            answer += copper2gold(value)
        elif key == 'gold':
            answer += value
        
    return answer

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_amount = people * 4
    horse_amount = horses * 3
    gold=copper2gold(people_amount) + copper2gold(horse_amount)
    total = gold * JOURNEY_IN_DAYS
    return round(total,2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    newlist =[]
    for i in range (0,len (list)):
        if list[i][key] == value:
            newlist.append(list[i])
    return newlist
    

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,'adventuring',True)


def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'shareWith',True)

def getAdventuringFriends(friends:list) -> list:
    newlist= []
    for teller in range (0,len(friends)):
        if friends[teller]['adventuring'] and friends[teller]['shareWith']: 
            newlist.append(friends[teller])
    return newlist
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
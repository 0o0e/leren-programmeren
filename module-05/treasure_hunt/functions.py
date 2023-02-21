import time, math
from termcolor import colored
from data import JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY,COST_TENT_GOLD_PER_WEEK,COST_HORSE_SILVER_PER_DAY



##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    amount = copper2silver(amount)
    return silver2gold(amount)


def platinum2gold(amount:int) -> float:
    return amount *25

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
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)


def getTotalRentalCost(horses:int, tents:int) -> float:
    COST_TENT_GOLD_PER_DAY = COST_TENT_GOLD_PER_WEEK *2
    COST_HORSE_GOLD_PER_DAY = silver2gold(COST_HORSE_SILVER_PER_DAY)
    return (COST_TENT_GOLD_PER_DAY * tents) + ((COST_HORSE_GOLD_PER_DAY * horses) * JOURNEY_IN_DAYS) 

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    aa = ''
    for i in range (0, len(items)):
        aa += str(items[i]['amount'])  + items[i]['unit'] + ' '+ items[i]['name']
        if i < len(items) -1:
            aa += ', '
    return aa
        

def getItemsValueInGold(items:list) -> float:
    amount_gold = 0
    for i in range (0,len(items)):
        if items[i]['price']['type'] == 'copper':
            amount_in_copper =items[i]['price']['amount']
            amount_gold += copper2gold(amount_in_copper) * items[i]['amount']
            # amount_gold += amount_gold * items[i]['amount']

        elif items[i]['price']['type'] == 'silver':
            amount_in_silver =items[i]['price']['amount']
            amount_gold += silver2gold(amount_in_silver) * items[i]['amount']

        elif items[i]['price']['type'] == 'platinum':
            amount_in_platinum =items[i]['price']['amount']
            amount_gold += platinum2gold(amount_in_platinum) * items[i]['amount']

        elif items[i]['price']['type'] == 'gold':
            amount_in_gold = items[i]['price']['amount']
            amount_gold += amount_in_gold * items[i]['amount']
    return amount_gold

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
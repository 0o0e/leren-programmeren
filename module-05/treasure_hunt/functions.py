import time, math
from termcolor import colored
from data import JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY,COST_TENT_GOLD_PER_WEEK,COST_HORSE_SILVER_PER_DAY,COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT




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
    amount_gold = 0

    for key, value in personCash.items():
        if key == 'platinum':
            amount_gold += platinum2gold(value)
        elif key == 'silver':
            amount_gold+= silver2gold(value)
        elif key == 'copper':
            amount_gold += copper2gold(value)
        elif key == 'gold':
            amount_gold += value
        
    return amount_gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_amount = people * COST_FOOD_HUMAN_COPPER_PER_DAY
    horse_amount = horses * COST_FOOD_HORSE_COPPER_PER_DAY
    gold=copper2gold(people_amount) + copper2gold(horse_amount)
    total = gold * JOURNEY_IN_DAYS
    return round(total,2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    newlist =[]
    for item in list:
        if item[key] == value:
            newlist.append(item)
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
    tents_total_cost = math.ceil(JOURNEY_IN_DAYS / 7) * COST_TENT_GOLD_PER_WEEK * tents
    horses_total_cost = (silver2gold(COST_HORSE_SILVER_PER_DAY)) * horses * JOURNEY_IN_DAYS
    return tents_total_cost + horses_total_cost

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
    for i in items:
        if i['price']['type'] == 'copper':
            amount_gold += (copper2gold(i['price']['amount'])) * i['amount']
        elif i['price']['type'] == 'silver':
            amount_gold += (silver2gold(i['price']['amount'])) * i['amount']
        elif i['price']['type'] == 'platinum':
            amount_gold += (platinum2gold(i['price']['amount'])) * i['amount']
        elif i['price']['type'] == 'gold':
            amount_gold += i['price']['amount'] * i['amount']
    return amount_gold

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_cash = 0
    for person in people:
        total_cash += platinum2gold(person['cash']['platinum'])
        total_cash += silver2gold(person['cash']['silver'])
        total_cash += copper2gold(person['cash']['copper'])
        total_cash += (person['cash']['gold'])
    return total_cash

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    interestinginvestors =[]
    for i in investors:
        if i['profitReturn'] <= 10:
            interestinginvestors.append(i)
    return interestinginvestors

def getAdventuringInvestors(investors:list) -> list:
    investors =getInterestingInvestors(investors)
    investors =getAdventuringPeople(investors)
    return investors


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    investors = getAdventuringInvestors(investors)

    food_cost = getJourneyFoodCostsInGold(1,1)
    gear_cost = getItemsValueInGold(gear)
    rental_cost = getTotalRentalCost(1,1)

    total = (rental_cost + food_cost + gear_cost) * len(investors)
    return total


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    humancost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    horsescost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    total = leftoverGold // (humancost + horsescost)
    return total

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    humancost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    horsescost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    total = (humancost + horsescost) * nightsInInn
    return round(total,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    newlist = []
    for investor in getInterestingInvestors(investors):
        antw = (profitGold / 100) * investor['profitReturn']
        newlist.append(round(antw,2))
    return newlist


def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    for investor_cut in investorsCuts:
        profitGold = profitGold - investor_cut
    return round((profitGold / fellowship),2)

##################### M04.D02.O13 #####################
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
    adventurers_cut = ((profitGold - sum(investorsCuts)) / len(fellowship))
    

    # verdeel de uitkomsten
    friends_extramoney = 0


    for friend in friends:
        if friend['shareWith'] == True and friend['adventuring'] == True:
            friends_extramoney += 10
    for i in people:
        begincash = round(getPersonCashInGold(i['cash']),2)
        if i == mainCharacter:    
            eindcash = round(begincash + friends_extramoney+ adventurers_cut,2)
        if i in friends:
            if i['adventuring'] == True and i['shareWith'] == True:
                eindcash = round(begincash + adventurers_cut - 10, 2)
            else:
                eindcash = begincash
        if i in investors:
            if i['adventuring'] == True and i['profitReturn'] <= 10:
                eindcash =  round(profitGold / 100 * i[ 'profitReturn'] , 2) + begincash + adventurers_cut
            elif i['adventuring'] == False and i['profitReturn'] <= 10:
                eindcash =  round(profitGold / 100 * i[ 'profitReturn'] , 2) + begincash
            else:
                eindcash = begincash
        earnings.append({
        'name'   : i['name'],
        'start'  : begincash,
        'end'    : eindcash
        })



    return earnings





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
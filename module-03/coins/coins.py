# name of student: esma
# number of student: 99072495
# purpose of program: counting how much money to return
# function of program: it counts how much to pay and how much is paid and then tell the user how much to give back
# structure of program: 


toPay = int(float(input('Amount to pay: '))) # how much the client has to pay
paid = int(float(input('Paid amount: '))) # how much the client paid
change = paid - toPay # how much the user has to give back to the client
tel = 0 
if change > 0: # if there is change there is a coinvalue otherwise there is no change so no need for a value
  coinValue = 5 # 50 cents

  while change > 0 and coinValue > 0: # while the change is not given back this loop will continue
    nrCoins = change // coinValue #
    if nrCoins > 0: # 
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' euro!' ) # here it prints how manycoins you need to return
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' euros did you return? ')) #
        change -= nrCoinsReturned * coinValue # The change is being paid. coins returned times coinvalue is how much is returned. then change minus that is how much is left.
        tel = tel + nrCoinsReturned
        print(f'{tel} coins of {coinValue} euro')
        tel = 0

# comment on code below: if the value is 5, first it goes through the while loop and then it turns into 3. then the value 3 goes through the while loop and turns in 2, and so it continues.
    if coinValue == 5:
        coinValue = 3
    elif coinValue == 3:
        coinValue = 2
    elif coinValue == 2:
        coinValue = 0.50
    elif coinValue == 0.50:
      coinValue = 0.20
    elif coinValue == 0.20:
      coinValue = 0.10
    elif coinValue == 0.10:
      coinValue = 0.05
    elif coinValue == 0.05:
      coinValue = 0.02
    elif coinValue == 0.02:
      coinValue = 0.01
    else:
      coinValue = 0



if change > 0: #if change is not returned, it prints that it is not returned. if all the change is given back it prints 'done'
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
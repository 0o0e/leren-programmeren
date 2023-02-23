
while True: 
  try:
    score_e = int(input('Wat is je score voor excellente acties? (maximaal 6) '))
    if score_e <= 6:
     break
  except:
    print('alleen nummers van 0 tot 6')

while True:
  try:
    score_p = int(input('Wat is je score voor professionele acties? (maximaal 8) '))
    if score_p <=8:
        break
  except: 
    print('alleen nummers van 0 tot 8')

while True:
  try:
    score_o = int(input('Wat is je score voor onprofessionele acties? (maximaal 5) '))
    if score_o <= 5:
        break
  except:
    print('alleen nummer van 0 tot 5')


while True:
  try:
    score_s = int(input('Wat is je score voor slechte acties? (maximaal 2) '))
    if score_s <= 2:
        break
  except:
    print('alleen nummers tussen 0 en 2')


totalscore = score_e + score_p - score_o - score_s
if (score_p == 8) and (score_e >= 4) and (score_o == 0) and (score_s == 0):
    print('De examenuitslag is Goed')
elif ((score_s == 0) and (totalscore >= 7) and (totalscore <= 13)) or ((score_s == 1) and (totalscore >= 9)):
    print('De examenuitslag is Voldoende')
else:
    print('De examenuislag is Onvoldoende')
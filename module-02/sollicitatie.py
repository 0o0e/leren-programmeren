naam = input('Wat is uw naam? ')


ervaring_jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? ')) #5
ervaring_dieren = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ')) #4
ervaring_acrobatiek = int(input('Hoeveel jaar prakttijkervaring heeft u met acrobatiek? ')) #3
mbo = input('Bent u in bezit van een MBO 4 diploma ondernemen? (ja/nee) ')
rijbewijs = input('Bent u in bezit van een vrachtwagen rijbewijs? (ja/nee) ')
hoed = input('Bent u in bezit van een hoge hoed? (ja/nee) ')
geslacht = input('Bent u een man of een vrouw? (m/v) ')
lengte = int(input('Wat is uw lichaamslengte in cm? ')) #150
gewicht = int(input('Wat is uw lichaamsgewicht ing kg? ')) #90 
certificaat = input("Heeft u het Certificaat 'personeel overleven met gevaarlijk'? (ja/nee) ")


if  geslacht == 'm':
    snor =input('Heeft u een snor breder dan 10 cm? (ja/nee) ')
    haar = 'nee'
if geslacht == 'v':
    haar = input('Draagt u rood krulhaar langer dan 20 cm? (ja/nee) ')
    snor = 'nee'

if  ervaring_jongleren >= 5: 
    heeft_ervaring_jongleren = True
if  ervaring_acrobatiek >= 3:
    heeft_ervaring_acrobatiek = True
if  ervaring_dieren >= 4:
    heeft_ervaring_dieren = True
if  mbo == 'ja':
    heeft_mbo = True
if  rijbewijs == 'ja':
    heeft_rijbewijs = True
if  hoed == 'ja':
    heeft_hoed = True

if  snor == 'ja':
    heeft_snor = True
if  haar == 'ja':
    heeft_haar = True

if  lengte >= 150:
    heeft_lengte = True
if  gewicht >= 90:
    heeft_gewicht = True
if  certificaat == 'ja':
    heeft_certificaat = True

fitforjob = (heeft_ervaring_acrobatiek or heeft_ervaring_dieren or heeft_ervaring_jongleren) and (heeft_snor or heeft_haar) and heeft_lengte and heeft_gewicht and heeft_certificaat and heeft_mbo and heeft_rijbewijs and heeft_hoed 

if fitforjob:
    print('je bent uitgenodigd voor een interview ')
else:
    print ('je bent niet geslaagd')
 
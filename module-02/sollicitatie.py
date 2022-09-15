from distutils import errors
from distutils.log import error
from ftplib import error_perm
from logging import exception


naam = input('Wat is uw naam? ')

geslacht = input('Bent u een man of een vrouw? (m/v) ')
if  geslacht == 'm':
    snor =input('Heeft u een snor breder dan 10 cm? (ja/nee) ')
if geslacht == 'v':
    haar = input('Draagt u rood krulhaar langer dan 20 cm? (ja/nee) ')

ervaring_jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? ')) #5
heeft_ervaring_jongleren = ervaring_jongleren >= 5

ervaring_acrobatiek = int(input('Hoeveel jaar prakttijkervaring heeft u met acrobatiek? ')) #3
heeft_ervaring_acrobatiek = ervaring_acrobatiek >= 3

ervaring_dieren = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ')) #4 
heeft_ervaring_dieren = ervaring_dieren >4

mbo = input('Bent u in bezit van een MBO 4 diploma ondernemen? (ja/nee) ')
heeft_mbo = mbo == 'ja'

rijbewijs = input('Bent u in bezit van een vrachtwagen rijbewijs? (ja/nee) ')
heeft_rijbewijs = rijbewijs == 'ja'

kleur = input('wat is je lievelingskleur? ')
if kleur == 'blauw':
    raise NameError('mensen met de lievelingskleur blauw zijn hier niet welkom')


naam = input('Begint je naam meet de letter a, e, i, of u? ')
if naam == 'ja':
    raise Exception('mensen met de beginletters a, e , i of u zijn niet welkom')


hoed = input('Bent u in bezit van een hoge hoed? (ja/nee) ')
heeft_hoed = hoed == 'ja'

lengte = int(input('Wat is uw lichaamslengte in cm? ')) #150
heeft_lengte = lengte >=150

gewicht = int(input('Wat is uw lichaamsgewicht ing kg? ')) #90 
heeft_gewicht = gewicht >= 90

idk = input('houd je van kikkers? ')
if idk =='nee':
    raise Exception('alleen mensen die van kikkers houden zijn hier welkom')


certificaat = input("Heeft u het Certificaat 'personeel overleven met gevaarlijk'? (ja/nee) ")
heeft_certificaat = certificaat == 'ja'

if geslacht == 'm':
 if  snor == 'ja':
    heeft_snor = True
 if geslacht == 'v':
    heeft_snor = False

manmetsnor = heeft_snor = True

if geslacht == 'v':
    if haar == 'ja':
     heeft_haar = True
    if geslacht == 'm':
     heeft_haar = False

vrouwmethaar = heeft_haar = True


fitforjob = (heeft_ervaring_acrobatiek or heeft_ervaring_dieren or heeft_ervaring_jongleren) and (manmetsnor or vrouwmethaar) and heeft_lengte and heeft_gewicht and heeft_certificaat and heeft_mbo and heeft_rijbewijs and heeft_hoed 

if fitforjob:
    print('gefeliciteerd',naam,',je bent uitgenodigd voor een interview!')
else:
    print ('sorry',naam,',je bent niet geslaagd.')
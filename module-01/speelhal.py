personen = input('Met hoeveel personen ben je in totaal? ')
personen = float (personen)
prijs_tickets = 7.45 * personen

vip_vr = input ('Hoeveel minuten ga je in totaal in de vip vr gameset? ')
vip_vr = float (vip_vr)

prijs_vip = 0.074 * vip_vr 

totaalprijs = prijs_tickets + prijs_vip
print('Dit geweldige dagje-uit met', personen ,'mensen in de Speelhal met', vip_vr ,'minuten VR kost je maar', totaalprijs ,'euro')

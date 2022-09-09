personen = int (input('Met hoeveel personen ben je in totaal? '))
prijs_tickets = 7.45 * personen

vip_vr = int (input ('Hoeveel minuten ga je in totaal in de vip vr gameset? '))

prijs_vip = 0.074 * vip_vr

totaalprijs = (prijs_tickets + prijs_vip) * 100

print('Dit geweldige dagje-uit met', personen ,'mensen in de Speelhal met', vip_vr ,'minuten VR kost je maar', totaalprijs ,'cent')

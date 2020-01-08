#invoer
getal = int(input('Geef getal: '))

#berekening
deler = 2
while getal % deler != 0 and getal > 2:
    deler += 1
    if deler == getal and getal % deler == 1:
        print('{} is een priemgetal'.format(getal))
    elif getal % deler == 0:\
        print('{} is geen priemgetal'.format(getal))

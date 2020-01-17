#invoer
getal = float(input('Geef het getal: '))

#berekening
som = 0
n = 1
aantal_keer = 0

while som < getal:
    som += 1 / (n * 2)
    n *= 2
    aantal_keer += 1

#uitvoer
print('{} {}'.format(aantal_keer, som))





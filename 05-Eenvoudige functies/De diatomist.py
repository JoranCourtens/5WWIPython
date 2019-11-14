#invoer
from math import pi
r_klein = float(input('Geef de straal van de kleine cirkel: '))
r_groot = float(input('Geef de straal van de grote cirkel: '))

#berekening
aantal_cirkels = int(0.83 * (r_groot ** 2) / (r_klein ** 2) - 1.9)
procent_bedekt = float((aantal_cirkels * (r_klein ** 2) * pi) / ((r_groot ** 2) * pi) * 100)

#uitvoer
uitvoer = '{:d} kleine cirkels bedekken {:.2f}% van de grote cirkel'
print(uitvoer.format(aantal_cirkels, procent_bedekt))


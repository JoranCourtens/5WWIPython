#invoer

getal_1 = int(input('Geef getal 1: '))
getal_2 = int(input('Geef getal 2: '))

#berekening
getal_3 = getal_1 + getal_2

uitvoer = '{0:6d} + {1:6<d} = {2:d}'

#uitvoer
print(uitvoer.format(getal_1, getal_2, getal_3))
print(uitvoer.format((getal_1 * 10 ** 1), (getal_2 * 10**1), (getal_3 * 10**1)))
print(uitvoer.format((getal_1 * 10 ** 2), (getal_2 * 10**2), (getal_3 * 10**2)))
print(uitvoer.format((getal_1 * 10 ** 3), (getal_2 * 10**3), (getal_3 * 10**3)))
print(uitvoer.format((getal_1 * 10 ** 4), (getal_2 * 10**4), (getal_3 * 10**4)))

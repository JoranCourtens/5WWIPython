#invoer
t = int(input('Geef aantal nanoseconden: '))

#berekening
t = t * 10**-9
c = 299792458
n = 1.000277

d = (c * t) / (2 * n)

#uitvoer
print(d, 'meter')

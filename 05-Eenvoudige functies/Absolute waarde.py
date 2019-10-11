#invoer

x = float(input('Geef x: '))
y = float(input('Geef y: '))

#berekening

absolute_waarde_1 = abs(abs(x) - abs(y))
absolute_waarde_2 = abs(x - y)

#uitvoer
print(float(round(absolute_waarde_1, 4)), str('≤'), float(round(absolute_waarde_2, 4)))

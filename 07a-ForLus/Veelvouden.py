#invoer
getal = int(input('Geef getal: '))

#berekening
som = 0
for veelvoud in range(getal, 101, getal):
    som+=veelvoud

#uitvoer
print(som)

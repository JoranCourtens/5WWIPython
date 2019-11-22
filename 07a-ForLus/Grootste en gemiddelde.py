#invoer
aantal = int(input('Aantal getallen: '))

#berekening
#Lees het eerste getal voor de lus in
getal_0 = int(input('Geef getal: '))

#Het eerste getal is onmiddelijk de som en het grootste getal
som, grootste = getal_0, getal_0

for i in range(aantal - 1):
    getal = int(input('Geef getal: '))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal

#uitvoer
uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'
print(uitvoer.format(grootste, gemiddelde))

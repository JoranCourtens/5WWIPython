#invoer
a = int(input('Geef getal a: '))
b = int(input('Geef getal b: '))

#berekening
deler = 1
som_a = 0
som_b = 0

for deler in range(1, a):
    if a % deler == 0:
        som_a += deler
    deler += 1

if som_a == b:
    uitvoer = '{} en {} zijn bevriende getallen'
else:
    uitvoer = '{} en {} zijn geen bevriende getallen'

#uitvoer
print(uitvoer.format(a, b))

#invoer
prijs = 0
prijs_product = float(input('Geef de prijs van product: '))

#berekening
while prijs_product > 0:
    prijs += prijs_product
    prijs_product = float(input('Geef de prijs van product: '))
uitvoer = 'De totale prijs is € {:.2f}'
print(uitvoer.format(prijs))





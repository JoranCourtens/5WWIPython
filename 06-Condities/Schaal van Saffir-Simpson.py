#invoer
windsnelheid = int(input('Geef de windsnelheid per uur: '))

#berekening
if windsnelheid < 119:
    print('geen orkaan')
elif windsnelheid <= 153:
    print('categorie 1')
elif windsnelheid <= 177:
    print('categorie 2')
elif windsnelheid <= 209:
    print('categorie 3')
elif windsnelheid <= 249:
    print('categorie 4')
elif windsnelheid >= 250:
    print('categorie 5')

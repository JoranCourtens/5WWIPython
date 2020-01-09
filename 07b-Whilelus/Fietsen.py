#invoer
snelheid_stijn = int(input('Snelheid Stijn: '))
snelheid_kaat = int(input('Snelheid Kaat: '))
afstand_huizen = int(input('Afstand huizen: '))

#berekening
seconden = 0
afstand = 0
while afstand < afstand_huizen:
    seconden += 1
    afstand += (snelheid_kaat + snelheid_stijn)

print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(seconden))



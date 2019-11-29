#invoer
totale_waarde = 0
waarde_kaart = int(input('Geef de waarde van de kaart: '))

#berekening
while totale_waarde < 21 and waarde_kaart > 0:
    totale_waarde += waarde_kaart
    if totale_waarde < 21:
        waarde_kaart = int(input('Geef de waarde van de kaart: '))
if totale_waarde < 21:
    print('Voorzichtig gespeeld ({})'.format(totale_waarde))
elif totale_waarde > 21:
    print('Verbrand ({})'.format(totale_waarde))
else:
    print('Gewonnen!')

#invoer
dikte_papier = int(input('Dikte papier: '))
afstand = int(input('Geef afstand Aarde-hemellichaam: '))
aantal_keer_vouwen = 0

#berekening
while dikte_papier < afstand:
    dikte_papier *= 2
    aantal_keer_vouwen = aantal_keer_vouwen + 1

print('Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(aantal_keer_vouwen, dikte_papier))

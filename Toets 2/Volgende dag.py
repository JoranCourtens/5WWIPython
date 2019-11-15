#invoer
dag = int(input('Geef de dag: '))
maand = int(input('Geef de maand: '))
jaar = int(input('Geef het jaar: '))

#berekening
schrikkeljaar = (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0)
volgende_dag = dag + 1
volgende_maand = maand + 1
volgend_jaar = jaar + 1
if dag < 28:
    print('{:d}/{:d}/{:d}'.format(int(volgende_dag), int(maand), int(jaar)))
elif dag == 28 and maand == 2 and schrikkeljaar == True:
    print('{:d}/{:d}/{:d}'.format(int(volgende_dag), int(maand), int(jaar)))
elif dag == 28 and maand == 2 and schrikkeljaar == False:
    print('{:d}/{:d}/{:d}'.format(int(1), int(volgende_maand), int(jaar)))
elif dag == 28:
    print('{:d}/{:d}/{:d}'.format(int(volgende_dag), int(maand), int(jaar)))
elif dag == 29:
    print('{:d}/{:d}/{:d}'.format(int(volgende_dag), int(maand), int(jaar)))
elif dag == 30 and (maand == 4 or maand == 6 or maand == 9 or maand == 11):
    print('{:d}/{:d}/{:d}'.format(int(1), int(volgende_maand), int(jaar)))
elif dag == 30:
    print('{:d}/{:d}/{:d}'.format(int(volgende_dag), int(maand), int(jaar)))
elif dag == 31 and (maand == 1 or maand == 3 or maand ==  5 or maand == 7 or maand == 8 or maand == 10):
    print('{:d}/{:d}/{:d}'.format(int(1), int(volgende_maand), int(jaar)))
elif dag == 31 and maand == 12:
    print('{:d}/{:d}/{:d}'.format(int(1), int(1), int(volgend_jaar)))

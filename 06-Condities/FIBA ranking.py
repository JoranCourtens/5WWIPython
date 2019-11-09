#input
score_thuisploeg = int(input('Geef het aantal punten van de thuisploeg: '))
score_uitploeg = int(input('Geef het aantal punten van de uitploeg: '))
puntenverschil = abs(score_thuisploeg - score_uitploeg)

#berekening
if score_thuisploeg > score_uitploeg and puntenverschil < 10:
    print('{} {:.2f}' .format('thuisploeg:', int(530)))
    print('{} {:.2f}' .format('  uitploeg:', int(470)))
elif score_thuisploeg > score_uitploeg and puntenverschil < 20:
    print('{} {:.2f}' .format('thuisploeg:', int(630)))
    print('{} {:.2f}' .format('  uitploeg:', int(370)))
elif score_thuisploeg > score_uitploeg and puntenverschil >= 20:
    print('{} {:.2f}' .format('thuisploeg:', int(730)))
    print('{} {:.2f}' .format('  uitploeg:', int(270)))
elif score_thuisploeg < score_uitploeg and puntenverschil < 10:
    print('{} {:.2f}' .format('thuisploeg:', int(330)))
    print('{} {:.2f}' .format('  uitploeg:', int(670)))
elif score_thuisploeg < score_uitploeg and puntenverschil < 20:
    print('{} {:.2f}' .format('thuisploeg:', int(230)))
    print('{} {:.2f}' .format('  uitploeg:', int(770)))
elif score_thuisploeg < score_uitploeg and puntenverschil >= 20:
    print('{} {:.2f}' .format('thuisploeg:', int(130)))
    print('{} {:.2f}' .format('  uitploeg:', int(870)))

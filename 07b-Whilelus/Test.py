getal = 0

while getal < 5:
    print(getal)
    getal += 1



vorst_periode = 0

# 1e invoerwaarde VOOR while-lus
temperatuur = int(input('Dagtemperatuur: '))

while temperatuur <= 0:
    vorst_periode += 1
    # op einde van while-lus NIEUWE INVOER vragen
    temperatuur = int(input('Dagtemperatuur: '))

print(vorst_periode)



from random import randint

temp = randint(-10, 30)
vorst_periode = 0

while temp < 0:
    vorst_periode += 1
    temp = randint(-10, 30)

print(vorst_periode, 'dagen')



from random import randint

munt = 0
aantal_experimenten = 1000000

for i in range(aantal_experimenten):
    munt += randint(0, 1)

print('munt: ', munt, 'kop: ', aantal_experimenten - munt)

for letter in "Joran":
    print(letter)

naam = input('Geef naam: ')
for letter in naam:
    print(letter)

aantal_klinkers, aantal_medeklinkers = 0, 0

naam = input('Geef naam: ')
for letter in naam:
    if letter in 'aeiou':
        aantal_klinkers += 1
    else:
        aantal_medeklinkers += 1

print(aantal_klinkers, aantal_medeklinkers)


aantal_klinkers = 0
naam = input('Geef naam: ')
for letter in naam:
    if letter in 'aeiou':
        aantal_klinkers += 1

print(aantal_klinkers, len(naam) - aantal_klinkers)


naam = input('Geef naam: ')

i = 1
for letter in naam:
    print(i * letter)
    i += 1

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(6):
    print('m')

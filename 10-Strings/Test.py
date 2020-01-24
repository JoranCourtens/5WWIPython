woord = 'Python'

for i in range(0, 6):
    print(woord[i])
for i in range(0, len(woord)):
    print(woord[i])
for i in range(0, len(woord), 2):
    print(woord[i])
for i in range(-1, -len(woord) - 1, -1):
    print(woord[i])
for i in range(-len(woord), 0):
    print(woord[i])


woord = input('Woord: ')

for i in range(0, len(woord)):
    if woord[i] in 'aeiou':
        woord = woord[:i] + '*' + woord[i + 1:]
print(woord)

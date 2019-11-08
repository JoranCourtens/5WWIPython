#invoer
woord = input(str('Geef woord: '))
omgekeerd_woord = ''

#berekening
for letter in woord:
    omgekeerd_woord = letter + omgekeerd_woord

print(omgekeerd_woord)

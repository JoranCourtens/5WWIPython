#invoer
woord = input('Geef woord: ')
geldbedrag = int(input('Geef geldbedrag: '))
gewonnen_bedrag = 0
gegokte_letters = ''
letter = input('Geef letter: ')

#berekening
while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    gewonnen_bedrag += geldbedrag
    letter = input('Geef letter: ')
print(gewonnen_bedrag)

#invoer
hendel = input('Trek aan de hendel van wissel? ')
brug = input('Man van de brug duwen? ')

#berekening
if hendel == 'ja' and brug == 'ja':
    print(2)
elif hendel == 'nee' and brug == 'nee':
    print(5)
else:
    print(1)

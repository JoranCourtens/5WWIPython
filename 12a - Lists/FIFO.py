invoer = str(input('Geef de invoer: '))
lijst = []
n = 0
uitvoer = ''
aantal_vraagtekens = 0
while invoer != 'STOP':
    if invoer == '?' and aantal_vraagtekens < len(lijst):
        uitvoer += lijst[n] + '\n'
        lijst[n] = []
        n += 1
        aantal_vraagtekens += 1
    elif invoer == '?' and aantal_vraagtekens >= len(lijst):
        invoer = 'STOP'
    else:
        lijst.append(invoer)
    invoer = str(input('Geef de invoer: '))

print(uitvoer)








#invoer
N60 = int(input('Geef aantal tjirps: '))

#berekening
TF = 50 + ((N60 - 40) / 4)
TC = 10 + ((N60 - 40) / 7)

#uitvoer
print('temperatuur', '(Fahrenheit):', TF)
print('temperatuur', '(Celsius):', TC)

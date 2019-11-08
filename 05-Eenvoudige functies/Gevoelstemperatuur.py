#invoer

t = float(input('Geef T: '))
w = float(input('Geef W: '))

gevoelstemperatuur = 13.12 + (0.6215 * t) + ((0.3965 * t) - 11.37) * ((3.6 * w) ** 0.16)

print(str(gevoelstemperatuur))

#invoer

t = float(input('Geef T: '))
w = float(input('Geef W: '))
w_meter = w / 3.6

gevoelstemperatuur = 13.12 + (0.6215 * t) + ((0.3965 * t - 11.37) * pow(3.6 * w_meter, 0.16))

print((gevoelstemperatuur))

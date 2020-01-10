#invoer
il = float(input('Geef il: '))
fi = float(input('Geef fi: '))
L = int(input('Geef L: '))

#berekening
R = 2
fc = 0.2
N = R * il * fi * fc * L

#uitvoer
print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren:', int(N))

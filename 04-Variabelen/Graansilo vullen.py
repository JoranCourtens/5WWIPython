#invoer
b = float(input('Geef b: '))
l = float(input('Geef l: '))
c = float(input('Geef c: '))
r = float(input('Geef r: '))
h = float(input('Geef h: '))

pi = 3.1415926535

#berekening
V_graan = float((c * b * l) / 10000)
V_silo = float(r**2 * h * pi)

aantal_graansilos = (V_graan // V_silo) + 1
hoogte_oogst_laatste_silo = float((V_graan % V_silo) / (r**2 * pi))

#uitvoer
print(int(aantal_graansilos))
print(hoogte_oogst_laatste_silo)

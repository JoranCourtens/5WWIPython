#invoer
aantal_sec = int(input('Geef aantal sec: '))

#berekening
d = aantal_sec // (60 * 60 * 24)
u = (aantal_sec % (60 * 60 * 24)) // (60 * 60)
m = ((aantal_sec % ( 60 * 60 * 24 ) % ( 60 * 60 ))) // 60
s = ((((aantal_sec) % ( 60 * 60 * 24 )) % ( 60 * 60 )) % 60) % 60

#uitvoer
print(str(d) + 'd ' + str(u) + ':' + str(m) + ':' + str(s))

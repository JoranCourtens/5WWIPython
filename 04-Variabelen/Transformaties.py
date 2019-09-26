#invoer
a = int(input("Geef a: "))
b = int(input("Geef b: "))

#berekening
f = 'f(x) = 2(x - 3)^2 + 4'
g = 'g(x) = 2(x - ' + str(3 + a) + ')^2 + ' + str(4 + b)

#uitvoer
print(f)
print(g)

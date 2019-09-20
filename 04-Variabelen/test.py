# wisselen van waarden:
x, y = 2, 'hallo'
x, y = y, x
print(x, y)

# programma voor berekenen van discriminant
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

discriminant = b**2 - (4 * a * c)

print(discriminant)

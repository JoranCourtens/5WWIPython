#priemgetallen
from math import floor, sqrt

#geeft aan of een getal een priemgetal is
#True, getal is een priemgetal, anders False
def is_priem(getal):
    i = 2
    while i <= floor(sqrt(getal)) and getal % i != 0:
        i += 1
    if i == floor(sqrt(getal)) + 1:
        return True
    else:
        return False

aantal_gevraagd = int(input('aantal gevraagd: '))
som, aantal, getal = 0, 0, 2

while aantal < aantal_gevraagd:
    if is_priem(getal):
        som, aantal = som + getal, aantal + 1
        getal += 1
print(som)


def welkom(naam):
    print('Welkom terug ' + naam)

welkom('Dominiek')
welkom(str(1))
welkom(str(True))
welkom(welkom('Dominiek'))

test = welkom('Dominiek')
print(test)


def pythagoras(a, b):
    c = -1
    if a > 0and b > 0:
        c = sqrt(a*a + b*b)
    return c

print(pythagoras(3, 4))




from math import sqrt

def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def wortels(a, b, discriminant):
    w1, w2 = None, None
    if discriminant >= 0:
        w1 = (-b + sqrt(discriminant)) / (2 * a)
        w2 = (-b - sqrt(discriminant)) / (2 * a)
    return w1, w2

wortel1, wortel2 = wortels(2,4,8)
print(wortel1, wortel2)



from random import randint


def gooi_muntstuk():
    rg = randint(0, 2)
    if rg == 0:
        muntstuk = 'kop'
    else:
        muntstuk = 'munt'
    return muntstuk

for i in range(10):
    print(gooi_muntstuk())
#print(rg, muntstuk)


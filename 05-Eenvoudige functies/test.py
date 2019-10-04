#format
uitvoer = '{} + {} = {}'

print(uitvoer.format(3, 4, 7))
print(uitvoer.format(-1, 4, 3))

uitvoer = '{0} + {0} = {1}'
print(uitvoer.format(5, 10))

uitvoer = '{:d} + {:f} = {:d}'
print(uitvoer.format(1, 1, 2))
# :d = int
# :f = float

#modules
import math
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

from math import sqrt as vierkantswortel
print(vierkantswortel(2))

from math import ceil
print(ceil(3.444))

from math import floor
print(floor(3.444))

import random
print(random.random())

from random import uniform, random, randint, seed
seed(124)
print(random())
print(uniform(1, 5))
print(randint(3, 100))

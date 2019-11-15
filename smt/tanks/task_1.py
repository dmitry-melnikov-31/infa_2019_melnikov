
from random import randrange as rnd, choice

z = open('tanks_weights.csv', 'w')
s = ''
for i in range(50):
    for j in range(9):
        s += str(rnd(-100, 101))
        if j != 8:
            s += ','
    s += '\n'
z.write(s)
z.close()
import numpy as np
from random import randrange as r
m =int(input('m:'))
n=int(input('n:'))
a=[]
b=[]
for x in range(n):
    b.append(r(-2, 5))
b = np.array(b)


for x in range(m-1):
    for y in range(n):
        a.append(r(-2,5))
    p = np.array(a)

    a=[]
    b = np.vstack((b, p))

print(b)



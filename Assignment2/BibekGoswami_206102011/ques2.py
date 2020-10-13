# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:38:07 2020

@author: Bibek
"""
import decimal
import random
import numpy as np
from matplotlib import pyplot as plt

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)
    
    
a = list(float_range(-10,10,0.1))
b = list(float_range(-10,10,0.1))

X = []

for i in range(200):
    X.append(random.randint(-10,10))
    
sigma = np.std(X)

E = []

for i in range(len(a)):
    s = 0
    for j in range(len(b)):
        y = 2*X[i] + 3 + sigma*(random.gauss(0,1))
        y_p = a[i]*X[i] + b[j]
        e = y - y_p
        s += (e*e)
    s = s/len(b)
    E.append(s)
    
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(a, b, E);

plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:36:28 2020

@author: Bibek
"""

import random
from matplotlib import pyplot as plt
import numpy as np


X = []

for j in range(100): 
    X.append(random.randint(-10, 10)) 
  
Y = []

for i in range(len(X)):
    temp = 2*X[i] + 3
    Y.append(temp)

Y_n = []

sigma = np.std(X)

for i in range(len(X)):
    temp = 2*X[i] + 3 + sigma*(random.gauss(0,1))
    Y_n.append(temp)
    
plt.plot(X,Y,color='black')
plt.scatter(X,Y_n,color='red')
plt.show()
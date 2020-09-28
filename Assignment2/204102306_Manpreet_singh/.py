# -*- coding: utf-8 -*-
"""
@author: Maj Manpreet Singh
"""

import matplotlib.pyplot as plt
import numpy as np
import math as m
import random
a = 3
b = 2

x= np.linspace(-10,10,100)
y1 = np.empty([100,],dtype = float)
normal=np.empty([100,],dtype = float)

for n in range(100):
#   x = random.uniform(-10,10)
    y = a*x + b
    print("x = ",x,"y = ",y)
    plt.scatter(x,y,color="pink")

#x1= np.linspace(-10,10,100)
#mean = 0.0
    
mean = sum(x)/len(x)
var = 0.0

for i in range(100):
    normal[i]=random.normalvariate(0,1)
for i in x:
    var += (i-mean)**2/100
stddev=m.sqrt(var)


y1 = 3*x + 2 + stddev*normal

plt.plot(x,y,color="Black")
print("x = ",x,"y = ",y)
plt.scatter(x,y1,color='purple')
print()


    
    



 

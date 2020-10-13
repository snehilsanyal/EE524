# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:34:48 2020

@author: NISHAN TIWARI
"""

import matplotlib.pyplot as plt
import math as m
import numpy as np
import random as r
x=np.linspace(-10,10,100)
a=2
b=3
y=a*x+b
plt.plot(x,y,'k')
normal=np.empty([100,],dtype=float)
for i in range(0,100):
    normal[i]=r.normalvariate(0,1)
mean=sum(x)/len(x)
var=0
for i in x:
    var+=(i-mean)**2/100
stddev=m.sqrt(var)
y1=a*x+b+stddev*normal
plt.scatter(x[:],y1,c='r')

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:15:28 2020

@author: NISHAN TIWARI
"""

import math as ma
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import random as rn
import matplotlib.pyplot as plt
a=b=np.linspace(-10,10,200)
x=np.linspace(-10,10,100)
normal=np.empty([100,],dtype=float)
for i in range(0,100):
    normal[i]=rn.normalvariate(0,1)
mean=sum(x)/len(x)
var=0
for i in x:
    var+=(i-mean)**2/100
stddev=ma.sqrt(var)
y1=2*x+3+stddev*normal
y2=np.empty([100,])
error=np.empty([200,200,100])
k=l=0
for i in a:
    l=0
    for j in b:
        y2=i*x+j
        error[k][l]=y1-y2
        l+=1
    k+=1
E=np.empty([200,200])
k=l=0
for i in a:
    l=0
    for j in b:
        E[k][l]=sum(error[k][l])/100
        l+=1
    k+=1
X,Y=np.meshgrid(a,b)
Z=E
fig = plt.figure(figsize=(10,10))
mycmap = plt.get_cmap('gist_earth')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z,cmap=mycmap)
ax.set_xlabel('a')
ax.set_xlim(-12,12)
ax.set_ylabel('b')
ax.set_ylim(-12,12)
ax.set_zlabel('Error')
ax.set_zlim(-15,15)
plt.show()
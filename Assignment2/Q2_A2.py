# -*- coding: utf-8 -*-
"""
@author: Maj Manpreet Singh
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math as m
import random

x= np.linspace(-10,10,100)
y1= np.empty([100,],dtype = float)
y2= np.empty([100,],dtype = float)
e= np.empty([200,200,100],dtype=float)
#=np.linspace(200,200,100)
a=np.linspace(-10,10,200)
b=np.linspace(-10,10,200)
normal=np.empty([100,],dtype = float)
   
mean = sum(x)/len(x)
var = 0.0

for i in range(100):
    normal[i]=random.normalvariate(0,1)
for i in x:
    var += (i-mean)**2/100
stddev=m.sqrt(var)

y1= 3*x + 2 + stddev*normal
print("x = ",x,"y1= ",y1)
plt.scatter(x,y1,color='purple')

l = k = 0
for i in a:
    l = 0
    for j in b:
        y2 = i*x + j
        e[k][l] = y1 - y2
        l += 1
    k += 1
E = np.empty([200,200],dtype = float)
l=k=0
for i in a:
    l=0
    temp=0
    for j in b:
        temp = sum(e[k][l])
        E[k][l] = temp**2/100
        l += 1
    k += 1

X , Y = np.meshgrid(a,b)
Z = E
fig = plt.figure(figsize = (10,10))
mycmap = plt.get_cmap('gist_earth')
ax = fig.add_subplot(111, projection ='3d')
ax.plot_surface(X,Y,Z,cmap=mycmap)
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)
ax.set_zlim(0,20000)
plt.show


    


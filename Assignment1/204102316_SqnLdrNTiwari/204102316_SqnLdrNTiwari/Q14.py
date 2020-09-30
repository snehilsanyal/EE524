# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:27:44 2020

@author: NISHAN TIWARI
"""
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.empty([101,2],dtype=float)
xc=np.empty([101,1])
yc=np.empty((101,1))
for i in range (0,101):
    x[i][0]=-5+0.1*i
    xc[i][0]=x[i][0]
    x[i][1]=0.5*math.sqrt(25-x[i][0]**2)
    yc[i][0]=x[i][1]
print(x)
plt.plot(xc,yc)
for i in range (0,101):
    x[i][0]=-5+0.1*i
    xc[i][0]=x[i][0]
    x[i][1]=-0.5*math.sqrt(25-x[i][0]**2)
    yc[i][0]=x[i][1]
plt.plot(xc,yc)

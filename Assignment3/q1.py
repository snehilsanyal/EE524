# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:21:17 2020

@author: NISHAN TIWARI
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
x=np.linspace(-5.12,5.12,100)
y=np.linspace(-5.12,5.12,100)
z1=np.empty([100])
z2=np.empty([100])
n=int(input("Enter n vaue\n"))
if n==1:
    z1=10+x**2-10*np.cos(2*np.pi*x)
    plt.plot(x,z1,'k')
else:
    x,y=np.meshgrid(x,y)
    z2 = (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y)) + 10*n
    fig = plt.figure() 
    ax = fig.gca(projection='3d') 
    ax.plot_surface(x,y,z2, rstride=1, cstride=1,cmap=cm.nipy_spectral, linewidth=0.08)    
    plt.show()
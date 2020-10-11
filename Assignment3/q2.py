# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:45:50 2020

@author: NISHAN TIWARI
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
x=np.linspace(-32,32,200)
y=np.linspace(-32,32,200)
n=int(input("Enter n\n"))
if n==1:
    z=-20*np.exp(-0.2*x)-np.exp(np.cos(2*np.pi*x))+20+np.exp(1)
    plt.plot(x,z,'k')
else:
    x,y=np.meshgrid(x,y)
    z=-20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y)))+20+np.exp(1)
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
    
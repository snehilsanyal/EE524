# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:39:48 2020

@author: NISHAN TIWARI
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
x=np.linspace(-1.5,4,100)
y=np.linspace(-3,4,100)
x,y=np.meshgrid(x,y)
z=np.sin(x+y)+(x-y)**2-1.5*x+2.5*y+1
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(x,y,z,cmap=cm.nipy_spectral)
plt.show()
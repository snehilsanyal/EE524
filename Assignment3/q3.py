# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:07:06 2020

@author: NISHAN TIWARI
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
x,y=np.meshgrid(x,y)
z=x**2+y**2
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(x,y,z,rstride=1, cstride=1,cmap=cm.nipy_spectral)
plt.show()
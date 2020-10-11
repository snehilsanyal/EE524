# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:31:21 2020

@author: NISHAN TIWARI
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
x=np.linspace(-2,2,80)
y=np.linspace(-2,3,100)
x,y=np.meshgrid(x,y)
z=100*(x**2-y)**2+(1-x)**2
fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(x,y,z,rstride=1, cstride=1,cmap=cm.nipy_spectral)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:54:22 2020

@author: keyen
"""
import numpy as np
from matplotlib import pyplot as plt

#Constants
m=3
c=2
#x axes
x=np.arange(-10,10,.01)
#y axes
y=m*x+c;


# plot of the line y=mx+c

fig=plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 3x+2')
plt.show()
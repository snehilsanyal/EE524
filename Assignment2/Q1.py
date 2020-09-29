# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:20:33 2020

@author: keyen
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

a=2;b=3

x=np.arange(-10,10,0.2)
y=a*x+b
noise_y=a*x+b+norm.rvs(0,1,100)

fig=plt.figure()
plot=plt.plot(x,y,'k')
plt.scatter(x,noise_y, c='r')
plt.show()


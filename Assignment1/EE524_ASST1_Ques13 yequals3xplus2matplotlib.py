# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:05:07 2020

@author: NISHAN TIWARI
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, -10, 10)
y=3*x+2
plt.plot(x, y, label='linear')
plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:27:25 2020

@author: NISHAN TIWARI
"""
import csv
import random
import numpy as np
set1=np.empty([10,10],dtype=int)
for i in range (0,10):
    for j in range(0,10):
        set1[i][j]=random.randint(0,100)
print(set1)
np.savetxt('setofpoints.csv', set1, fmt="%d", delimiter=",")

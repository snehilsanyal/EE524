# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:21:34 2020

@author: NISHAN TIWARI
"""
import random as rn
import numpy as np
row=int(input("Enter no of rows of first matrix.\n"))
col=int(input("Enter no of columns of first matrix.\n"))
a=np.empty([row,col])
for i in range(0,row):
    for j in range(0,col):
        a[i][j]=rn.randint(-2, 5)
print(a)

    


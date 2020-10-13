# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:22:40 2020

@author: NISHAN TIWARI
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:21:34 2020

@author: NISHAN TIWARI
"""
import random as rn
import numpy as np
row1=int(input("Enter no of rows of first matrix.\n"))
col1=int(input("Enter no of columns of first matrix.\n"))
row2=int(input("Enter no of rows of second matrix.\n"))
col2=int(input("Enter no of columns of second matrix.\n"))
if row2==col1: 
    a=np.empty([row1,col1])
    b=np.empty([row2,col2])
    c=np.empty([row1,col2])
    d=np.empty([row1,col2])
    for i in range(0,row1):
        for j in range(0,col1):
            a[i][j]=rn.randint(-100, 100)
    for i in range(0,row2):
        for j in range(0,col2):
            b[i][j]=rn.randint(-100,30)
    for i in range(0,row1):
        for j in range(0,col2):
            c[i][j]=0
            for k in range(0,row2):
                c[i][j]+=a[i][k]*b[k][j]
    print(a)
    print(b)
    print(c)
    d=np.matmul(a, b)
    print(d)
    if np.array_equal(c, d):
        print("Your program is correct\n")
    else:
        print("ERROR in code\n")
else:
    print("ERROR, the number of columns of first matrix should be same as number of rows of second matrix")



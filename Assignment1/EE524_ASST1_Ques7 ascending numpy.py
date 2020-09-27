# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:53:29 2020

@author: NISHAN TIWARI
"""

import numpy as np
n=15
a=np.empty(n,dtype=int)
for i in range(0,n):
    a[i]=int(input("Enter number\n"))
print("The array you input is\n",a)
for j in range (0,n-1):
    for k in range (0,n-j-1):
        if a[k]>a[k+1]:
            s=a[k]
            a[k]=a[k+1]
            a[k+1]=s
print("The final sorted array in ascending order is\n",a)
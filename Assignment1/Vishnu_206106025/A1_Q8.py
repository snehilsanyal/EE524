# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:50:00 2020

@author: keyen
"""

# Function to generate a random matrix
def randmat(m,n,intervala=-5,intervalb=5):
    matrics=[]
    mtemp=[]
    for k in range(m):
        temp=[]
        for j in range(n):
            temp=[]    
            temp=random.randint(intervala,intervalb)
            matrics.append(temp)
    mtemp=np.array(matrics)
    mtemp=mtemp.reshape(m,n)
    return mtemp


# Example Program
import random
import numpy as np

#input matrix sizes
print("This program will print matrix A(m,n) with values in the range -2,5\n")
print("Enter the size of desired martix A(m,n)")

m=int(input("Enter m = "))
n=int(input("Enter n = "))  

#generating random matrix
martics=randmat(m,n,-2,5)
print(martics)
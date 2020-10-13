# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:54:45 2020

@author: keyen
"""
#Custom fucntion to multiply two matrices
def matrixmult(A,B):
    m=A.shape[0]
    n=A.shape[1]
    p=B.shape[1]
    f=np.zeros((m,p),dtype='int')
    if (A.shape[1]==B.shape[0]):
        for j in range(m):
            for k in range(p):
                f[j][k]=sum(A[j][r]*B[r][k] for r in range(n))       
    else:
        print('Shapes of the matrices do not match')
        
    return f

#Function to check if two matrices are equal
def isSame(A,B):
    m=A.shape[0]
    n=A.shape[1]
    p=B.shape[1]
    for i in range(m):
        for j in range(n):
            if (A[i][j] != B[i][j]):
                return 0
    return 1
#function to generate a random matrix as an array
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


#Example Program

import numpy as np
import time
import random

print("This program multiplies two random matrices of size A(m,n) and B(n,p) and compare the results with the built in function")
print()

print("")
choice=int(input("The size is determined randomly, press 1 to enter manually and press any number to continue  "))
try: 
    choice
    if choice==1:
        print("Enter desired size of the matrices, A(m,n) and B(n,p) when prompted")
        print()
        m=int(input("Enter m = "))
        n=int(input("Enter n = "))
        p=int(input("Enter p = "))
    else:
        m=random.randint(1,10)
        n=random.randint(1,10)
        p=random.randint(1,10)
finally:
    martisA=randmat(m,n)
    martisB=randmat(n,p)
    
#Comparison with inbuilt function    
customResult=matrixmult(martisA,martisB)
pythonResult=np.dot(martisA,martisB)

#print results    
print("\nMatrix A = \n\n", martisA)
print("\nMatrix B = \n\n", martisA)
print("\nDot product using custom function \n\n", customResult)
print("\nDot product using inbuilt function\n\n", pythonResult)

if (isSame(customResult,pythonResult)==1):
    print('\n\nThe two methods yield the same result\n\n')
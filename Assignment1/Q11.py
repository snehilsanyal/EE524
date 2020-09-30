# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:38:04 2020

@author: NISHAN TIWARI
"""

import csv
import numpy as np

f = open('setofpoints.csv')
csv_f = csv.reader(f)
matrix = np.empty([10,10],dtype=int)
i=0
for row in csv_f:
    for j in range(0,10):
        matrix[i][j] = int(row[j])
    i+=1
print(matrix)
f.close()
for i in range(0,10):
    globals()["v" + str(i+1)]=np.empty([10,1],dtype=int)
    for j in range(0,10):
        globals()["v" + str(i+1)][j][0]=matrix[j][i]
    print("v",i+1,"\b=\n",globals()["v"+str(i+1)])
mu = np.empty([10,1],dtype=float)
sum1=0
for i in range(0,10):
    for j in range(0,10):
        sum1+=globals()["v" + str(j+1)][i][0]
    mu[i][0]=sum1/10
print("mu=\n",mu)
for i in range(0,10):
    globals()["x" + str(i+1) + "minusmu"]=np.empty([10,1],dtype=float)
    for j in range(0,10):
        globals()["x" + str(i+1) + "minusmu"][j][0]=globals()["v" + str(i+1)][j][0]-mu[j][0]
    print("x",i+1,"\b-mu=\n",globals()["x" + str(i+1) + "minusmu"])
for i in range(0,10):
    globals()["x" + str(i+1) + "minusmutranspose"]=np.empty([1,10],dtype=float)
    for j in range(0,10):
        globals()["x" + str(i+1) + "minusmutranspose"][0][j]=globals()["x" + str(i+1) + "minusmu"][j][0]
    print("x",i+1,"\b-mutranspose=\n",globals()["x" + str(i+1) + "minusmutranspose"])
finalsum=np.zeros([10,10])
temp=np.empty([10,10])
for i in range(0,10):
    temp=np.matmul(globals()["x" + str(i+1) + "minusmu"],globals()["x" + str(i+1) + "minusmutranspose"])
    finalsum=np.add(temp, finalsum,)
print("the final sum is\n",finalsum)


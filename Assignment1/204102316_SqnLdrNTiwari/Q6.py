# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:51:40 2020

@author: NISHAN TIWARI
"""

list1=[]
n=15
for i in range (0,n):
    e=int(input("Enter the elements\n"))
    list1.append(e)
print ("The numbers before sorting are\n",list1)
for j in range (0,n-1):
    for k in range (0,n-j-1):
        if list1[k]<list1[k+1]:
            s=list1[k]
            list1[k]=list1[k+1]
            list1[k+1]=s
print("The list after sorting in descending order is\n",list1)

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:50:10 2020

@author: NISHAN TIWARI
"""

a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))
if a>b:
    c=a
    a=b
    b=c
if a!=b and b%a!=0:
    for i in range (b*2,a*b+1,b):
        #print(i)
        if i%a==0 and i%b==0:
            break 
        else:
            continue
else:
    i=b
print("LCM of ",a," and ",b," is ",i)

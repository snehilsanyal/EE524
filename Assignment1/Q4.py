# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:49:24 2020

@author: NISHAN TIWARI
"""

a=int(input("Enter first number\n"))
b=int(input("\nEnter second number\n"))
if a>b:
    c=a
    a=b
    b=c
l=0
d=0
if a==1:
    print(a+1," is prime")
    d=3
    l=1
elif a%2==0:
    if a==2:
        print(a," is prime")
        l=1
    d=a+1
else:
    d=a
for i in range (d,b+1,2):
    if i==3 or i==5 or i==7 or i==11 or i==13 or i==17 or i==19 or i==23 or i==29:
        print(i," is prime")
        l+=1
        continue
    elif i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0 or i%17==0 or i%19==0 or i%23==0 or i%29==0:
        continue
    k=0
    for j in range (31,i,2):
        if j%3==0 or j%5==0 or j%7==0 or j%11==0 or j%13==0 or j%17==0 or j%19==0 or j%23==0 or j%29==0:
            continue
        elif i%j==0:
            k+=1
    if k==0 and i!=1:
        print(i," is prime")
        l+=1
print("total number of prime numbers between ",a," and ",b,"are ",l)   
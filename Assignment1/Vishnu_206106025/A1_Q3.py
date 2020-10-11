# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:27:43 2020

@author: keyen
"""


def factorial(num):    
    fact=1
    for i in range(1,num):
        fact=fact*(num-i+1)        
    return fact

print("This program will calculate the factorial of a given number")

number=int(input('Enter a number \n'))
fact=factorial(number)
print()
print("%d! = %d " % (number,fact))


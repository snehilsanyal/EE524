# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:13:16 2020

@author: keyen
"""
#introduction
print("Algebraic Operations with two numbers")
print("Please enter two numbers when prompted")

#input from user
number1=int(input("Enter first number \n"))
number2=int(input("Enter second number \n"))

if number2==0:
    print("The second number is ZERO, as division with ZERO is not possible, \n the results of %d/%d and %d mod %d will not be displayed" % (number1, number2, number1, number2))
#Calculations

Sum=number1+number2
Diff=number1-number2
Multipl=number1*number2

if number2!=0:
    Division=number1/number2
    Mod=number1%number2


print()
print("%d+%d = %d " % (number1, number2, Sum))
print("%d-%d = %d " % (number1, number2, Diff))
print("%d*%d = %d " % (number1, number2, Multipl))

try: Division
except NameError:
    print()
    print("Second Number cannot be zero as division with zero is not possible")
else:
    print("%d/%d = %d " % (number1,number2, Division))

try: Mod
except NameError:
    print("mod with ZERO is not a feasible calculation")
else:
    print("%d mod %d = %d " % (number1, number2,Mod))


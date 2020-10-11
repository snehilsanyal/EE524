# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:35:56 2020

@author: keyen
"""

print('This program computes and prints the prime numbers in a given range [a,b]')




a=int(input("Enter the left endpoint 'a' "))
b=int(input("Enter the right endpoint 'b' "))

#Flag for prime number
tick=False
#ignoring 1 as it is not a prime
if a==1:
    a=a+1;
#parsing over the range
k=[]
for i in range(a,b):
    tick=True
    for j in range(2,i):
        if (i % j)==0:
            tick=False
            break
    
    if tick:
        k.append(i)

primes=str(k)[1:-1] # converting to string for printing
print("\nThe prime numbers between %d and %d are : \n\n" %(a,b) + primes)
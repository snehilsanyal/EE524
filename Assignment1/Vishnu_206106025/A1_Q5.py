# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:00:43 2020

@author: keyen
"""

import math
import sys


print("This program will calculate the LCM of two given numbers")





a=int(input('Enter the first number  '))
b=int(input('Enter the second number  '))

if a ==0 and b==0:
    print("Both numbers cannot be ZERO")
    sys.exit()

lcm=int(a*b/math.gcd(a, b))

print("LCM of %d and %d is %d" %(a,b,lcm))


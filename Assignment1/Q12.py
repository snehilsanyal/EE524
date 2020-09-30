# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:49:26 2020

@author: NISHAN TIWARI
"""
import math
import cmath
class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))            
    def display(self):
        if self.imgPart < 0.0:
            print(self.realPart,self.imgPart,"i", sep="")
        else:
            print(self.realPart,"+",self.imgPart,"i", sep="")
    def sum(self, c1, c2):
        self.realPart = float(c1.realPart + c2.realPart)
        self.imgPart = float(c1.imgPart + c2.imgPart)
    def subtract(self, c1, c2):
        self.realPart = float(c1.realPart - c2.realPart)
        self.imgPart = float(c1.imgPart - c2.imgPart )
    def multiply(self, c1, c2):
        self.realPart = float(c1.realPart * c2.realPart - c1.imgPart*c2.imgPart)
        self.imgPart = float(c1.imgPart * c2.realPart + c1.realPart * c2.imgPart)
    def mod(self,c1):
        return math.sqrt(c1.realPart**2 + c1.imgPart**2)
    def angle(self,c1):
        return math.atan(c1.imgPart/c1.realPart)
    def division(self,c1,c2):
        self.realPart = float((c1.realPart*c2.realPart+c1.imgPart*c2.imgPart)/math.sqrt(c2.realPart**2 + c2.imgPart**2))
        self.imgPart = float((-c1.realPart*c2.imgPart+c1.imgPart*c2.realPart)/math.sqrt(c2.realPart**2 + c2.imgPart**2))
    def conjugate(self,c1):
        self.realPart = c1.realPart
        self.imgPart = -1*c1.imgPart
c1 = Complex()
c2 = Complex()
c3 = Complex()
c4 = Complex()
c5 = Complex()
c6 = Complex()
c7 = Complex()
c8 = Complex()
c9 = Complex()
c10 = Complex()
c11 = Complex()
c12 = Complex()
print("Enter first complex number")
c1.initComplex()
print("\nEnter second complex number")
c2.initComplex()
print("\nFirst Complex Number: ", end="")
c1.display()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()
print("Difference of two complex numbers is ", end="")
c4.subtract(c1,c2)
c4.display()
print("Product of two complex numbers is ", end="")
c5.multiply(c1,c2)
c5.display()
print("Mod of first complex numbers is ", end="")
d = c6.mod(c1)
print(d)
print("Angle of First Complex Number is ", end= "")
f = c9.angle(c1)
print(f)
print("Mod of second complex numbers is ", end="")
e = c7.mod(c2)
print(e)
print("Angle of second Complex Number is ", end= "")
g = c10.angle(c2)
print(g)
print("Division of two complex numbers is ", end="")
c8.division(c1, c2)
c8.display()
print("Conjugate of first complex number is ", end="")
c11.conjugate(c1)
c11.display()
print("Conjugate of second complex number is ", end="")
c12.conjugate(c2)
c12.display()
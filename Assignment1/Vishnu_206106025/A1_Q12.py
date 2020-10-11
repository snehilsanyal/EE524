
# Class defining operations on complex number

class cmpl(object):
    
    def __init__(self, real=0.000, img=0.000):
        
        self.real = real
        self.img = img
        self.numb,self.dispnum = self.number(self.real,self.img) 
        #self.numb is the actual complex number defined by inbuilt complex complex number generator
        #self.dispnumb is an object to see print the complex number as a string
        
    def number(self,real, img):
        thenumber = []
        thenumber = real + img*1j 
        isit=abs(img)<1 or abs(real)<1
        if (img>=0):    
            thenumberstring = "%d+%dj" %(real,img)
            if isit:
                thenumberstring = "%f+%fj" %(np.round(real,3),np.round(img,3))
        else:
            thenumberstring = "%d%dj" %(real,img)
            
        return thenumber, thenumberstring


#this function extracts real and imaginary values into variables for easy use    
    def values(num):
        a = num.real
        b = num.img
        return a, b
#function for conjugate number       
    def conj(num):
        a,b = cmpl.values(num)
        conjreal = a
        conjimg = -b
        return cmpl(conjreal, conjimg)
#function for absolute value
    def absolute(num):
        a,b = cmpl.values(num)
        absoluteval = abs(np.sqrt(np.square(a) + np.square(b)))
        return absoluteval
#function for angle in the complex plain        
    def angle(num):
        a,b = cmpl.values(num)
        angletheta = a/b
        theta = np.tanh(angletheta)
        return theta
#addition        
    def add(num1,num2):
        a,b = cmpl.values(num1)
        c,d = cmpl.values(num2)
        realval = a+c 
        imgval = b+d
        addition = cmpl(realval,imgval)
        return addition
#subtraction    
    def subtract(num1,num2):
        a,b = cmpl.values(num1)
        c,d = cmpl.values(num2)
        realval = a - c
        imgval = b - d
        subtraction = cmpl(realval,imgval)
        return subtraction
#multiplication    
    def multiply(num1,num2):
        a,b = cmpl.values(num1)
        c,d = cmpl.values(num2)
        realval = a*c - b*d
        imgval = b*c + a*d 
        multip = cmpl(realval,imgval)
        return multip
    
#Division        
    def divide(num1,num2):
        realval=[]
        a,b = cmpl.values(num1)
        c,d = cmpl.values(num2)
        numerator = cmpl.multiply(num1,cmpl.conj(num2))
        denomenator = cmpl.multiply(num2,cmpl.conj(num2))
        numerA,numerB = cmpl.values(numerator)
        denomval = np.square(c) + np.square(d)        
        realval = numerA/denomval
        imgval = numerB/denomval
        div = cmpl(realval,imgval)
        return div
    
    


# Example program

import scipy as sp
import numpy as np

#number1
a=2
b=3

#number2
c=-4
d=6

#initialising the complex numbers
number1=cmpl(1,2)
number2=cmpl(4,5)

#operations
addnum=cmpl.add(number1,number2)
minusnum=cmpl.subtract(number1,number2)
multplenum=cmpl.multiply(number1,number2)
dividnum=cmpl.divide(number1, number2)

#Conjugate, Absolute and Complex Angle
conjugatenum1=cmpl.conj(number1)
conjugatenum2=cmpl.conj(number2)
anglenum1=cmpl.angle(number1)
anglenum2=cmpl.angle(number2)
absolutenum1=cmpl.absolute(number1)
absolutenum2=cmpl.absolute(number2)


#Print results

print("\n\nComplex Number A = "+ number1.dispnum)
print("Complex Number B = "+ number2.dispnum)

print("\nAddition")
print("(%s) + (%s) = %s\n " %(number1.dispnum,number2.dispnum,addnum.dispnum))
print("\nSubtraction")
print("%s - %s = %s \n" %(number1.dispnum,number2.dispnum,minusnum.dispnum))
print("\nMultiplicaton")
print("%s * %s = %s " %(number1.dispnum,number2.dispnum,multplenum.dispnum))
print("\nDivision")
print("      %s" %number1.dispnum)
print("  ------------   =  %s " %dividnum.dispnum)
print("      %s\n" %number2.dispnum)



print("Conjugate of (" +number1.dispnum +") is ("+ conjugatenum1.dispnum+")\n")
print("Conjugate of (" +number2.dispnum +") is ("+ conjugatenum2.dispnum+")\n")
print("\nComplex angle of the number ("+number1.dispnum+") is " +str(np.round(anglenum1,4)))
print("\nComplex angle of the number ("+number2.dispnum+") is " +str(np.round(anglenum2,4)))
print("\n\nAbsolute value of the complex number |(" + number1.dispnum+")| = "+ str(np.round(absolutenum1,3)))
print("\nAbsolute value of the complex number |(" + number2.dispnum+")| = "+ str(np.round(absolutenum2,3)))


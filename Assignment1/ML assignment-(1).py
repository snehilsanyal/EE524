#!/usr/bin/env python
# coding: utf-8

# # 1.Print hello world

# In[1]:


print('Hello World!')


# # 2.Algebraic expressions

# In[2]:


a=int(input('enter the value of a ='))
b=int(input('enter the value of b ='))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print('c=a+b=',c)
print('d=a-b=',d)
print('e=a*b=',e)
print('f=a/b=',f)
print('g=a%b=',g)


# # 3.Factorial of a number

# In[3]:


num=1
x=int(input('enter the value of x='))
while x<x+1:       
    num=num*x
    x-=1
    if x==0:
         break
print('factorial of a number is =',num)


# # 4.Prime numbers

# In[24]:


list=[]
def prime(a,b):
    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                    list.append(i)
    return list
prime(3,30)


# # 5.Lcm of two numbers

# In[5]:


def compute_Lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            Lcm = greater
            break
        greater += 1
    print('The Lcm of x and y is=',Lcm)
compute_Lcm(12,6)


# # 6.Bubblesort algorithm(descending order)

# In[6]:


def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
bubble([3,1,5,2,6,8,9,12,11,33,23,54,66,16,35])
    


# # 7.Ascending order

# In[7]:


import numpy as np 
bubble=np.array([3,1,5,2,6,8,9,12,11,33,23,54,66,16,35])
bubble[::1].sort()
print(bubble)


# # 8.Print matrix in range (-2,5)

# In[8]:


import numpy as np
m= int(input('enter rows='))
n= int(input('enter columns='))
a=np.random.randint(-2,5,size=(m,n))
print(a)


# # 9.Multiply two matrices

# In[12]:


import numpy as np
m=int(input("enter rows of first matrix="))
n=int(input("enter columns of first matrix="))
p=int(input("enter columns of second matrix="))
matrix1 = np.zeros ((m,n),dtype=int)
matrix2 = np.zeros((n,p),dtype=int)
reuslt = np.zeros((m,p),dtype=int)

for i in range(m):
    for j in range(n):
        matrix1[i][j]=int(input('enter elements='))
print(matrix1)
for i in range(n):
    for j in range(p):
        matrix2[i][j]=int(input('enter elements='))
print(matrix2)   

for i in range (m):
    for j in range (len(matrix2)):
         for k in range(p):
            result[i][j] += result[i][j] + matrix1[i][k] * matrix2[k][j]
print('matrix multplication = ',result)    
        


# # 10.Write file operations

# In[15]:


import csv
from numpy import random 
import numpy as np
n = random.randint(1000,size=(100))
print(n)
file="File.csv"
with open(file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Num'])
    csvwriter.writerow(n)


# # 11. Read file operations

# In[16]:


import csv
import numpy
reader=[]
csv.reader(open("Random.csv","rb"),delimiter=",")
x = list(reader)
result = numpy.array(x).astype("float")


# # 12.Complex number

# In[17]:


import cmath
from math import sqrt

class Complex(object):

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))

    def __div__(self, other):
        r = (other.real**2 + other.imag**2)
        return Complex((self.real*other.real - self.imag*other.imag)/r,
            (self.imag*other.real + self.real*other.imag)/r)

    def __abs__(self):
        return ((self.real**2) + (self.imag**2))**0.5
    
    def __conjugate__(self):
        return complex(self.real,-self.imag)
    def __phase__(self):
        return cmath.phase(self)
    
    
c1=complex(5,6)
c2=complex(7,8)
print('c1 =',c1)
print('c2 =',c2)
addition=c1+c2
print('addition =',addition)
subraction=c1-c2
print('subraction =',subraction)
multiplication=c1*c2
print('multiplication =',multiplication)
division=c1/c2
print('division =',division)
absolute_value =(c1.real**2+c1.imag**2)**0.5
print('absolute value c1 =',absolute_value)
absolute_value =(c2.real**2+c2.imag**2)**0.5
print('absolute value c2 =',absolute_value)
phase =cmath.phase(c1)
print('phase c1 =',phase )
phase =cmath.phase(c2)
print('phase c2 =',phase )
conjugate=complex(c1.real,-c1.imag)
print('conj c1 =',conjugate)
conjugate=complex(c2.real,-c2.imag)
print('conj c2 =',conjugate)




# # 13.Plot the function

# In[18]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10)
y = 3*x+2
plt.xlim(-10,10)
plt.plot(x, y,label='y=3x+2',c='r')
plt.title('Graph of y=2x+1')
plt.xlabel('X-AXIS', c='b')
plt.ylabel('Y-AXIS', c='b')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





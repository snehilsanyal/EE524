print("Assignment No.1 \nSubmitted by: Maj Manpreet Singh")
print()
print()
print()

#1. Print ’Hello World!’

print("Q.1 Hello World!")
print()

#2. User input two numbers a and b. Perform the following algebraic operations c = a + b, d = a − b, e = a ∗ b,
#   f =a /b and g = a%b and print their results.

print("Q.2. Perform the algebraic operations")
print()
Num1 = float(input(" Enter value of a: "))
Num2 = float(input(" Enter value of b: "))
op = input(" Enter operator +, -, *, /, % : ")

if op == "+":
    print("c = ", Num1 + Num2)

elif op == "-":
    print("d = ", Num1 - Num2)

elif op == "*":
    print("e = ", Num1 * Num2)

elif op == "/":
    print("f = ", Num1 / Num2)

elif op == "%":
    print("g = ", Num1 % Num2)

print()


#3. Find the factorial of a number ’num’ and print the result.
print("Q.3. Find the factorial of a number.")
print()
def factorial(a):
    fact = 1
    for p in range(a,0,-1):
        fact=fact*p
    return fact
n=int(input(" Enter a number: "))
result=factorial(n)
print(" Factorial of",n,"is",result)

print()



#4. Take two user inputs a and b. Write a program to print all the prime numbers in the interval [a,b].

print("Q.4. Print all the prime numbers in the interval [a,b]")
print()
a=int(input(" Enter starting number a: "))
b=int(input(" Enter end number b : "))
prime=[]
for num in range(a,b+1):
    fact=0
    for x in range(2,num-1):
        if num % x == 0:
            fact =1
            break

    if fact ==0 :
        prime.append(num)

print(" List of prime numbers is",prime)

print()


#5. Take two user inputs a and b and find their Lowest Common Multiple(LCM).


print("Q.5.Find the Lowest Common Multiple of two numbers")
print()
a=int(input(" Enter first number a: "))
b=int(input(" Enter second number b: "))

for m in range (1,a*b +1):
    if m%a == 0 and m%b ==0:
        print("LCM of number is ", m)
        break

print()

#6. Create a list of length n = 15. Sort the array in descending order and print the sorted List as well as the sorted indices. Use the bubble sort algorithm.
print("Q.6. Sort the array in descending order and print the sorted List as well as the sorted indices. Use the bubble sort algorithm.")
print()
list = []
num = int(input("How many numbers you want to enter in the list: "))
print("Enter Value: ")
for k in range(num) :
    list.append(float(input()))

print("Unsorted List: ",list)

for j in range(len(list) - 1):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp
            print(list)
        else:
            print(list)
print()


# Q.7 Repeat the previous program for sorting in ascending order. Use numpy array instead of list.

print("Q.7 Sorting in ascending order using numpy")
print()
print("Unsorted List: ",list)


import numpy as np
x = np.array(list)
print("Sorted List in ascending order", np.sort(list))
print()


#Q.8. Print a matrix M Rmxn having random values in the given range [-2, 5].m and n are to be given as userinput.

print(" Q.8 Print a matrix M with Rmxn.")
m = int(input("Enter the number of row: "))
n = int(input("Enter the number of column: "))

matrix = []

for i in range(m):
    a = []
    
    for j in range(n):
        k = int(input())
        a.append(k)
    matrix.append(a)
    
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end="")
        
    print()
    
    
#second algo
    
m = int(input("Enter Number of Row: "))
n = int(input("Enter Number of Column: "))
Matrix = []
for i in range (m):
  Matrix.append([])
for i in range (m):
    for j in range(n):
        Matrix[i].append(j)
        Matrix[i][j] = 0
for i in range (m):
    for j in range (n):
        print('entry in row: ',i+1,'column: ',j+1)
        Matrix[i][j] = int(input())
        print(Matrix)
    print()

    
    
#Q.9.Write a program to multiply two random matrices M1Rmxn, M2Rnxp(Don’tuse built-in functions). Compare the result obtained with the built-in function.
    
print("Q.9 Print multiplication of two random matrices.")    
m = int(input("Enter Number of Row: "))
n = int(input("Enter Number of Column: "))
p = int(input("Enter the Column number for matrix1/ Row number of matrix2: "))

print("Enter the element for matrix1: ")
matrix1 = [[int(input()) for i in range(n)] for j in range(m)]
print("matrix1: ")
for i in range(m):
    for j in range(n):
        print(format(matrix1[i][j], "<3"), end="")
    print()


print("Enter the element for matrix2: ")
matrix2 = [[int(input()) for i in range(n)] for j in range(m)]
print("matrix2: ")

for i in range(m):
    for j in range(n):
        print(format(matrix2[i][j], "<3"), end="")
    print()

result = [[0 for i in range(m)] for j in range(n)]

for i in range(m):
    for j in range(n):
        for k in range(p):
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

print("result is: ")
for i in range(m):
    for j in range(n):
        print(format(result[i][j], "<7"),end= "")
    print()

print()



#10. Write File operations :
#    • Generate a set of n= 100 random points X = xi, i = 1, . . . n, xiR10.

print("Q.10 Generate a set of n= 100 random points X = xi, i = 1, . . . n, xiR10. ")
print()
import random

X = range(0,100)
value = random.choices(X, k=10)
print(value)
print()




import csv
import random
import numpy as np
set1=np.empty([10,10],dtype=int)
for i in range (0,10):
    for j in range(0,10):
        set1[i][j]=random.randint(0,100)
print(set1)
np.savetxt('setofpoints.csv', set1, fmt="%d", delimiter=",")


#11. Read File operations:
#    • Read the CSV file generated in the previous program to a matrix.Each column of matrix should represent a vector.
#    • Compute the following : C =1nPni=1(Xi − µ)(Xi − µ)T where µ =1nPni=1 Xi where i = 1,2,3 ... n. Xi = [xi1,xi2, ... xi10] is a column vector.



#12. Define a class for a complex number a + jb. Define memeber functionsto do basic operations conjugate, absolute value, addition, subtraction, multiplication, division and angle. 
# Define two complex numbers c1, c2 and print the results of the following operations c1 + c2, c1c2, c1c2,c1 c2,|c1|, |c2|,6 c1, 6 c2.

print("Q.12 Define two complex numbers and operate different operations on them.")
print()
import cmath

a1 = float(input("Enter real number of first complex number c1: "))
b1 = float(input("Enter imaginary number of first complex number c1: "))
a2 = float(input("Enter real number of second complex number c2: "))
b2 = float(input("Enter imaginary number of second complex number c2: "))
c1 = complex(a1,b1);
c2 = complex(a2,b2);
print(" c1= ",c1,"\n","c2= ",c2)
print()
x = c1 + c2
print("Sum of two complex number: ",x)
print()
y = c1 * c2
print("Product of two complex number: ",y)
print()
z = c1 / c2
print("Division of two complex number: ",z)
print()
print("Phase of first complex number c1: ",cmath.phase(c1))
print()
print("Phase of first complex number c2: ",cmath.phase(c2))
print()
print("Absolute of first complex number c1: ",abs(c1))
print()
print("Absolute of first complex number c1: ",abs(c2))

r = cmath.polar(c1)
s = cmath.polar(c2)

print("The argument and modulus of first complex number c1: ",r)
print()
print("The argument and modulus of second complex number c2: ",s)
print()


#Q.13. Plot the function y = 3x + 2 with x  [−10, 10]. Use Matplotlib for the same.
print("Q.13. Plot the function y = 3x + 2 with x  [−10, 10]. Use Matplotlib for the same.")

print()
import numpy as np
import matplotlib.pyplot as plt
x= np.arange(-10,10)
y = 3*x + 2

plt.plot(x,y)
print("y = ",y)
plt.show()
print()



#Q.14. Scatter plot all the points.
#    • Generate a set of n = 100 points, X = xi, i = 1,2, .... n, xiR2 withinan ellipse centered at µx = 5 and µy = -5 with major axis as 10 andminor axis as 5.
#    • Plot all the points using Matplotlib

print("Q.14 #Q.14. Scatter plot all the points.\nGenerate a set of n = 100 points, X = xi, i = 1,2, .... n, xiR2 withinan ellipse centered at µx = 5 and µy = -5 with major axis as 10 andminor axis as 5.\nPlot all the points using Matplotlib")
print()
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.empty([101,2],dtype=float)
xc=np.empty([101,1])
yc=np.empty((101,1))
for i in range (0,101):
    x[i][0]=-5+0.1*i
    xc[i][0]=x[i][0]
    x[i][1]=0.5*math.sqrt(25-x[i][0]**2)
    yc[i][0]=x[i][1]
print(x)
plt.plot(xc,yc)
for i in range (0,101):
    x[i][0]=-5+0.1*i
    xc[i][0]=x[i][0]
    x[i][1]=-0.5*math.sqrt(25-x[i][0]**2)
    yc[i][0]=x[i][1]
plt.plot(xc,yc)
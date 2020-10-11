import numpy as np
import random

print('Enter values for m, n, p for the matrix multiplication of shapes: (mxn)*(nxp)')
m=int(input('Enter number of m :'))
n=int(input('Enter number of n :'))
p=int(input('Enter number of p :'))

A=np.random.randint(0,20,(m,n))
B=np.random.randint(0,20,(n,p))
print('Matrix A:')
print(A)
print()
print('Matrix B:')
print(B)
print()
c=np.ndarray(shape=(m,p), dtype='int')

for i in range(m):
    for j in range(p):
        c[i][j]=0
        for k in range(n):
            c[i][j]+=A[i][k]*B[k][j]
print('Result of manual multiplication:')
print(c)
print()
print('Result of using built-in function (np.matmul(A,B)):')
print(np.matmul(A,B))
print()
print('Result of using built-in function (A.dot(B)):')
print(A.dot(B))

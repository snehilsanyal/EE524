## Program to multiply two matrices

import numpy as np

print("Enter the values of m, n & p for the matrices M1(mxn) and M2(nxp) and click enter after entering each element:")
m = int(input())
n = int(input())
p = int(input())

M1 = np.random.randint(1,5,(m,n))
M2 = np.random.randint(1,5,(n,p))
M = np.zeros((m,p),dtype='int16')
print(M1)
print(M2)
print(M)

for i in range(m):
    for j in range(p):
        for k in range(n):
            M[i,j] = M[i,j] + (M1[i,k]*M2[k,j])
            
print("The elements of resultant matrix, M, using manual calculations is:")
print(M)


print("The elements of resultant matrix, M, using inbuilt function is:")
print(np.matmul(M1,M2))


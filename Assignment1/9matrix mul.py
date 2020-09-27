import numpy as np
m=int(input('enter the row of matrix A'))
n=int(input('enter the column of matrix A'))
p=int(input('enter the column of matrix B'))
A=np.random.randint(10,size=(m,n))
B=np.random.randint(10,size=(n,p))
C=np.random.randint(1,size=(m,p))             #declared matrix C as it will get overrided finally.
print('MATRIX A :')
print(A)
print('MATRIX B :')
print(B)
for i in range(m):
    for k in range(p):
        for j in range(n):
            C[i][k]=C[i][k]+A[i][j]*B[j][k]
print('MATRIX C = A*B :')
print(C)
X=np.random.randint(1,size=(m,p))
X=np.dot(A,B)                                #it computes multiplication using built in function.
E=np.random.randint(1,size=(m,p))
E=np.subtract(C,X)                           #it will check the diff. in built in func.output and manual written code output.
print('difference between manually coded multiplication and built in function output:')
print(E)                                      #if it comes out to be zero matrix then the code written above is correct.       

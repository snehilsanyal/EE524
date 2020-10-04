import numpy as np
import random
#entries of number of row and coloumn of first matrix
print("enter number of row of first matrix")
m=int(input())
print("enter number of column of first matrix")
n=int(input())

#random matrix generation of m*n dimension

matrix_element1=[]
i=0
while(i<m*n):
    matrix_element1.append(random.randrange(-2,5))
    i=i+1
matrix1= np.array(matrix_element1).reshape(m, n)
print("matrix1 = ",matrix1)

 #entries of number of row and colomn of second matrix

print("enter number of row of second matrix")
p=int(input())
print("enter number of column of second matrix")
r=int(input())

#random mattrix generation of p*r dimension
matrix_element2=[]
i=0
while(i<p*r):
    matrix_element2.append(random.randrange(-2,5))
    i=i+1
matrix2 = np.array(matrix_element2).reshape(p, r)
print("matrix= ",matrix2)

# matrix multiplication
result_matrix_element=[]
if n==p:                #checking whether colomn of second matrix is equal first matrix or not

    for i in range(m):
        for j in range(r):
            sum = 0
            for k in range(n):
                sum = sum + matrix1[i][k] * matrix2[k][j]
            result_matrix_element.append(sum)

    result_matrix = np.array(result_matrix_element).reshape(m, r)
    print("result = ",result_matrix)

else:
    print("matrix multiplication does not exit")


#matrix multiplication using built-in function
result=np.dot(matrix1,matrix2)
print("result using built in function= ",result)
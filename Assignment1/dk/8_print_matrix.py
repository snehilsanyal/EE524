import numpy as np
import random
print("enter number of row")
m=int(input())
print("enter number of column")
n=int(input())
matrix_element=[]
i=0
while(i<m*n):
    matrix_element.append(random.randrange(-2,5))
    i=i+1
matrix = np.array(matrix_element).reshape(m, n)
print(matrix)
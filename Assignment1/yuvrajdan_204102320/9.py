#Q9
import numpy as np
#  1st 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
#  2nd 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):

   for j in range(len(Y[i])):
    
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print("array multiplication using loop:")
for r in result:
   print(r)
#USING NUMPY
arr1=np.array([[12,7,3],
    [4 ,5,6],
    [7 ,8,9]])
arr2=np.array([[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]])
arr = np.dot(arr1,arr2) 
print(" \n \narray multiplication using inbulit function:")
arr
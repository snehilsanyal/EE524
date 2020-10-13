## Program to read from CSV file and compute Mean vector and Variance matrix

import numpy as np
import pandas as pd

#M = np.genfromtxt('D:/IITG/ML Lab/Assignments/Assignment-1/Responses/Write_CSV.csv', delimiter=',')

# Reading matrix from CSV file
M = pd.read_csv('D:/IITG/ML Lab/Assignments/Assignment-1/Responses/Write_CSV.csv',header=None)
M = M.to_numpy()
print(M)
print(M.shape)

m = M.shape[0]
n = M.shape[1]

# Mean Matrix
U = np.zeros((m,1))

# Variance Matrix
C = np.zeros((m,m))

 
for i in range(n):
    X = M[:,i].reshape(m,1)
    U = U + X
U = U/n
print("Mean Matrix, U =",U)
print(U.shape)
     

for i in range(n):
    X = M[:,i].reshape(m,1)
    X = X - U
    X_t = X.transpose()
    X2 = np.matmul(X, X_t)
    C = C + X2
C = C/n

print("Variance Matrix, C =",C)
print(C.shape)
    



## Program to write data points to a CSV file

import numpy as np

m = 10
n = 100

a = np.random.random((m,n))
print(a)
print(a.shape)

np.savetxt('D:/IITG/ML Lab/Assignments/Assignment-1/Responses/Write_CSV.csv',a,delimiter=',')


# csv_file = open('D:/IITG/ML Lab/Assignments/Assignment-1/Responses/Write_CSV.csv', 'w')


# for i in range(a.shape[0]):
#     for j in range(a.shape[1]):
#         csv_file.write(str(a[i,j]))
#         csv_file.write(',')
#     csv_file.write('\n')
# csv_file.close()
    


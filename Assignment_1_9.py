import numpy as np

#Function to create a matrix
def matrix(m,n):
    arr = np.array([])
    print('\n__Enter the elements of matrix__\n')
    for i in range(m*n):
        ele = int(input())
        arr = np.append(arr,ele)
    mat = np.reshape(arr,(m,n))
    print('\nThe entered matrix is:\n')
    print(mat)

    return mat

#Function to multiply two matrices
def mat_mul(arr1,arr2,m,n,p):
    result = np.array([])
    for i in range(m):
        for j in range(p):
            sum = 0
            for k in range(n):
                sum = sum + arr1[i,k]*arr2[k,j]
            result = np.append(result,sum)
    result1 = np.reshape(result,(m,p))
    return result1

def main():
    print("\n__Program to multiply two matrices__\n")
    row1 = int(input('\n\nEnter the number of rows in first matrix: '))
    col1 = int(input('\nEnter the number of columns in first matrix: '))
    mat1 = matrix(row1,col1)
    row2 = int(input('\nEnter the number of rows in the second matrix: '))
    col2 = int(input('\nEnter the numbers of columns in the second matrix'))
    mat2 = matrix(row2,col2)

    if col1 == row2:
        print('\nThe matrices are consistent for matrix multiplication\n')
        print('\nTheir product is:\n')
        prod = mat_mul(mat1,mat2,row1,col1,col2)
        print(prod)
    else:
        print('\nThe matrices are not consistent for matrix multiplication as column of 1st dose not matches rows of 2nd matrix')

if __name__ == '__main__':
    main()

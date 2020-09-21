import numpy as np
import random as rd

#Random Number array
def ran_arr(m,n):
    arr = np.array([])
    for i in range(m*n):
        randnum = rd.randrange(-2,6)
        arr = np.append(arr,randnum)

    return arr

def main():
    print("\n__Matrix with random number between [2,5] as elements__")
    rows = int(input('\nEnter the number of rows: '))
    cols = int(input('\nEnter the number of columns:'))
    arr = ran_arr(rows,cols)
    mat = np.reshape(arr,(rows,cols))
    print('\n The Matrix is\n')
    print(mat)

if __name__ == '__main__':
    main()

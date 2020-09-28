import numpy as np
import random as rd
import csv

#Generation of vectors with random values
def gen_rand_vect():
    arr = np.array([])
    for i in range(100*10):
        n = rd.randint(-5,10)
        arr = np.append(arr,n)

    vect_arr = np.reshape(arr,(10,100))
    return vect_arr
#writing data to a CSV File
def write_csv(arr):
    file = open('Assign_1_10.csv','w+',newline = '')

    header = []
    with file:
        for i in range(100):
            header.append('Vector'+str(i+1))
        writer = csv.DictWriter(file,fieldnames = header)
        writer.writeheader()
        write = csv.writer(file)
        write.writerows(arr)



def main():
    z = gen_rand_vect()
    print("\nThe array of vectors is:\n")
    print('\n',z)
    write_csv(z)

if __name__ == '__main__':
    main()

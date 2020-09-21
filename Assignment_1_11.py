import numpy as np
import pandas as pd

#function to read a CSV file and manipulate its columns
def read_file():
    #Reading the data into a datframe
    data  = pd.read_csv('Assign_1_10.csv')
    data1 = data
    data['Mean'] = data.mean(axis = 1) #Calculating mean of each row
    #Converting Data to mean-zero data
    for i in range(100):
        name = 'Vector'+str(i+1)
        data1[name] = data1[name] - data['Mean']
    sum = 0
    #Calculating Inner product of each Vector and adding them up
    for i in range(100):
        name = 'Vector'+str(i+1)
        arr = np.array([])
        arr = data1[name]
        sum = sum + np.dot(arr.transpose(),arr)
        j = i+1

    result = sum/j

    return result

def main():
    result = read_file()
    print("\nThe required sum is: ",result)

if __name__ == '__main__':
    main()

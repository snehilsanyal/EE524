import random
import numpy as np

def BubbleSort(unsortedArr):
    n = len(unsortedArr)
    unsortedArr = np.array([(i, unsortedArr[i]) for i in range(n)])
    #print(np.shape(unsortedArr))
    for i in range(n-1): # iterating from 0 to n-2 index
        for j in range(0, n-i-1):   #iterating from 0 to n-i-2
            if unsortedArr[j][1] >  unsortedArr[j + 1][1]: # condition check to sort in ascending manner
                unsortedArr[j][0],unsortedArr[j+1][0] = unsortedArr[j+1][0], unsortedArr[j][0]
                unsortedArr[j][1],unsortedArr[j+1][1] = unsortedArr[j+1][1], unsortedArr[j][1]
    return unsortedArr


unsortedArr = np.random.randint(1, 100, 15)  # generating a random np array of 15 numbers
print('The unsorted array:')
print(unsortedArr)
print()
print('The sorted array in the form (index,value):')
print(BubbleSort(unsortedArr))

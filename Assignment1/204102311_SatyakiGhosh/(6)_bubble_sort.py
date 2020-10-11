import random

def BubbleSort(unsortedArr):
    n = len(unsortedArr)
    unsortedArr = [(i, unsortedArr[i]) for i in range(n)]
    for i in range(n-1): # iterating from 0 to n-2 index
        for j in range(0, n-i-1):   #iterating from 0 to n-i-2
            if unsortedArr[j][1] < unsortedArr[j + 1][1]: # condition check to sort in descending manner
                unsortedArr[j],unsortedArr[j+1] = unsortedArr[j+1], unsortedArr[j]
    return unsortedArr


unsortedArr = random.sample(range(1, 100), 15)  # generating a random list of 15 numbers
print('The unsorted array:')
print(unsortedArr)
print()
print('The sorted array in the form (index,value):')
print(BubbleSort(unsortedArr))

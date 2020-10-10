import copy
import numpy as np

#The bubblesort algorith for sorting

def bubbleSort(arr):
    temp=copy.copy(arr)
    n = len(temp)
    ind = []
    for i in range(n):
        for j in range(0, n-i-1):
            if temp[j]>temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
    
    for i in range(n):
        temparray=copy.copy(arr)
        temparray=temparray.tolist()
        ind.append(temparray.index(temp[i])) 
        
    temp=np.array(temp)
    ind=np.array(ind)
    return temp, ind



# Python program for implementation of Bubble Sort 
#sorting a random matrix in ascening order
#Ascending Order

randomarray=np.random.randint(1,100,15)
sortedarray,index=bubbleSort(randomarray)




print("The sorted array is 'S' \n")
print(sortedarray)
print("\nThe original random array 'R'\n")
print(randomarray)
print("\nThe S-->R mapping")
print(index)


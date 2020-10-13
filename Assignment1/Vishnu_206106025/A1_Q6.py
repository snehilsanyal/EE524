# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:22:20 2020

@author: keyen
"""

# Python program for implementation of Bubble Sort 

import random
import copy

#Implementation of Bubble Sort function
def bubbleSort(arr):
    temp=copy.copy(arr)
    n = len(temp)
    ind = []
    for i in range(n):
        for j in range(0, n-i-1):
            if temp[j]<temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
    
    for i in range(n):
        ind.append(arr.index(temp[i]))
    
    return temp, ind


print("\n\nThis program will generate 15 random numbers in a list and sort them in descending order\n\n")

#Sorting a random matrix in descending order using lists
#Descending Order
#Generation of a random list
randomlist=[]
for i in range(0,15):
    n=random.randint(1,100)
    randomlist.append(n)
    
print("Generated random list 'R' ")
print(str(randomlist)[1:-1])

#Using the BubbleSort function to sort the list
sort_list,sort_ind = bubbleSort(randomlist)

print("\nThe list after sorting in descending order  'S' ")
print(*sort_list, sep= ', ')
print("\nThe mapping from S ---> R")
print(*sort_ind, sep = ', ')

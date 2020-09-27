import numpy as np

arr=[20,30,50,40,55,656,213,455,20,1,3,5,12,33,546]
for c in range(1,15):
    for i in range(1,15):
        if (arr[i-1]>arr[i]):
            s=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=s
print(arr)
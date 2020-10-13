import numpy as np
arr = input('enter 15 numbers separated by space:')
a=list(map(int, arr.split()))
arr = np.asarray(a)
n = len(arr)
b=arr
t=[]
for x in np.arange(n - 1):
    for y in np.arange(n - x - 1):
        if b[y] > b[y + 1]:
            b[y], b[y + 1] = b[y + 1], b[y]
print('sorted list:',b)
for x in b:
    t.append(a.index(x))
print('sorted indices:',t)



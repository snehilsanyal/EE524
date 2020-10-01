## Print an mxn matrix with random values in range[-2,5]

import numpy as np

print("Enter the values of m & n for an mxn matrix and click Enter after entering each element:") 
m = int(input())
n = int(input())

a = np.random.uniform(-2,5,(m,n))

print(m,"x",n,"random array is:")
print(a)

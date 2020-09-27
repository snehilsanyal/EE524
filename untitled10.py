#Q8
import numpy as np
m=int(input('enter 1st number:'))
n=int(input('enter 2nd number:'))
arr=np.random.randint(-2,5,m*n)
arr.reshape(m,n)

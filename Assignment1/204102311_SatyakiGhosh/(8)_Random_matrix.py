
import numpy as np
import random

rows=int(input('Enter number of rows:'))
col=int(input('Enter number of columns:'))

rand_matrix=np.random.randint(-2,5,(rows,col))
print(f'The random matrix of shape {rows}x{col}:')
print(rand_matrix)

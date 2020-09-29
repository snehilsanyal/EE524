import matplotlib.pyplot as plt
import numpy as np
from numpy import random
X=np.arange(-10,10,0.2)
Y=2*X+3
plt.plot(X,Y,color='black')
mean,var=0,1
s = np.random.normal(mean, var,100)
sigma=np.std(s)
y=2*X+3+sigma*s
plt.scatter(X,y,color='r')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

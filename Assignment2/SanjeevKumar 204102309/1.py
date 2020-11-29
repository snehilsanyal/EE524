from matplotlib import colors
import matplotlib.pyplot as plt
from random import uniform as ran
import numpy as np
a = []
b=  []
c = []
for i in range(100):
    x = ran(-10,10)
    b.append(x)
    y = 2*x+3
    a.append(y)
for i in range(100):
    h = a[i]+np.random.normal(0,1)# y = 2x+3+(sigma = 1)**2N(0,1)
    c.append(h)
plt.plot(b,a,color ='black')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend(['Y=2x+3'])
plt.scatter(b,c,color = 'red')
plt.title('Scatter points with N(0,1)')
plt.show()


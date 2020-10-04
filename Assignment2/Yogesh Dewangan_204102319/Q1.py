import random
import matplotlib.pyplot as plt
import numpy as np

a, b = 2, 3
j=100
x = [random.randrange(-10,10) for i in range(j)]
x=np.sort(x)
y=  [a*x[i]+b for i in range(j) ]
print(y) 
u=np.random.normal(0, 1, 100)
s= np.std(u)
v=[y[i]+s*u[i] for i in range(j)]
plt.scatter(x,v,c='red')
plt.plot(x,y,c='black')
plt.xlabel('x values---->')
plt.ylabel('The value of function---->')
plt.title('Generating points around line')
plt.rcParams['figure.facecolor']='orange'
plt.tight_layout()
plt.show()

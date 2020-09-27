import numpy as np
import math as m
import matplotlib.pyplot as plt

a2=[]
b2=[]
x=[]
y=[]
C=0
for phi in np.arange(0,2*(m.pi),2*(m.pi)/100):
    b = np.random.uniform(0, 2.5)
    a = np.random.uniform(0, 5)
    x1= a*(m.cos(phi))
    y1= b*(m.sin(phi))
    a1= 5*(m.cos(phi))
    b1= 2.5*(m.sin(phi))
    a2.append(a1)
    b2.append(b1)
    x.append(x1)
    y.append(y1)
    C=C+1

print(x)
print(y)

plt.scatter(a2,b2,c='red',marker='.')
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('SCATTER PLOT OF 100 POINTS INSIDE ELLIPSE')
plt.show()
print('Total number of points generated:',C)


#question Number -2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure()

x = np.arange(-10,10,0.2)
nor = np.random.randn(100)
y1 = 2*x + 3 + nor

a = np.arange(-10,10,0.1)
b = np.arange(-10,10,0.1)

ei = np.empty([200,200,100])
k=l=0
for i in a:
    l = 0
    for j in b:
        y2 = i*x+j
        ei[k][l] = y1-y2
        l+=1
    k+=1
E = np.empty([200,200])
k = l = 0
for i in a:
    l=0
    avg = 0
    for j in b:
        avg = sum(ei[k][l])
        E[k][l] = avg**2/100
        l+=1
    k+=1
X,Y = np.meshgrid(a,b)
Z = E
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111,projection ='3d')
ax.plot_surface(X,Y,Z,)
ax.set_xlabel('------> a')
ax.set_ylabel('------> b')
ax.set_zlabel('------> Error')
plt.show()

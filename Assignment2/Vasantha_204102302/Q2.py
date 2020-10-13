from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy as np

a=np.arange(-10, 10, 0.1)
b=np.arange(-10, 10, 0.1)
X=np.arange(-10, 10, 0.1)

s=np.std(X)
N=np.var(s)
u=np.random.normal(0,1,200)
Y=2*X+3+(N)*(u)

n=100

for i in range(0,200):
    E1=((Y-a*X[i]+b)**2)
    i+=1
    E2=E1/n 
    
fig = plt.figure()
ax=fig.gca(projection='3d')

a, b = np.meshgrid(a, b)
E2 = np.array([E1 for X,Y in zip(np.ravel(X), np.ravel(Y))])
E = E2.reshape(a.shape)

ax.plot_surface(a, b, E,cmap='plasma')

ax.set_xlabel('X-AXIS')
ax.set_ylabel('Y-AXIS')
ax.set_zlabel('ERROR')

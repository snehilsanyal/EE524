import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from random import uniform as ran
import numpy as np
x = ran(-10,10)
c=[]
for i in range(100):
    v=np.random.normal(0,1)
    y = 2*x+3+v
    c.append(y)
u = np.arange(-10,10,0.1)
v = np.arange(-10,10,0.1)
z = [[0 for x in range(len(u))]for x in range(len(v))]
for i in range(len(u)):
    for j in range(len(v)):
        sum = 0
        for k in range(100):
            er =  c[k] - (u[i] * x + v[j])
            sum = sum + er ** 2
        av = sum / 100
        z[j][i] = av
f = np.array(z)
u,v = np.meshgrid(u,v)
ax = plt.axes(projection = '3d')
ax.plot_surface(u,v,f)
plt.show()
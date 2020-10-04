#--- Q2. a

import numpy as np
a = np.arange(-10, 10, 0.1) #a ranges between -10 and 10 (given) with steps of 0.1
print("values of a varies between -10 and 10 with steps of 0.1:\n", a)
b = np.arange(-10, 10, 0.1) #b ranges between -10 and 10 (given) with steps of 0.1
print("values of b varies between -10 and 10 with steps of 0.1:\n", b)




#---- Q2. b - e

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

from sklearn.metrics import mean_squared_error 
from mpl_toolkits.mplot3d import axes3d


x = np.linspace(-10,10,200)
a = np.arange(-10,10,0.1)
b = np.arange(-10,10,0.1)
z = np.random.normal(0,1)

y1 = 2*x + 3 + z

E = np.zeros((200,200))

for i in range(200):
    for j in range(200):
        y = a[i]*x + b[j]
        y1 = 2*x + 3 + z
        E[i][j] = metrics.mean_squared_error(y1,y)
        
a,b=np.meshgrid(a,b)  
fig=plt.figure(figsize=(10,5))  #we have set figure size to (10,5)
ax=plt.axes(projection='3d')
ax.plot_surface(a,b,E)

surf = ax.plot_surface(a, b, E, cmap=cm.Spectral, linewidth=0, antialiased=False) #here Spectral is the color of the 3d surface. cm is actually imported from matplotlib
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_xlabel('a (x-axis)')
ax.set_ylabel('b (y-axis)')
ax.set_zlabel('E (z-axis)')

plt.show()


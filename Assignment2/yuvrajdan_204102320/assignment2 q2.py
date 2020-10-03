#Q2 plot error surface in 3d for  different values of a,b

import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure()
x=np.linspace(-10,10,200)
a=np.arange(-10,10,0.1)
b=np.arange(-10,10,0.1)
nor=np.random.normal(loc=0,scale=1) #mean=0 and sd=1
y1=2*x+3 + nor
E=np.zeros((200,200))

for i in range(200):
    for j in range(200):
        y=a[i]*x + b[j]
        y1=2*x+3 + nor
        E[i][j]=metrics.mean_squared_error(y1,y)
        
a,b=np.meshgrid(a,b)  
fig=plt.figure()  
axes=plt.axes(projection='3d')
axes.plot_surface(a,b,E)
plt.show()
 
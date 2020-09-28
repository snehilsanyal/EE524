import matplotlib.pyplot as plt
import random
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.cm as cm



#generation of 1x200 row matrix  for a and b
a=np.arange(-10,10,.1)
b=np.arange(-10,10,.1)

#generation of 1x200 matrix for x
x=np.arange(-10,10,.1)
noise1=np.random.normal(0,1,200)
y=2*x+3
sigma=np.std(x)
g_n=np.random.normal(0,1,200)
y1=y+sigma*g_n
##########
E=[]
for i in range(200):
    e=(y1-a[i]*x+b[i])**2
    avg_e=sum(e)/100
    E=np.append(E,avg_e)
    E1=np.array([E]).transpose()


##############
a,b=np.meshgrid(a,b)
fig=plt.figure()
axes=fig.add_subplot(111,projection='3d')
axes.plot_surface(a,b,E1)
plt.show()




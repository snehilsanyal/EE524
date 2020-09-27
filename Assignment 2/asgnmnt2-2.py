import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
a = np.arange(-10,10,0.2)
b = np.arange(-10,10,0.2)
x = np.arange(-10,10,0.2) 
y = 2*x+3
u=np.random.normal(0, 1, 100)
s= np.std(u)
y1=y+(s*u)
a,b =np.meshgrid(a,b)
e= (y1-a*x+b)**2
e1=e/100
fig = plt.figure() 
axes = fig.gca(projection ='3d') 
axes.plot_surface(a, b, e1) 
axes.set_xlabel('a----->')
axes.set_ylabel('b----->')
axes.set_zlabel('Error----->')
axes.set_title("Error surface plot")
axes.set_xlim(-10,10)
axes.set_ylim(-10,10)
axes.set_facecolor("orange")
plt.tight_layout()
plt.show() 


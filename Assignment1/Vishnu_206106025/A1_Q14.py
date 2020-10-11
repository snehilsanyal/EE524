
## This function intakes a set of random co-ordinates (x,y) and checks whether
## the points satisfy the conditions of a given 2D equation
## Whether the points lie inside of an ellipse with specified major(a) and minor axes(b)
 
def insidepoints(x,y,a,b):    
    insidex=[]
    insidey=[]
    k=0
    for i in range(1000):
        if (x[i]-u)**2/a**2 + (y[i]-v)**2/b**2 < 1:
            insidex.append(x[i])
            insidey.append(y[i])
            k+=1
        if k==100:
            break
    return insidex,insidey


#Example code

import numpy as np
from matplotlib import pyplot as plt
from math import pi
import random

# x and y value of center co-ordinate (u,v)
u=5.     
v=-5    
# Major and Minor Axes
a=10  #radius on the x-axis
b=5   #radius on the y-axis

n=100 # no of points in the ellipse
t = np.linspace(0, 2*pi, n)

#The ellipse
boundx=u+a*np.cos(t)
boundy=v+b*np.sin(t)

#Random (x,y) points
x=np.random.randint(-5,15,10000)
y=np.random.randint(-10,10,10000)

# Finding points within the ellipse
xin,yin=insidepoints(x,y,a,b)

#Plot to verify

plt.plot(u+a*np.cos(t),v+b*np.sin(t))
plt.grid(color='lightgray',linestyle='--')
plt.title('Points within Ellipse')
plt.scatter(xin,yin,c='k')
plt.show()






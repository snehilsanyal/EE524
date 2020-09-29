"""
Created on Sun Sep 27 21:54:39 2020

@author: keyen

"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.stats import norm

# X value and Y value
x=np.arange(-10,10,0.2)
y=2*x+2
#Vector for varying a and b  
a=np.arange(-10,10,0.1)
b=np.arange(-10,10,0.1)

# Varying a and b and calculating the error surface
line=[]
noise_line=[]    
eror=[] 
erval=[]  
erval_list=[]
abserr=[]
for i in range(0,len(a)):
    line=[];noise_line=[];eror=[];erval=[];abserr=[]
    for j in range(0,len(b)):    
        noise_line=a[i]*x+b[j] # The line with varying a and b
        line=2*x+3+norm.rvs(0,1,100) # original line with normally distributed error
        eror=np.array(noise_line)-np.array(line) 
        abserr=np.mean(np.square(eror))/100 # average error for a set of a and b
        erval.append(abserr)
    erval_list.append(erval)
    


errsurf=np.array(erval_list)

ax1,ax2=np.meshgrid(a,b)



# Plot the surface.

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(ax1, ax2, errsurf, cmap=cm.plasma,
                       linewidth=0, antialiased=False)
#fig.colorbar(surf, shrink=0.5, aspect=5)
fig.colorbar(surf, orientation="vertical", pad=0.05)
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('error')
ax.set_title('Error Surface')
plt.show()



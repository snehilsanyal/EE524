#PLOTTING ERROR SURFACE


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax1= fig.add_subplot(111, projection='3d')
Z= np.zeros((200,200))                                        #TO CREATE A TWO DIMENSIONAL ARRAY
x= np.random.uniform(-10, 10, 100)
a= np.arange(-10, 10, 0.1)
b= np.arange(-10, 10, 0.1)
for i in range(200):
    for j in range(200):
        Yj= x*a[i] + b[j]
        Yk= 2*x+3 + np.random.normal()
        Z[i][j]=np.sum((Yk-Yj)**2) * 0.01                    #EACH SUM OF [(  ei^2 ) *0.01] IS STORED AT RESPECTIVE 40000 PLACES IN MATRIX        
a,b=np.meshgrid(a,b)
mycmap= plt.get_cmap('gist_earth')
ax1.plot_surface(a, b, Z, cmap=mycmap)
ax1.set_xlabel("VALUES OF a")
ax1.set_ylabel("VALUES OF b")
ax1.set_zlabel("MEAN OF SQ. ERROR")
plt.show()

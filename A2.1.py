#PLOTTING NOISY POINTS AROUND LINE.

import numpy as np
import matplotlib.pyplot as plt

x= np.random.uniform(-10,10,100)
y=2*x+3
plt.plot(x,y,'k')
z=np.random.randn(100)
y=y+z
plt.scatter(x,y,c='r')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

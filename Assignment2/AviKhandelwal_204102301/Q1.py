

#------------------------------------------Assignment-2, Question-1, Avi Khandelwal-------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


x = np.random.uniform(-10,10,100) # Generating 100 values of x in (-10,10), all uniformly distributed  
y = 2*x + 3 # Calculating y from x
nor = np.random.randn(100) # Generating 100 random points following normal distribution
y1 = 2*x + 3 + nor # Corrupting the y values previously obtained with gaussian noise


plt.plot(x,y,color='k',linewidth=1,label = "y = 2x + 3")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x,y1,s=5,color='r',label = "Gaussian noise")
plt.title("Plot of a line with noisy points")
plt.legend()
plt.grid(True)
plt.show()

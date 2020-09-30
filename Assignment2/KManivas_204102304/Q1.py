# Program to plot the line y = ax+b and scattered plot of y with Gaussian noise

import numpy as np
import matplotlib.pyplot as plt

# Initialization
a = 2
b = 3
u = 0
sig = 1

# Assigning 100 different points to x in the range [-10,10]
x = np.linspace(-10,10,100)
# print(x)

# Calculate y for above values of x
y = [(a*i)+b for i in x]
# print(y)

# Generate 100 points of Gaussian noise N(0,1)
y_noise = np.random.normal(u,sig,100)
# print(y_noise)

# Add the noise to y to get actual values of y
y_act = y + (sig*y_noise)

# Plot the line and scattered points (generated from Noise)
plt.plot(x,y,color='black',label='y=3x+2')
plt.scatter(x,y_act,color='red',label='y=3x+2+[sigma*N(0,1)]',marker='.')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot showing Training data and Predicted data')
plt.legend()
plt.grid()
plt.show()



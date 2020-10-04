import numpy as np
from matplotlib import pyplot as plt

a=2
b=3
N=100
x=np.linspace(-10,10,N)     # 100 points chosen in the range [-10,10]
mu=0    # mean=0
sigma=1 # standard deviation=1

gaussian_points=np.random.normal(mu, sigma, N)  #picking 100 points from a normal distribution
y= a*x + b   #   y= ax + b for the set of points in x
y_points=y+sigma*gaussian_points  #   addding the gaussian_points to the line y = 2x + 3

plt.plot(x,y,'k',label='y=2x+3',linewidth=3)    # plotting the line y = 2x + 3
plt.scatter(x,y_points,c='R')   #   scatter plot of the values mixed with gaussian noise

plt.title('Straight line')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend()
plt.grid(True, color='g')

plt.show()  #   showing the plot

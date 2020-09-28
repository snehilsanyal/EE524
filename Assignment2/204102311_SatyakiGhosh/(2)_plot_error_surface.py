from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

def error(a,b):

    N=100
    x=np.linspace(-10,10,N) #taking 100 points for x in the range [-10,10]
    mu=0    # mean=0
    sigma=1 #standard deviation=1
    e=np.ndarray(shape=np.shape(a),dtype='float')   #initializing a numpy error for holding the error values
    for i in range(np.shape(a)[0]):         # looping from 0 to 200 for a-axis
        for j in range(np.shape(b)[0]):     # looping from 0 to 200 for b-axis
            gaussian_points=np.random.normal(mu, sigma, N)  # picking 100 points from the normal distribution
            y_hat= a[i][j]*x + b[i][j]      #   calculating y=ax+b for a specific pair (a,b)
            y=(2*x + 3)+sigma*gaussian_points     #   2x + 3 + N(0,1)
            e[i][j]=np.sum((y-y_hat)**2)/N  #   calculating the mean squared error
    return e


fig = plt.figure()  #initializing an object for plotting
ax = fig.gca(projection='3d')   #required for 3d plot

start=-10   # limits and interval of a and b
end=10
interval=0.1

a=np.arange(start,end,interval) # creating a numpy array for a and b
b=np.arange(start,end,interval)
a,b=np.meshgrid(a,b)    # creating a meshgrid for 3d plot
print(f'Mean error value of the entire surface= {np.mean(error(a,b))}')     #printing mean error value of the entire surface
print('Error for all combinations of a and b (in 200x200 format):') #printing the 200x200 error matrix
print(error(a,b))

# a is x-axis,  b is y-axis, error(a,b) is the error-surface values
surf = ax.plot_surface(a,b, error(a,b), cmap=cm.coolwarm,edgecolor='none')  #linewidth=0, antialiased=False
ax.set_xlabel('$a$', rotation=150)  # naming the axes
ax.set_ylabel('$b$')
ax.set_zlabel('$Error$', rotation=60)

# To add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title('Error Surface plot')  # title for the plot
plt.show()  # showing the plot

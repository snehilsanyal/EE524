import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
#Function to calculate average error for a paritcular 'a' and 'b' and return the value
def error_cal(a,b,x,y):
    y_new = a*x + b
    error = y_new - y
    error_sq = error*error
    m = len(y)
    mse = error_sq.sum()/m

    return mse
#Function to append mean square values for all combinations of (a,b) in a  matrix and
#plot it on 3D plot having x = a; y = b; and z = error values

def error(slope,intercept):
    a = np.arange(-10,10,0.1)
    b = np.arange(-10,10,0.1)
    x = np.linspace(-10,10,num=100)
    y = slope * x + intercept #To generate a line with slope and intercept passed by user

    mu = float(input("\nEnter the mean of random distribution: "))
    st_dev = float(input("\nEnter the standard deviation of random distribution: "))

    s = st_dev * np.random.normal(mu,st_dev,100)
    y_new = y + s #Adding noise to the y values

    cost = np.array([]) #MSE matrix
    for i in range(len(a)):
        for j in range(len(b)):
            mse = error_cal(a[i],b[j],x,y_new)
            cost = np.append(cost,mse)

    print("\n\nThe size of the error array is: ",np.size(cost))
    cost = np.reshape(cost,[len(a),len(b)])

    #Plotting the curve
    mycmap = plt.get_cmap('gist_earth')
    a,b = np.meshgrid(a,b)
    ax.plot_surface(a,b,cost)
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('Error')

    plt.show()

def main():
    slope = float(input('\nEnter the value of the slope of the line: '))
    intercept = float(input('\nEnter the vlaue of y intercept of the line: '))
    error(slope,intercept)


if __name__ == '__main__':
    main()

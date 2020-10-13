import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Defining straight parameters and plotting straight line
def st_line():
    slope = int(input('Enter the slope of the line: '))
    intercept = int(input('Enter the y-intercept value: '))
    print('\n\nThe equation of the straight line is: y = ', str(slope),'*x  +  ',str(intercept))

    #Generating an array of 100 linearly spaced numbers between -10 to 10
    x = np.linspace(-10,10, num = 100)
    y = np.array([])

    #FInding y corresponding to every element of x
    for i in range(100):
        y_i = slope * x[i] + intercept
        y = np.append(y,y_i)

    #Modifying y values with normal distribution 1*N(0,1)
    modification_arr = norm_dist()
    y_new = y+modification_arr

    #Writing X and Y values to a csv file
    data_frame = {'X-coordinate' : x, 'Y-coordinate' : y,'Y-coordinate_random': y_new}
    df = pd.DataFrame(data_frame)
    df.to_csv('Data1.csv')

    #Plotting the straight line and normally distributed point around the line
    plt.plot(x,y,'k',x,y_new,'ro')
    plt.axis([-10, 10, -40, 40])
    plt.show()
#Generation of normally distributed points
def norm_dist():

    mu = float(input('\n\nEnter the mean of normal distribution: '))
    var = float(input('\nEnter the variance of the normal distribution: '))
    sigma = var**0.5
    s = np.random.normal(mu,sigma,100)
    s1 = sigma*s
    return s1

def main():
    st_line()

if __name__ == '__main__':
    main()

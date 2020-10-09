# Program to scatter points within an ellipse

import numpy as np
import matplotlib.pyplot as plt
import math

# a & b values of ellipse where a=len of Major axis/2 & b=len of Minor axis/2
a, b = 5.0, 2.5

# Centre of Ellipse  
p, q = 5.0, -5.0

# Creating a set of 100 values of x between 0 and 10
x1 = np.linspace(10,0,50)
x1 = x1.tolist()
x2 = np.linspace(0,10,50)
x2 = x2.tolist()

x = x1 + x2
# print(x)


theta1 = []
theta2 = []
y_temp_p = []
y_temp_n = []
y_temp = []
y = []

# Calculating the theta values from x list using the eq x=acos(theta)
for i in x1:
    temp1 = math.acos((i-p)/a)
    theta1.append(temp1)
    
for i in x2:
    temp2 = math.acos((i-p)/a)
    temp2 = 0 - temp2
    theta2.append(temp2)
    
theta = theta1 + theta2

# print(theta)

# Calculating the y_temp values from theta list using the eq y=bsin(theta)
for j in theta:
    temp = q + (b*math.sin(j))
    y_temp.append(temp)

# print(y_temp)

# Generating random numbers between Major axis and boundary of ellipse for each value of (x,y_temp)
for i in range(len(x)):
    temp = np.random.uniform(q,y_temp[i])
    y.append(temp)

# Plotting the Ellipse and the points
plt.plot(x,y_temp,label='Ellipse',color='blue',linewidth='2') 
plt.scatter(x,y,label='Points',color='red',marker='.')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Points within Ellipse")
plt.legend()
plt.show()


    

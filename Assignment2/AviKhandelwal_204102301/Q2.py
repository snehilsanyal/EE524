

#------------------------------------------Assignment-2, Question-2, Avi Khandelwal-------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.random.uniform(-10,10,100) # Generating 100 values of x in (-10,10), all uniformly distributed  
y = 2*x + 3 # Calculating y from x
nor = np.random.randn(100) # Generating 100 random points following normal distribution
y1 = 2*x + 3 + nor # Corrupting the y values previously obtained with gaussian noise


a = np.arange(-10,10,0.1) # obtaining 200 a values (-10,10)
b = np.arange(-10,10,0.1) # obtaining 200 b values (-10,10)


e = y1 - y # Calculating e vector of dimension 100 which is storing noise in y values
msq = np.sum(e**2)/100 # Calculating mean square error through the formula

print("Values of a and b as per question: ",2,3,"and the corresponding error:",msq,"\n")
error = np.array([100]) # Initialising error vector

A = 0 # Shows the value of a calculated by squared error function
B = 0 # Shows the value of b calculated by squared error function
E = 0 # shows the corresponding error for that particular a and b values as calculated by squared error function

#Iterating over all a and b values 
for i in a:
    for j in b:
       y = i*x + j 
       e = y1 - y
       sq = sum(e**2)/100
       # To find out the a,b corresponding to which error is minimum and storing them in A,B and error in E
       if sq < np.min(error): 
            A = i
            B = j
            E = sq
       error = np.append(error,sq)

error = np.delete(error,0) #Deleting the '100' element in error vector which was earlier inititalied
error = error.reshape(200,200) # Reshaping the vector in 200x200


a, b = np.meshgrid(a, b)
print("Values of a and b as per squared error function: ",A,B,"and the corresponding error:",E) 
#We can see that values of A, B and E are coming close to a=2,b=3 and the error and hence the method works correctly 

surf = ax.plot_surface(a,b,error, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.xlabel("a")
plt.ylabel("b")
plt.title("Error Surface")

plt.show() 

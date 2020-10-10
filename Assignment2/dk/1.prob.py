import matplotlib.pyplot as plt
import random
import numpy as np

a=2
b=3
sigma=5
#generation of n value for x

x=[random.randrange(-10,10) for j in range(100)]
#generating sigma*N(0,1)
noise1=np.random.normal(0,1,100)

#generating matrix without noise

ones_x=np.array([[1 for i in range(100)],x]).transpose()

#generating matrix with noise

ones_x_noise=np.array([[1 for i in range(100)],x,noise1]).transpose()

#generating column vector without noise
parameter=np.array([[b,a]]).transpose()
#generating column vector with noise
parameter_noise=np.array([b,a,sigma]).transpose()
#calculation of y[i]=b+ax[i]
#[1 x].[b a]'=b+ax
y_i=np.dot(ones_x,parameter)

#calculation of y[i]=b+ax[i]+sigma*N(0,1)
#[1 x N1].[b a sigma]'=b+ax+sigma.N1
y_i_noise=np.dot(ones_x_noise,parameter_noise)


plt.scatter(x,y_i_noise,color="r")
plt.plot(x,y_i,color="k")


plt.show()

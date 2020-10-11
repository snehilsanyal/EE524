# Q1  Generate a set of points around a line y=ax + b

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
a=2
b=3
y=a*x+b
plt.plot(x,y,color='black')
p=np.random.normal(loc=0,scale=1,size=10*10) #mean=0 ,sd=1
q=a*x+b +p
plt.scatter(x,q,color='red')
plt.plot(x,y,color='black')
plt.xlabel('X axes')
plt.ylabel('Y axes')


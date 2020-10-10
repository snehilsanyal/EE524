
#Q14
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
a=5
b=-5
t=np.linspace(0,2*np.pi,100)
x=5*np.cos(t)
y=2.5*np.sin(t)
plt.scatter(x,y)
p=np.random.randn(100)
q=np.random.randn(100)
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')
plt.title('ELLIPSE')
plt.scatter(p,q)
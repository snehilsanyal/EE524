import matplotlib.pyplot as plt
import numpy as np
import random
a = 2
b = 3
x=np.linspace(-10,10,100)
y=[a*x[i]+b for i in range(100)]
plt.plot(x,y,c='black')
plt.xlim(-10,10)
s=np.std(x)
u=np.random.normal(0,1,100)
z=(y)+(s)*(u)
plt.scatter(x,z,c='red')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('Y=AX+B')
plt.show()

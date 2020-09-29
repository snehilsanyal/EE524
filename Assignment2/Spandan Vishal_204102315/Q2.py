import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits import mplot3d
a=np.arange(-10,10,0.1)
b=np.arange(-10,10,0.1)
x=np.arange(-10,10,0.1)
s=np.random.normal(0,1,200)
sigma=np.std(s)
avg_e=np.zeros((200,200))
for i in range(200):
  sum=0
  for j in range(200):
    yi=2*x[j]+3+sigma*s[j]
    yi_hat=a[i]*x[j]+b[j]
    ei=yi-yi_hat
    sum=sum + (ei**2)/200
  avg_e[i][j]=sum

a1,b1=np.meshgrid(a,b)
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.plot_surface(a1, b1, avg_e,cmap='viridis');
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Average error')
plt.show()

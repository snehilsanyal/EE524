## Program to print line plot y = 3x+2

import matplotlib.pyplot as plt
import numpy as np

a = -10.0
b = 10.0

x = np.linspace(a,b,201)
print(x)
y = [3*j+2 for j in x]
print(y)
# y1 = [4*j+3 for j in x]
plt.plot(x,y,color='green',label='y=3x+2',linewidth='2')
# plt.plot(x,y1,color='yellow',label='y=4x+3',linewidth='2')
plt.xlabel('x range',color='blue')
plt.ylabel('y range',color='blue')
plt.title('Lineplot',color='red')
plt.legend()
plt.grid()
plt.show()




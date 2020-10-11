#Question Number -1 
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10,10,0.2)
y = 2*x + 3
nor = np.random.randn(100)
y1 = 2*x + 3 + nor
plt.plot(x,y, color='black')
plt.scatter(x,y1,color ='red')
plt.xlabel('x----->')
plt.ylabel('y------>')
plt.title('plot of y = 2x+3 and some point around line')
plt.show()

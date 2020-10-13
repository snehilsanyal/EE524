import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10)
y = 3*x+2
plt.plot(x, y,label='y=3x+2')
plt.xlabel('x axis', c='m')
plt.ylabel('y axis', c='m')
plt.show()



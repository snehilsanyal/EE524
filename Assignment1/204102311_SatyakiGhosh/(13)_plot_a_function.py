from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-10,10,10000)
y=3*x + 2

plt.plot(x,y,'g',label='y=3x+2',linewidth=5)

plt.title('Straight line')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend()
plt.grid(True, color='k')

plt.show()

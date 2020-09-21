import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2,2,50)
plt.plot(x,3*x+2)
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('y = 3x + 2')
plt.show()

#Q13
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
x=np.linspace(-10,10,10)
y=3*x +2
plt.plot(x,y)
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')
plt.title('TITLE')
plt.grid(color='y',linestyle='--')
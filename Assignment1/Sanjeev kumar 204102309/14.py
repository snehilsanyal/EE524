import matplotlib.pyplot as plt
import random as ran
import numpy as np

t = []
u = []
x=np.linspace(-4,10,100)
y=np.linspace(-10,5,100)
x, y = np.meshgrid(x, y)
plt.contour(x,y,(((x-5)**2/25)+(y+5)**2/6.25),[1],colors='r')
while len(t) < 100:
    a = ran.uniform(0, 10)
    b = ran.uniform(-7.5, -2.5)
    # simplifying the equation of ellipse as follows-
    if (4 * b * b + 40 * b + 25 * a * a - 250 * a + 700) < 0:
        t.append(a)
        u.append(b)
    else:
        continue


plt.scatter(t, u, label='Scatter plot', color='c')
plt.legend()
plt.grid()
plt.show()



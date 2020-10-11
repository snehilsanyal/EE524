import matplotlib.pyplot as plt
import random

X=[random.randrange(200) for i in range(100)]
y=[((0.5*((75+10*i-i**2)**.5))-5) for i in X]
plt.plot(X,y)
plt.show()
print(X)
print(y)

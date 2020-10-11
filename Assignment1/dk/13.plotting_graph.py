import matplotlib.pyplot as plt
import random
x=[random.randrange(-10,10) for i in range(10)]
y=[3*i+2 for i in x]

print(x)
print(y)
plt.plot(x,y)
plt.title('problem no.13')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

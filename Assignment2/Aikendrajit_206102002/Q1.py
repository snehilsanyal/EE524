#---- Q1. a

import numpy as np
import matplotlib.pyplot as plt

a = 2
b =3
x = np.linspace(-10,10,10)
y = a*x + b
plt.plot(x,y, '-b', label = 'y=ax+b')
plt.title('Graph of y=ax+b')
plt.grid()
plt.show()


#---- Q1. b

import numpy as np
import matplotlib.pyplot as plt

# declare a and b as given values
a = 2
b = 3
x = np.linspace(-10,10,100)
y = a*x + b
plt.plot(x,y, '_b', label = 'y=ax+b') #these 100 points are shown as "_" and it forms a straight line as shown in the graph below
plt.title('Graph of y=ax+b')
plt.grid()
plt.show() 




#-----  Q1. c

import numpy as np
from sympy import solve #sympy is a python library for symbolic maths

xi = int(input("Enter any number:"))
yi = 2*xi + 3
solve(yi)
print("The value of yi is:",yi)



#----- Q1. d

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10)
y = 2*x + 3
plt.plot(x,y, '-k', label = 'y=ax+b')
plt.title('Graph of y=ax+b')
plt.grid()
plt.show()




# ----   Q1. e & f

import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0,10,10)
y = 2*x + 3
plt.plot(x,y, '-k', label = 'y=ax+b')
plt.title('Graph of y=ax+b')
plt.grid()
 
def y(x, m, b):
    return m*x + b

X = np.linspace(0, 10, 100)
y_above = [y(x, 2, 3) + abs(random.gauss(0,1)) for x in X] #here we replace m = 2, b = 3 (given) & mean = 0, std. deviation = 1 (square root of variance. and it is given that variance is 1.)
y_below = [y(x, 2, 3) - abs(random.gauss(0,1)) for x in X]

plt.scatter(X, y_below, c = 'r')
plt.scatter(X, y_above, c = 'r')
plt.show()


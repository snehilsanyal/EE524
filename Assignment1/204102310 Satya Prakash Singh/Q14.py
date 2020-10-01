import matplotlib.pyplot as mp
import numpy as np
import random as rdm
import math

def ellipse_point():

    x = np.array([])
    y = np.array([])
    print('\n__The program is for the ellipses with major axis parallel to x-axis__\n')
    maj_axis = float(input('Enter the length of major axis of ellipse: '))
    min_axis = float(input('Enter the length of minor axis of ellipse: '))
    x0 = float(input('Enter the x-co-ordinate of centre of ellipse: '))
    y0 = float(input('Enter the y-co-ordinate of centre of ellipse: '))

    x_min = (x0 - (maj_axis)/2)
    x_max = (x0 + (maj_axis)/2)

    for i in range(100):
        x = np.append(x,rdm.uniform(x_min,x_max))
    for i in range(100):
        y_min = (y0 -((min_axis/maj_axis)* math.sqrt((maj_axis/2)**2 -(x[i]-x0)**2)))
        y_max = (y0 +((min_axis/maj_axis)* math.sqrt((maj_axis/2)**2 -(x[i]-x0)**2)))
        y = np.append(y,rdm.uniform(y_min,y_max))

    mp.plot(x,y, 'rs')
    mp.show()


def main():
    ellipse_point()

if __name__ == '__main__':
    main()

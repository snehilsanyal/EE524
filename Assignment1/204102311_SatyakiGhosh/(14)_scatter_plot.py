import numpy
import matplotlib.pyplot as plt
import random

# Returns theta in [-pi/2, 3pi/2]
def generate_theta(a, b):
    u = random.random()
    #https://en.wikipedia.org/wiki/Inverse_transform_sampling
    theta = numpy.arctan(b/a * numpy.tan(numpy.pi*u/2))     # for increasing chances of choosing theta where the radius is larger ,ie. closer to 0 than pi/2
    #theta=random.random()*numpy.pi
    v = random.random() #to generate theta in all 4 quadrants
    if v < 0.25:
        return theta
    elif v < 0.5:
        return numpy.pi - theta
    elif v < 0.75:
        return numpy.pi + theta
    else:
        return -theta

def radius(a, b, theta):
    return a * b / numpy.sqrt((b*numpy.cos(theta))**2 + (a*numpy.sin(theta))**2) #maximum permissible radius depending on theta for the given ellipse (derived using polar form of ellipse)

def random_point(a, b):
    random_theta = generate_theta(a, b)
    max_radius = radius(a, b, random_theta)
    random_radius = max_radius * numpy.sqrt(random.random())    #square-root taken to generate more points towards the periphery than the centre

    return numpy.array([
        random_radius * numpy.cos(random_theta),    # X-coordinate
        random_radius * numpy.sin(random_theta)     # Y-coordinate
    ])

a = 5
b = 2.5
ux=5
uy=-5
N=100

points = numpy.array([random_point(a, b) for _ in range(N)])

plt.scatter(points[:,0]+ux, points[:,1]+uy)
plt.title(f'Scatter plot inside an ellipse ({N} Points)')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.grid(True, color='k')
plt.show()

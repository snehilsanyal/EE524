import numpy as np
class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def conjugate(self):
        c = np.complex(self.a, self.b)
        d = np.conjugate(c)
        return d
    def angle(self):
        c = np.complex(self.a, self.b)
        d = np.arctan(self.b/self.a)*180/np.pi
        return d
    def absolute(self):
        c = np.complex(self.a, self.b)
        return abs(c)
    def add(self,c2):
        c1 = np.complex(self.a, self.b)
        c2 = np.complex(c2.a,c2.b)
        e = c1+c2
        return e
    def substract(self,c2):
        c1 = np.complex(self.a, self.b)
        c2 = np.complex(c2.a,c2.b)
        e = c1-c2
        return e
    def multiply(self,c2):
        c1 = np.complex(self.a, self.b)
        c2 = np.complex(c2.a,c2.b)
        e = c1*c2
        return e
    def divide(self,c2):
        c1 = np.complex(self.a, self.b)
        c2 = np.complex(c2.a,c2.b)
        e = c1/c2
        return e


c1=complex(1,1)
c2= complex(2,5)
print(c1.conjugate())
print(c1.absolute())
print(c1.angle(),end='degrees\n')
print(c1.add(c2))
print(c1.substract(c2))
print(c1.multiply(c2))
print(c1.divide(c2))



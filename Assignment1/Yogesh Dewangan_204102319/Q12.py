import cmath
from math import sqrt

class Complex(object):

    def init(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def sub(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def mul(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))

    def div(self, other):
        r = (other.real**2 + other.imag**2)
        return Complex((self.real*other.real - self.imag*other.imag)/r,
            (self.imag*other.real + self.real*other.imag)/r)

    def abs(self):
        return ((self.real**2) + (self.imag**2))**0.5
    
    def conjugate(self):
        return complex(self.real,-self.imag)
    def phase(self):
        return cmath.phase(self)
    
    
c1=complex(2,3)
c2=complex(3,5)
print('c1 =',c1)
print('c2 =',c2)
add=c1+c2
print('add =',add)
sub=c1-c2
print('sub =',sub)
mul=c1*c2
print('mul =',mul)
div=c1/c2
print('div =',div)
abs =(c1.real**2+c1.imag**2)**0.5
print('abs c1 =',abs)
abs =(c2.real**2+c2.imag**2)**0.5
print('abs c2 =',abs)
phase =cmath.phase(c1)
print('phase c1 =',phase )
phase =cmath.phase(c2)
print('phase c2 =',phase )
conjugate=complex(c1.real,-c1.imag)
print('conj c1 =',conjugate)
conjugate=complex(c2.real,-c2.imag)
print('conj c2 =',conjugate)




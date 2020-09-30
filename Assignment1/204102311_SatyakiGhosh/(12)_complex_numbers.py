import cmath

class Complex_Numbers:
    def __init__(self,value):
        self.cmplx=value

    def conjugate(self):
        c=self.cmplx
        x=c.real
        y=c.imag
        return complex(x,-y)

    def absolute_value(self):
        return abs(self.cmplx)

    def add(self,other_no):
        return self.cmplx+other_no.cmplx

    def multiply(self,other_no):
        return self.cmplx*other_no.cmplx

    def divide(self,other_no):
        return self.cmplx/other_no.cmplx

    def phase(self):
        return cmath.phase(self.cmplx)

a=complex(1,1)
b=complex(3,5)

c1=Complex_Numbers(a)
c2=Complex_Numbers(b)

print(f'First complex number: {a}')
print(f'Second complex number: {b}')
print(f'Additon {a} and {b}: {c1.add(c2)}')
print(f'Conjugate of {a}: {c1.conjugate()}')
print(f'Conjugate of {b}: {c2.conjugate()}')
print(f'Multiplication {a} and {b}: {c1.multiply(c2)}')
print(f'Division of {a} by {b}: {c1.divide(c2)}')
print(f'Absolute value of {a}: {c1.absolute_value()}')
print(f'Absolute value of {b}: {c2.absolute_value()}')
print(f'Phase of {a}: {c1.phase()} radians')
print(f'Phase of {b}: {c2.phase()} radians')

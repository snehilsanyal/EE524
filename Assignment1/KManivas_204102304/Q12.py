## Program to define complex class

import math

class complex:
    
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def __repr__(self):
        if self.im >= 0:
            return f"{self.re}+j{abs(self.im)}"
        else:
            return f"{self.re}-j{abs(self.im)}"
    def conjugate(self):
        if self.im >= 0:
            return f"{self.re}-j{abs(self.im)}"
        else:
            return f"{self.re}+j{abs(self.im)}"
    def absolute(self):
        return math.sqrt((self.re**2)+(self.im**2))
    def angle(self):
        return math.degrees(math.atan(self.im/self.re))
    def add(self, c):
        re = self.re + c.re
        im = self.im + c.im
        if im >= 0:
            return f"{re}+j{abs(im)}"
        else:
            return f"{re}-j{abs(im)}"
    def subtract(self, c):
        re = self.re - c.re
        im = self.im - c.im
        if im >= 0:
            return f"{re}+j{abs(im)}"
        else:
            return f"{re}-j{abs(im)}"
    def multiply(self, c):
        re = self.re * c.re - self.im * c.im
        im = self.re * c.im + self.im * c.re
        if im >= 0:
            return f"{re}+j{abs(im)}"
        else:
            return f"{re}-j{abs(im)}"
    def divide(self,c):
        c1_m = self.absolute()
        c1_a = self.angle()
        c2_m = c.absolute()
        c2_a = c.angle()
        c3_m = c1_m/c2_m
        c3_a = c1_a-c2_a
        c4_re = round(c3_m * math.cos(c3_a),2)
        c4_im = round(c3_m * math.sin(c3_a),2)
        if c4_im >= 0:
            return f"{c4_re}+j{abs(c4_im)}"
        else:
            return f"{c4_re}-j{abs(c4_im)}"
        

c1 = complex(1,2)
c2 = complex(3,4)

print("The conjugate of c1 is:", c1.conjugate())
print("The conjugate of c2 is:", c2.conjugate())
print("The absolute value of c1 is:", c1.absolute())
print("The absolute value of c2 is:", c2.absolute())
print("The angle of c1 is:", c1.angle())
print("The angle of c2 is:", c2.angle())
print("The addition of c1 & c2 is:", c1.add(c2))
print("The subtraction of c1 & c2 is:", c1.subtract(c2))
print("The multiplication of c1 & c2 is:", c1.multiply(c2))
print("The division of c1 & c2 is:", c1.divide(c2))

        
        
    


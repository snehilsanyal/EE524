#Q12
import cmath 
class complex_:
    def __init__(self,z1,z2):
        self.z1=z1
        self.z2=z2
    def add(self):    
        return self.z1+self.z2
    def sub(self):    
        return self.z1-self.z2
    def multi(self):    
        return self.z1*self.z2
    def divide(self):    
        return self.z1/self.z2
    def mode(self):
        return  ((self.z1)**2 + (self.z2)**2)**.5
    def phase1(self):
        return cmath.phase(self.z1) 
    def phase2(self):
        return cmath.phase(self.z2) 
z1=complex(3,5)
z2=complex(4,6)
result=complex_(z1,z2)
a=result.add()
b=result.sub()
c=result.multi()
d=result.divide()
e=result.mode()
f=result.phase1()
g=result.phase2()
print(a,b,c,d,e,f,g)

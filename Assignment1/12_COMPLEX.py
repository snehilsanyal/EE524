import cmath as c
class comp:

    def cnj(self1,c1):
        print('conjugate of c1 is:',c1.conjugate())

    def abs_val(self,c1):
        print('absolute value of c1 is:', abs(c1) )

    def addi(self,c1,c2):
        return c1+c2

    def subt(self,c1,c2):
        return c1-c2

    def mult(self,c1,c2):
        return c1*c2

    def divi(self,c1,c2):
        return c1/c2

    def angle(self,c1):
        return c.phase(c1)


c1= complex(2, 3)
c2= complex(5, 6)

obj=comp()

obj.abs_val(c1)
obj.cnj(c2)
print('sum of c1 and c2 is:', obj.addi(c1,c2))

print('subtration of c1 and c2 is:', obj.subt(c1,c2))

print('c1*c2:', obj.mult(c1,c2))

print('c1/c2:', obj.divi(c1,c2))

print('phase of c1 in radians:', obj.angle(c1))







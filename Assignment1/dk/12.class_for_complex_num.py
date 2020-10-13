class complex:
    __real=int()
    __im=int()
    def set_data(self,x,y):
        self.real=x
        self.im=y

    def show_data(self):
        print("Re= ",self.real," ","Im= ",self.im)
    def sum(self,c):
        self.real=self.real+c.real
        self.im=self.im +c.im
        return self
    def substraction(self,c):
        self.real=c.real-self.real
        self.im=c.im-self.im
        return self
    def multiplication(self,c):
        self.real=self.real*c.real
        self.im=self.im*c.im
        return self
    def div(self,c):
        self.real=self.real/c.real
        self.im=self.im/c.im
        return self
    def conjugate(c):
        c.real=c.real
        c.im=-(c.im)
        return c
    def abs_value(c):
        return (((c.real)**2+(c.im)**2)**0.5)


c1=complex()
c2=complex()
c1.set_data(3,2)
c2.set_data(4,5)
c3=c1.sum(c2)
print("sum is: ")
c3.show_data()
c4=c1.substraction(c2)
print("difference is:")
c4.show_data()
c3=c1.multiplication(c2)
print("c1 X c2 is:")
c3.show_data()
c3=c1.div(c2)
print("c1/c2 is :")
c3.show_data()
print(c1.abs_value())
c3=c1.conjugate()



def gcd(x,y):
    if x==0:
        return y
    return gcd(y%x,x)

def lcm(x,y):
    return(x*y/gcd(x,y))

x = int ( input ( "enter value of x: " ) )

y = int ( input ( "enter value of y: " ) )

print('LCM OF', x, 'and', y, 'is :', lcm(x, y) )
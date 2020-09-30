a = int(input('a:'))
b = int(input('b:'))
c=[]
for x in range(a,b+1):
    for y in range(2, x + 1):
        if x % y == 0:
            c.append(y)
    if c[0] == x:
        print(x,end=' ')
    c.clear()
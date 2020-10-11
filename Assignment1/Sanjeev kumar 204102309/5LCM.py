a = int(input('a:'))
b = int(input('b:'))
c=[]
d=[]
for x in  range(1,b+1):
    c.append(a*x)
for x in range(1,a+1):
    d.append(b*x)
for x in d:
    if x in c:
        print(x)
        break

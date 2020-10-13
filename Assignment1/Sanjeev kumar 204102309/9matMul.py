import numpy as np
from random import randrange as r
m = int(input('m:'))
n = int(input('n:'))
p = int(input('p:'))
def mat(m,n):
    a=[]
    b=[]
    for x in range(n):
        b.append(r(-2, 5))
    b = np.array(b)


    for x in range(m-1):
        for y in range(n):
            a.append(r(-2,5))
        p = np.array(a)

        a=[]
        b = np.vstack((b, p))
    return b
rows = []
num = 0

M1 = mat(m,n)
M2 = mat(n,p)
print('M1=',M1)
print('M2=',M2)
f = np.empty((0,p),int)


for x in range(0,m):
    for y in range(0,n):
        for z in range(0,p):
          num =num + M1[x][z]*M2[z][y]
        rows.append(num)
        num=0
    b= np.array([rows])
    rows.clear()
    f = np.append(f,b,axis=0)
print('Product=',f)
print('By inbuilt Function:',np.matmul(M1,M2))








m=int(input("Please enter value of row in MAT1:"))
n=int(input("please enter value of column MAT1:"))
mat1 = []
for i in range(0,m):
    mat1.append([])
for i in range(0,m) :
    for j in range(0,n):
        mat1[i].append(j)
        mat1[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("enter in row:",i+1,"column:",j+1)
        mat1[i][j]=int(input())
print(mat1)   

p=int(input("Please enter value of row in MAT2:"))
q=int(input("please enter value of column in MAT2:"))
mat2 = []
for i in range(0,p):
    mat2.append([])
for i in range(0,p) :
    for j in range(0,q):
        mat2[i].append(j)
        mat2[i][j]=0
for i in range(0,p):
    for j in range(0,q):
        print("enter in row:",i+1,"column:",j+1)
        mat2[i][j]=int(input())
print(mat2)        
            
Res=[] 
for i in range (0,m):
    Res.append([])
for i in range (0,m):
    for j in range(0,q):
        Res[i].append(j)
        Res[i][j]=0
for p in range(len(mat1)):
    for q in range(len(mat2[0])):
        for r in range(len(mat2)):
             Res[p][q] += mat1[p][r] * mat2[r][q]
print(Res)    
        
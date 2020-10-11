
m=int(input("Please enter value of row:"))
n=int(input("please enter value of column:"))
mat = []
for i in range(0,m):
    mat.append([])
for i in range(0,m) :
    for j in range(0,n):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("enter in row:",i+1,"column:",j+1)
        mat[i][j]=int(input())
print(mat)        
        
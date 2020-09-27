#Prime number in {a,b}
x=int(input("Please enter value of x:"))
y=int(input("please enter value of y:"))

for i in range(x,y+1):
    for m in range(2,i):
             if i%m==0:
                 break
             elif m==(i-1):
                print(i ,end= ",")
                 
                 
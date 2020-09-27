a=int(input('enter the value of a:'))
b=int(input('enter the value of b:'))
for i in range(a,b+1):
    c=0
    for j in range(1,i+1):
        if (i%j==0):
            c=c+1
    if(c==2):
        print(i)
        
        

    

        

li=[10,25,3,8,96,105,23,256,412,50,2,33,369,457,568]
for c in range(1,15):
    for i in range(1,15):
        if (li[i-1]<li[i]):
            s=li[i]
            li[i]=li[i-1]
            li[i-1]=s
print(li)
    
        

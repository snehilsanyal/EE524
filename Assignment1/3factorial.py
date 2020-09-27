N=int(input('enter any integer value:'))
i=1
f=1
for i in range(1,N+1):
    f=f*i
    i+=1

print("factorial is:",f)

print("enter two number")
a=int(input())
b=int(input())
temp1=a
temp2=b
if a>b:         #code for finding hcf
    rem=a%b
    while(rem!=0):
        a=b
        b=rem
        rem=a%b
        continue
    print(int((temp1*temp2)/b))#printing lcm
elif b>a:
    rem=b%a
    while(rem!=0):
        b=a
        a=rem
        rem=b%a
        continue
    print(int((temp1*temp2)/a))
else:
    print(a)




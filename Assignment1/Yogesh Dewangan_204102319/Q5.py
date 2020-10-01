#LCM of two number
x=int(input("Please enter the 1st number:"))
y=int(input("Please enter the 2nd number:"))
for m in range(1, x*y+1):
    if m%x==0 and m%y==0:
        print("The HCF is",m)
        break
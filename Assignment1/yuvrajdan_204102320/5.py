#Q5
def calculate_lcm(x,y):
    if x>y:
        larger=x
    else :
        larger=y
    while(True):
        if((larger%x==0) and (larger%y==0)):
            lcm=larger
            break
        larger+=1
    return lcm
num1=20
num2=24
result=calculate_lcm(num1,num2)
print(result)



#Q3
num=int(input('enter a number here:'))
factorial=1
if num<0:
    print("factorial is not exist")
elif num==0:
    print("the factorial is 1")
else:    
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of", num,"is",factorial)
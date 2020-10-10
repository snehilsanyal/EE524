print("Enter a number")
num=int(input())
fact=1
if num>=0:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
else:
    print("factorial of -Ve number is not possible")


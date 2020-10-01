##Program to print factorial of a given Number

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

print("Enter a number to calculate factorial:")
num1 = int(input())
print("The factorial of ", num1, "is ", factorial(num1))
        
        

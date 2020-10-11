def gcd(a,b): #function to find gcd of two numbers
    if a==0:
        return b
    else:
        return gcd(b%a,a)


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

#if any of the input is 0, it is Invalid
if a==0 or b==0:
    print('LCM of 0 and any other number could be 0 as both are factors of 0. But then LCM of any two numbers would be 0 since 0 is the least of all positive numbers. So it is not defined ')
    print('Invalid input!')
    exit()

#finding which number is smaller
if a>b:
    small=b
    large=a
else:
    small=a
    large=b

lcm=int((small*large)/gcd(small,large)) # since lcm(a,b)= (a*b)/gcd(a,b)
print(f'LCM of {small} and {large} is {lcm}')

def fact(n): #recursive funtion to find factorial of a number
    if n==1:
        return 1
    return n*fact(n-1)


print('Enter the number:')
a=int(input())
print(f'Factorial of {a} = {fact(a)}')

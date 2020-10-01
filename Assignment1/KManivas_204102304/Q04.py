## Program to find the prime numbers in the interval [a,b]

print("Enter two numbers, a and b:")
a = int(input())
b = int(input())
prime = None
print("List of prime numbers in the interval [",a,",",b,"] are: ")
for i in range(a,b+1):
    prime = True
    for j in range(2, (i//2)+1):
        if i%j == 0:
            prime = False
            break
        else:
            continue
    if prime and i!=0 and i!=1:
        print(i, end=' ')
print()

            
        
            
    

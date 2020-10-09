## Program to calculate LCM of two given numbers, a and b

print("Enter two number, a and b, and click Enter after entering each number:")
a = int(input())
b = int(input())
lcm = 1
if a>=b:
    max = a 
    min = b
else:
    max = b
    min = a 
if max%min == 0:
    lcm = max
else:
    i = 2
    while i<=min:
        if max%i == 0 and min%i == 0:
            max = max//i
            min = min//i
            lcm = lcm*i
        else:
            i += 1
    lcm = lcm * min * max

            
print("The LCM of",a,"and",b,"is:",lcm)
                
                
            

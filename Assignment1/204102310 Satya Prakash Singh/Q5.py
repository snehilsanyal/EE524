def LCM(a,b):
    if a % b == 0:
        lcm = a
    else:
        i = 1
        while a % b != 0:
            a *=i
            i +=1
        lcm = a
    return lcm

def main():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))

    if num1 > num2:
        lcm = LCM(num1,num2)
    else:
        lcm = LCM(num2,num1)
    print('The LCM of two numbers is: ',lcm)

if __name__ == '__main__':
    main()
